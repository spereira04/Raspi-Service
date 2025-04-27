import transformers

_real_from_pretrained = transformers.AutoImageProcessor.from_pretrained

def _patched_from_pretrained(*args, **kwargs):
    kwargs["use_fast"] = True
    return _real_from_pretrained(*args, **kwargs)

transformers.AutoImageProcessor.from_pretrained = _patched_from_pretrained

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
    ibed: imgbeddings

    def __init__(self, baseUrl, accessService):
        self.baseUrl = baseUrl
        self.accessService = accessService
        self.ibed = imgbeddings()

    def look_for_similar_user_vector(self, buffer):
        access_time = int(time.time())

        embedding = self.ibed.to_embeddings(Image.open(io.BytesIO(buffer)))[0]
        
        gresponse: str
        try:
            # User Service
            response = requests.get(url=self.baseUrl+'/vector', json={'vector': np.float32(embedding).tolist()})
            body = json.loads(response.content)

            # Access Service
            if(response.status_code == 200):
                gresponse = self.accessService.send_successful_access(access_time, body['firstName'], body['lastName'], body['cid'])
            else:
                gresponse = self.accessService.send_unsuccessful_access(access_time)
        except requests.exceptions.ConnectionError:
            print("No connection to the User Service")
            return
        except grpc._channel._InactiveRpcError:
            print("No connection to the Access Service")
            return

        print(gresponse)
        # handle response