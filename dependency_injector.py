from user_vectors_service import UserVectorsService
from user_vectors_repository import UserVectorRepository

class DependencyInjector:

    user_vectors_service : UserVectorsService
    user_vectors_repository : UserVectorRepository

    def _create_user_vectors_service(self):
        self.user_vectors_repository = UserVectorRepository("host='localhost' dbname='postgres' user='myuser' password='mypassword'")
        self.user_vectors_service = UserVectorsService(self.user_vectors_repository)

    def initialize(self):
        self._create_user_vectors_service()

    

