from imgbeddings import imgbeddings
import requests
import numpy as np
import time
import json
from access_service import AccessService
from PIL import Image
import io

class UserRFIDService:

    baseUrl: str
    accessService: AccessService

    def __init__(self, baseUrl, accessService):
        self.baseUrl = baseUrl
        self.accessService = accessService

    def look_for_user_rfid(self, rfid):
        access_time = int(time.time())
        
        response = requests.get(url=self.baseUrl+'/rfid/{rfid}')
        body = json.loads(response.content)
        
        gresponse: str
        if(response.status_code == 200):
            gresponse = self.accessService.send_successful_access(access_time, body['firstName'], body['lastName'], body['cid'])
        else:
            gresponse = self.accessService.send_unsuccessful_access(access_time)
        
        print(gresponse)
        # handle response