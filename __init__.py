from camera import CV2Camera
from dependency_injector import DependencyInjector
from rfid_reader import RFIDReader
import threading

def start_camera_detection():
    DependencyInjector.initialize()

    camera = CV2Camera(DependencyInjector.user_vectors_service)

    camera.verify_input_video_capture_device()

    while True:
        camera.read_frame()

        camera.detect_faces()

        camera.show_frame("Face recon")
        
        if camera.check_for_exit():
            break

    camera.exit()

def start_rfid_detection():
    DependencyInjector.initialize()

    rfid_reader = RFIDReader(DependencyInjector.user_rfid_service)

    while True:
        rfid_reader.read_rfid()  


if __name__ == '__main__':
    threading.Thread(target=start_rfid_detection).start()
    start_camera_detection()
