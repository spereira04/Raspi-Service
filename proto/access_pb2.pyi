from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AccessTypeEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CAMERA: _ClassVar[AccessTypeEnum]
    RFID: _ClassVar[AccessTypeEnum]
CAMERA: AccessTypeEnum
RFID: AccessTypeEnum

class SuccessfulAccessDTO(_message.Message):
    __slots__ = ("time", "firstName", "lastName", "cid", "accessType", "doorName")
    TIME_FIELD_NUMBER: _ClassVar[int]
    FIRSTNAME_FIELD_NUMBER: _ClassVar[int]
    LASTNAME_FIELD_NUMBER: _ClassVar[int]
    CID_FIELD_NUMBER: _ClassVar[int]
    ACCESSTYPE_FIELD_NUMBER: _ClassVar[int]
    DOORNAME_FIELD_NUMBER: _ClassVar[int]
    time: int
    firstName: str
    lastName: str
    cid: str
    accessType: AccessTypeEnum
    doorName: str
    def __init__(self, time: _Optional[int] = ..., firstName: _Optional[str] = ..., lastName: _Optional[str] = ..., cid: _Optional[str] = ..., accessType: _Optional[_Union[AccessTypeEnum, str]] = ..., doorName: _Optional[str] = ...) -> None: ...

class FailedAccessDTO(_message.Message):
    __slots__ = ("time", "accessType", "doorName")
    TIME_FIELD_NUMBER: _ClassVar[int]
    ACCESSTYPE_FIELD_NUMBER: _ClassVar[int]
    DOORNAME_FIELD_NUMBER: _ClassVar[int]
    time: int
    accessType: AccessTypeEnum
    doorName: str
    def __init__(self, time: _Optional[int] = ..., accessType: _Optional[_Union[AccessTypeEnum, str]] = ..., doorName: _Optional[str] = ...) -> None: ...

class SubmitResponseDTO(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: str
    def __init__(self, response: _Optional[str] = ...) -> None: ...

class DoorCredentialsDTO(_message.Message):
    __slots__ = ("doorName", "doorAccessLevel", "passcode")
    DOORNAME_FIELD_NUMBER: _ClassVar[int]
    DOORACCESSLEVEL_FIELD_NUMBER: _ClassVar[int]
    PASSCODE_FIELD_NUMBER: _ClassVar[int]
    doorName: str
    doorAccessLevel: int
    passcode: str
    def __init__(self, doorName: _Optional[str] = ..., doorAccessLevel: _Optional[int] = ..., passcode: _Optional[str] = ...) -> None: ...

class DoorTokenDTO(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...
