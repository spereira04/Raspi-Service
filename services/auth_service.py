import requests
import json
from config.raspi import Raspi

class AuthService:
    baseUrl: str
    raspi: Raspi
	

    def __init__(self, baseUrl, raspi):
        self.baseUrl = baseUrl
        self.raspi = raspi

    def log_in(self):
        try:
            data = {'doorName': self.raspi.door_name, 'passcode': self.raspi.passcode}
            response = requests.post(url=self.baseUrl+'/doors/connect', data=data)
            print(response.json())
            print('=============================================')
            print(response.json()['token'])
            self.raspi.set_access_token(response.json()['token'])
            return True
        except requests.exceptions.ConnectionError:
            print("No connection to the User Service")
            return False
    
        