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


    def send_successful_access(self, time, full_name, cid, accessType):
        successfulAccessDTO = proto.access_pb2.SuccessfulAccessDTO(time=time, fullName=full_name, cid=cid, accessType=accessType, doorName=self.raspi.door_name)
        return self.stub.SubmitSuccessfulAccess(successfulAccessDTO, metadata = [('authorization', self.raspi.access_token)])

    def send_unsuccessful_access(self, time, accessType):
        failedAccessDTO = proto.access_pb2.FailedAccessDTO(time=time, accessType=accessType, doorName=self.raspi.door_name)
        return self.stub.SubmitFailedAccess(failedAccessDTO, metadata = [('authorization', self.raspi.access_token)])
    
    def send_email(self, time, accessType):
        failedAccessDTO = proto.access_pb2.FailedAccessDTO(time=time, accessType=accessType, doorName=self.raspi.door_name)
        print("send email triggered")
        return self.stub.SendEmail(failedAccessDTO, metadata = [('authorization', self.raspi.access_token)])