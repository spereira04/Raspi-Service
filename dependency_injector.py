from user_vectors_service import UserVectorsService
from user_vectors_repository import UserVectorRepository
from access_service import AccesService

class DependencyInjector:
    
    user_vectors_service: UserVectorsService
    user_vectors_repository: UserVectorRepository

    access_service: AccesService

    @staticmethod
    def _create_user_vectors_service():
        DependencyInjector.user_vectors_repository = UserVectorRepository("host='localhost' dbname='postgres' user='myuser' password='mypassword'")
        DependencyInjector.user_vectors_service = UserVectorsService(DependencyInjector.user_vectors_repository)

    @staticmethod
    def _create_access_service():
        DependencyInjector.access_service = AccesService('10.252.50.2:9090')

    @staticmethod
    def initialize():
        DependencyInjector._create_user_vectors_service()
        DependencyInjector._create_access_service()

    

