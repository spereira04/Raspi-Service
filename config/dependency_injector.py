from services.user_vectors_service import UserVectorsService
from services.user_rfid_service import UserRFIDService
from services.access_service import AccessService
from config.raspi import Raspi

import os
from dotenv import find_dotenv, load_dotenv

class DependencyInjector:
    
    user_vectors_service: UserVectorsService
    user_rfid_service: UserRFIDService

    access_service: AccessService

    raspi: Raspi

    @staticmethod
    def _create_user_vectors_service():
        DependencyInjector.user_vectors_service = UserVectorsService(os.getenv("user-service-base-url"), DependencyInjector.access_service, DependencyInjector.raspi)

    @staticmethod
    def _create_user_rfid_service():
        DependencyInjector.user_rfid_service = UserRFIDService(os.getenv("user-service-base-url"), DependencyInjector.access_service, DependencyInjector.raspi)

    @staticmethod
    def _create_access_service():
        DependencyInjector.access_service = AccessService(os.getenv("access-service-base-url"), DependencyInjector.raspi)

    @staticmethod
    def _create_raspi():
        DependencyInjector.raspi = Raspi(os.getenv("door-name"), os.getenv("passcode"), int(os.getenv("door-access-level")))

    @staticmethod
    def initialize():

        dotenv_path = find_dotenv()

        load_dotenv(dotenv_path)

        DependencyInjector._create_raspi()
        DependencyInjector._create_access_service()
        DependencyInjector._create_user_vectors_service()
        DependencyInjector._create_user_rfid_service()
