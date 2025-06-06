import cv2
from cv2.typing import MatLike
import datetime
import sys
from services.user_vectors_service import UserVectorsService
import threading
from picamera2 import Picamera2

class CV2Camera:

    user_vectors_service: UserVectorsService
    video_capture: Picamera2

    haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +  'haarcascade_frontalface_default.xml')

    image_last_time_taken = datetime.datetime.now()

    TIME_BETWEEN_PICTURES = 8

    current_faces = []
    current_frame = None

    def __init__(self, user_vectors_service: UserVectorsService):
        self.user_vectors_service = user_vectors_service
        self.video_capture = Picamera2()
        self.video_capture.configure(self.video_capture.create_video_configuration())
        self.video_capture.start()

    def _can_take_picture(self):
        current_time = datetime.datetime.now()
        (current_time - self.image_last_time_taken).total_seconds()
        return (current_time - self.image_last_time_taken).total_seconds() >= self.TIME_BETWEEN_PICTURES

    def _take_picture(self, x, y, w, h):
        if self._can_take_picture():
            image = self.current_frame[y:y+h, x:x+w]
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            _, buffer = cv2.imencode('.jpg', gray_image)

            self.image_last_time_taken = datetime.datetime.now()

            threading.Thread(target=self.user_vectors_service.look_for_similar_user_vector, args=(buffer,)).start()


    def read_frame(self):
        self.current_frame = self.video_capture.capture_array()

    def detect_faces(self):
        self.current_faces = self.haar_cascade.detectMultiScale(
            self.current_frame, scaleFactor=1.05, minNeighbors=3, minSize=(300, 300)
        )
        self._draw_faces_in_frame()

    def faces_detected(self):
        return len(self.current_faces) >= 1

    def _draw_faces_in_frame(self):
        if len(self.current_faces) < 1:
            return
        
        x, y, w, h = self.current_faces[0]

        cv2.rectangle(self.current_frame, (x, y), (x+h, y+w), (0, 0, 255), 2)

        self._take_picture(x, y, w, h)

    def show_frame(self, winname):
        try:
            cv2.imshow(winname, self.current_frame)
        except:
            print('no image')

    def check_for_exit(self):
        return cv2.waitKey(1) == ord("q")

    def exit(self):
        self.video_capture.stop()
        cv2.destroyAllWindows()
