from camera import CV2Camera
from dependency_injector import DependencyInjector

if __name__ == '__main__':

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

