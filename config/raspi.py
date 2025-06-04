class Raspi:
    door_name: str
    passcode: str
    access_token: str

    def __init__(self, door_name, passcode):
        self.door_name = door_name
        self.passcode = passcode

    def set_access_token(self, token):
        self.access_token = token