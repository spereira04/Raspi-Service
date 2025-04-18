from user_vectors_service import UserVectorsService
from access_service import AccessService

import os
from dotenv import find_dotenv, load_dotenv

class DependencyInjector:
    
    user_vectors_service: UserVectorsService

    access_service: AccessService

    @staticmethod
    def _create_user_vectors_service():
        DependencyInjector.user_vectors_service = UserVectorsService(os.getenv("user-vectors-service-base-url"), DependencyInjector.access_service)

    @staticmethod
    def _create_access_service():
        DependencyInjector.access_service = AccessService(os.getenv("access-service-base-url"))

    @staticmethod
    def initialize():

        dotenv_path = find_dotenv()

        load_dotenv(dotenv_path)

        DependencyInjector._create_access_service()
        DependencyInjector._create_user_vectors_service()
        

    

