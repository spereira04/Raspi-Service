class Raspi:
    door_name: str
    passcode: int
    door_access_level: int
    access_token: str

    def __init__(self, door_name, passcode, door_access_level):
        self.door_name = door_name
        self.passcode = passcode
        self.door_access_level = door_access_level

    def set_access_token(self, token):
        print(token)
        self.access_token = token