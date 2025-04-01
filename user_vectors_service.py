from imgbeddings import imgbeddings
from PIL import Image
from user_vectors_repository import UserVectorRepository

class UserVectorsService:

    userVectorsRepository : UserVectorRepository

    def __init__(self, userVectorsRepository):
        self.userVectorsRepository = userVectorsRepository

    def look_for_similar_user_vector(self, image_path):
        ibed = imgbeddings()

        img = Image.open(image_path)

        embedding = ibed.to_embeddings(img)[0]
        

