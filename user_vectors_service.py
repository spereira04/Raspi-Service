from imgbeddings import imgbeddings
import requests
import numpy as np

class UserVectorsService:

    baseUrl: str

    def __init__(self, baseUrl):
        self.baseUrl = baseUrl

    def look_for_similar_user_vector(self, picture):
        ibed = imgbeddings()
        embedding = ibed.to_embeddings(picture)[0]
        
        response = requests.get(url=self.baseUrl+'/vector', json={'vector': np.float32(embedding).tolist()})
        print(response.content)

    def save_embedding(self):
        ibed = imgbeddings()

        embedding = ibed.to_embeddings("resources/face.jpg")[0]

        print(embedding)

        
        response = requests.post(url=self.baseUrl+'/vector', json={'userId': '14ed3a2e-c82b-40bc-946d-e1cea1af457c', 'vector': np.float32(embedding).tolist() })
        print(response.status_code)
        

