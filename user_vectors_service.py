from imgbeddings import imgbeddings
import requests
import numpy as np
import time
import json
from access_service import AccessService
from PIL import Image
import io
import grpc

class UserVectorsService:

    baseUrl: str
    accessService: AccessService

    def __init__(self, baseUrl, accessService):
        self.baseUrl = baseUrl
        self.accessService = accessService

    def look_for_similar_user_vector(self, buffer):
        access_time = int(time.time())
        ibed = imgbeddings()

        embedding = ibed.to_embeddings(Image.open(io.BytesIO(buffer)))[0]
        
        try:
            # User Service
            response = requests.get(url=self.baseUrl+'/vector', json={'vector': np.float32(embedding).tolist()})
            body = json.loads(response.content)

            # Access Service
            gresponse: str
            if(response.status_code == 200):
                gresponse = self.accessService.send_successful_access(access_time, body['firstName'], body['lastName'], body['cid'])
            else:
                gresponse = self.accessService.send_unsuccessful_access(access_time)
        except requests.exceptions.ConnectionError as conn_error:
            print("No connection to the User Service")
        except grpc._channel._InactiveRpcError as conn_error:
            print("No connection to the Access Service")

        print(gresponse)
        # handle response