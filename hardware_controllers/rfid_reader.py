from services.user_rfid_service import UserRFIDService
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

class RFIDReader:

    user_rfid_service: UserRFIDService
    reader: SimpleMFRC522

    def __init__(self, user_rfid_service):
        self.user_rfid_service = user_rfid_service
        self.reader = SimpleMFRC522()

    def read_rfid(self):
        id, _ = self.reader.read()

        self.user_rfid_service.look_for_user_rfid(int(id))
