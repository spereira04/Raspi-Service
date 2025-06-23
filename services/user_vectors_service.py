import warnings
from imgbeddings import imgbeddings
import requests
import numpy as np
import time
import json
from services.access_service import AccessService
from PIL import Image
import io
import grpc
from config.raspi import Raspi
from proto.access_pb2 import AccessTypeEnum

warnings.filterwarnings("ignore", category=FutureWarning, message=".*feature_extractor.*")
class UserVectorsService:

    baseUrl: str
    accessService: AccessService
    ibed: imgbeddings
    raspi: Raspi

    def __init__(self, baseUrl, accessService, raspi):
        self.baseUrl = baseUrl
        self.accessService = accessService
        self.ibed = imgbeddings()
        self.raspi = raspi

    def look_for_similar_user_vector(self, buffer):
        access_time = int(time.time() + 3*60*60)

        embedding = self.ibed.to_embeddings(Image.open(io.BytesIO(buffer)))[0]
        
        gresponse: str
        try:
            # User Service
            params = {'doorName' : self.raspi.door_name }
            response = requests.get(url=self.baseUrl+'/vector', json={'vector': np.float32(embedding).tolist()}, params=params)
            body = json.loads(response.content)

            # Access Service
            if(response.status_code == 200):
                gresponse = self.accessService.send_successful_access(access_time, body['fullName'], body['cid'], AccessTypeEnum.CAMERA)
                self.raspi.reset_failed_streak()
            else:
                gresponse = self.accessService.send_unsuccessful_access(access_time, AccessTypeEnum.CAMERA)
                if(self.raspi.triggers_fail()):
                    self.accessService.send_email(access_time, AccessTypeEnum.CAMERA)
        except requests.exceptions.ConnectionError:
            print("No connection to the User Service")
            return
        except grpc._channel._InactiveRpcError:
            print("No connection to the Access Service")
            return

        print(gresponse)
        # handle response