class Raspi:
    door_name: str
    passcode: str
    access_token: str
    max_attempts: int
    failed_streak: int

    def __init__(self, door_name, passcode, max_attempts):
        self.door_name = door_name
        self.passcode = passcode
        self.max_attempts = int(max_attempts)
        self.failed_streak = 0

    def set_access_token(self, token):
        self.access_token = "Bearer " + token

    def triggers_fail(self):
        self.failed_streak += 1
        if(self.failed_streak == self.max_attempts):
            self.reset_failed_streak()
            return True
        return False
            

    def reset_failed_streak(self):
        self.failed_streak = 0