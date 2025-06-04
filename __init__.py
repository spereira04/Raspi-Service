from hardware_controllers.camera import CV2Camera
from config.dependency_injector import DependencyInjector
from hardware_controllers.rfid_reader import RFIDReader
import threading
import time

def log_in():
    auth_service = DependencyInjector.auth_service

    connected = False

    while (not connected):
        print("Attempting login")
        connected = auth_service.log_in()

def start_camera_detection():
    camera = CV2Camera(DependencyInjector.user_vectors_service)

    while True:
        camera.read_frame()

        camera.detect_faces()

        camera.show_frame("Face recon")
        
        if camera.check_for_exit():
            break

    camera.exit()

def start_rfid_detection():
    DependencyInjector.initialize()

    log_in()

    rfid_reader = RFIDReader(DependencyInjector.user_rfid_service)

    while True:
        rfid_reader.read_rfid()  
        time.sleep(3)

if __name__ == '__main__':
    DependencyInjector.initialize()

    log_in()
    
    threading.Thread(target=start_rfid_detection).start()
    start_camera_detection()
