from camera import CV2Camera
from dependency_injector import DependencyInjector

dependency_injector = DependencyInjector()

if __name__ == '__main__':

    dependency_injector.initialize()

    camera = CV2Camera()

    camera.verify_input_video_capture_device()

    while True:
        camera.read_frame()


        camera.detect_faces()

        if not camera.faces_detected():
            continue

        camera.draw_faces_in_frame()

        camera.show_frame("Face recon")

        if camera.check_for_exit():
            break

    camera.exit()

