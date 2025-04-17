from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SuccessfulAccessDTO(_message.Message):
    __slots__ = ("time", "firstName", "lastName", "cid")
    TIME_FIELD_NUMBER: _ClassVar[int]
    FIRSTNAME_FIELD_NUMBER: _ClassVar[int]
    LASTNAME_FIELD_NUMBER: _ClassVar[int]
    CID_FIELD_NUMBER: _ClassVar[int]
    time: int
    firstName: str
    lastName: str
    cid: str
    def __init__(self, time: _Optional[int] = ..., firstName: _Optional[str] = ..., lastName: _Optional[str] = ..., cid: _Optional[str] = ...) -> None: ...

class FailedAccessDTO(_message.Message):
    __slots__ = ("time",)
    TIME_FIELD_NUMBER: _ClassVar[int]
    time: int
    def __init__(self, time: _Optional[int] = ...) -> None: ...

class SubmitResponseDTO(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: str
    def __init__(self, response: _Optional[str] = ...) -> None: ...
