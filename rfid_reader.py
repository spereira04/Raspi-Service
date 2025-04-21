from imgbeddings import imgbeddings
from user_rfid_service import UserRFIDService
from access_service import AccessService
from PIL import Image
import io

class RFIDReader:

    user_rfid_service: UserRFIDService

    def __init__(self, user_rfid_service):
        self.user_rfid_service = user_rfid_service

    def read_rfid(self):
        read_code = input('METEMELA: ')
        self.user_rfid_service.look_for_user_rfid(int(read_code))


