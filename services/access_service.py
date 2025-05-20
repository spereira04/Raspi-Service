from config.raspi import Raspi
import grpc
import proto.access_pb2, proto.access_pb2_grpc

class AccessService:

    stub: proto.access_pb2_grpc.AccessStub

    raspi: Raspi

    def __init__(self, channel_url, raspi):
        channel = grpc.insecure_channel(channel_url)
        self.stub = proto.access_pb2_grpc.AccessStub(channel)
        self.raspi = raspi
        self.connect()


    def send_successful_access(self, time, firstName, lastName, cid):
        successfulAccessDTO = proto.access_pb2.SuccessfulAccessDTO(time=time, firstName=firstName, lastName=lastName, cid=cid)
        return self.stub.SubmitSuccessfulAccess(successfulAccessDTO, metadata = [('authorization', self.raspi.access_token)])

    def send_unsuccessful_access(self, time):
        return self.stub.SubmitFailedAccess(proto.access_pb2.FailedAccessDTO(time=time), metadata = [('authorization', self.raspi.access_token)])

    def connect(self):
        doorCredentialsDTO = proto.access_pb2.DoorCredentialsDTO(
            doorName = self.raspi.door_name,
            passcode = self.raspi.passcode,
            doorAccessLevel = self.raspi.door_access_level)
        
        self.raspi.set_access_token(self.stub.Connect(doorCredentialsDTO).token)