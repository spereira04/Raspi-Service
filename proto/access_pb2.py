# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: proto/access.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'proto/access.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12proto/access.proto\"y\n\x13SuccessfulAccessDTO\x12\x0c\n\x04time\x18\x01 \x01(\x03\x12\x10\n\x08\x66ullName\x18\x02 \x01(\t\x12\x0b\n\x03\x63id\x18\x03 \x01(\t\x12#\n\naccessType\x18\x04 \x01(\x0e\x32\x0f.AccessTypeEnum\x12\x10\n\x08\x64oorName\x18\x05 \x01(\t\"V\n\x0f\x46\x61iledAccessDTO\x12\x0c\n\x04time\x18\x01 \x01(\x03\x12#\n\naccessType\x18\x02 \x01(\x0e\x32\x0f.AccessTypeEnum\x12\x10\n\x08\x64oorName\x18\x03 \x01(\t\"%\n\x11SubmitResponseDTO\x12\x10\n\x08response\x18\x01 \x01(\t*&\n\x0e\x41\x63\x63\x65ssTypeEnum\x12\n\n\x06\x43\x41MERA\x10\x00\x12\x08\n\x04RFID\x10\x01\x32\xc1\x01\n\x06\x41\x63\x63\x65ss\x12\x44\n\x16SubmitSuccessfulAccess\x12\x14.SuccessfulAccessDTO\x1a\x12.SubmitResponseDTO\"\x00\x12<\n\x12SubmitFailedAccess\x12\x10.FailedAccessDTO\x1a\x12.SubmitResponseDTO\"\x00\x12\x33\n\tSendEmail\x12\x10.FailedAccessDTO\x1a\x12.SubmitResponseDTO\"\x00\x42\x36\n%org.springframework.grpc.sample.protoB\x0b\x41\x63\x63\x65ssProtoP\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.access_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n%org.springframework.grpc.sample.protoB\013AccessProtoP\000'
  _globals['_ACCESSTYPEENUM']._serialized_start=272
  _globals['_ACCESSTYPEENUM']._serialized_end=310
  _globals['_SUCCESSFULACCESSDTO']._serialized_start=22
  _globals['_SUCCESSFULACCESSDTO']._serialized_end=143
  _globals['_FAILEDACCESSDTO']._serialized_start=145
  _globals['_FAILEDACCESSDTO']._serialized_end=231
  _globals['_SUBMITRESPONSEDTO']._serialized_start=233
  _globals['_SUBMITRESPONSEDTO']._serialized_end=270
  _globals['_ACCESS']._serialized_start=313
  _globals['_ACCESS']._serialized_end=506
# @@protoc_insertion_point(module_scope)
