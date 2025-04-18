from imgbeddings import imgbeddings
import requests
import numpy as np
import time
import json
from access_service import AccessService

class UserVectorsService:

    baseUrl: str
    accessService: AccessService

    def __init__(self, baseUrl, accessService):
        self.baseUrl = baseUrl
        self.accessService = accessService

    def look_for_similar_user_vector(self, picture):
        access_time = int(time.time())
        ibed = imgbeddings()
        embedding = ibed.to_embeddings(picture)[0]
        
        response = requests.get(url=self.baseUrl+'/vector', json={'vector': np.float32(embedding).tolist()})
        body = json.loads(response.content)
        
        gresponse: str
        if(response.status_code == 200):
            gresponse = self.accessService.send_successful_access(access_time, body['firstName'], body['lastName'], body['cid'])
        else:
            gresponse = self.accessService.send_unsuccessful_access(access_time)
        
        # handle response


    def save_embedding(self):
        ibed = imgbeddings()

        embedding = ibed.to_embeddings("resources/face.jpg")[0]

        print(embedding)

        
        response = requests.post(url= 'http://localhost:8080/users/8b7187c0-16f5-4d3c-bdcb-48bb783776e7/vector', json={'vector': np.float32(embedding).tolist() })
        print(response.status_code)
        

