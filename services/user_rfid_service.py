import requests
import time
import json
from services.access_service import AccessService
import grpc
from config.raspi import Raspi

class UserRFIDService:

    baseUrl: str
    accessService: AccessService
    raspi : Raspi

    def __init__(self, baseUrl, accessService, raspi):
        self.baseUrl = baseUrl
        self.accessService = accessService
        self.raspi = raspi

    def look_for_user_rfid(self, rfid):
        access_time = int(time.time())

        gresponse: str
        # try:    
        params = {'doorName' : self.raspi.door_name }
        response = requests.get(url=self.baseUrl+'/rfid/'+str(rfid), params=params)
        body = json.loads(response.content)
        
        if(response.status_code == 200):
            gresponse = self.accessService.send_successful_access(access_time, body['fullName'], body['cid'])
        else:
            gresponse = self.accessService.send_unsuccessful_access(access_time)
        # except requests.exceptions.ConnectionError:
        #     print("No connection to the User Service")
        #     return
        # except grpc._channel._InactiveRpcError:
        #     print("No connection to the Access Service")
        #     return


        print(gresponse)
        # handle response