from build.proto.access_pb2_grpc import AccessStub
from build.proto.access_pb2 import FailedAccessDTO
import grpc

class AccesService:

    stub: AccessStub

    def __init__(self, channel_url):
        channel = grpc.insecure_channel(channel_url)
        self.stub = AccessStub(channel)


    def send_successful_access(self):
        self.stub.SumbitSuccessfulAccess('{}')

    def send_unsuccessful_access(self):
        self.stub.SumbitFailedAccess(FailedAccessDTO(time=1744146241))