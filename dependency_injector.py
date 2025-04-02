from user_vectors_service import UserVectorsService
from user_vectors_repository import UserVectorRepository

class DependencyInjector:
    
    user_vectors_service : UserVectorsService
    user_vectors_repository : UserVectorRepository

    @staticmethod
    def _create_user_vectors_service():
        DependencyInjector.user_vectors_repository = UserVectorRepository("host='localhost' dbname='postgres' user='myuser' password='mypassword'")
        DependencyInjector.user_vectors_service = UserVectorsService(DependencyInjector.user_vectors_repository)

    @staticmethod
    def initialize():
        DependencyInjector._create_user_vectors_service()

    

