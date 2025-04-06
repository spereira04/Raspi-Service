import cv2
from cv2.typing import MatLike
import datetime
import sys
from user_vectors_service import UserVectorsService

class CV2Camera:

    user_vectors_service: UserVectorsService

    haar_cascade = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")
    video_capture = cv2.VideoCapture(0)

    image_last_time_taken = datetime.datetime.now()

    TIME_BETWEEN_PICTURES = 5
    PICTURE_PATH = 'resources/face.jpg'

    current_faces = []
    current_frame_ret = False
    current_frame = None

    def __init__(self, user_vectors_service: UserVectorsService):
        self.user_vectors_service = user_vectors_service

    def _can_take_picture(self):
        current_time = datetime.datetime.now()
        (current_time - self.image_last_time_taken).total_seconds()
        return (current_time - self.image_last_time_taken).total_seconds() >= self.TIME_BETWEEN_PICTURES

    def _take_picture(self, x, y, w, h):
        if self._can_take_picture():
            image = self.current_frame[y:y+h, x:x+w]
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(self.PICTURE_PATH, gray_image)
            self.image_last_time_taken = datetime.datetime.now()
            self.user_vectors_service.look_for_similar_user_vector(self.PICTURE_PATH)

    def read_frame(self):
        self.current_frame_ret, self.current_frame = self.video_capture.read()

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
        cv2.imshow(winname, self.current_frame)

    def check_for_exit(self):
        return cv2.waitKey(1) == ord("q")

    def exit(self):
        self.video_capture.release()
        cv2.destroyAllWindows()

    def verify_input_video_capture_device(self):
        if not self.video_capture.isOpened():
            sys.exit('Video source not found')
