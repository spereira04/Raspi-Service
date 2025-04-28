
import grpc
import proto.access_pb2, proto.access_pb2_grpc

class AccessService:

    stub: proto.access_pb2_grpc.AccessStub

    def __init__(self, channel_url):
        channel = grpc.insecure_channel(channel_url)
        self.stub = proto.access_pb2_grpc.AccessStub(channel)


    def send_successful_access(self, time, firstName, lastName, cid):
        successfulAccessDTO = proto.access_pb2.SuccessfulAccessDTO(time=time, firstName=firstName, lastName=lastName, cid=cid)
        return self.stub.SubmitSuccessfulAccess(successfulAccessDTO)

    def send_unsuccessful_access(self, time):
        return self.stub.SubmitFailedAccess(proto.access_pb2.FailedAccessDTO(time=time))
