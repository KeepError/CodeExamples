# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: users_services.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import users_objects_pb2 as users__objects__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14users_services.proto\x1a\x13users_objects.proto\"!\n\x0eGetByIdRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"_\n\x0fGetByIdResponse\x12\x18\n\x04user\x18\x01 \x01(\x0b\x32\x05.UserH\x00\x88\x01\x01\x12\x1f\n\x05\x65rror\x18\x02 \x01(\x0e\x32\x0b.UsersErrorH\x01\x88\x01\x01\x42\x07\n\x05_userB\x08\n\x06_error\"\x0f\n\rCreateRequest\"^\n\x0e\x43reateResponse\x12\x18\n\x04user\x18\x01 \x01(\x0b\x32\x05.UserH\x00\x88\x01\x01\x12\x1f\n\x05\x65rror\x18\x02 \x01(\x0e\x32\x0b.UsersErrorH\x01\x88\x01\x01\x42\x07\n\x05_userB\x08\n\x06_error2g\n\x0cUsersService\x12,\n\x07GetById\x12\x0f.GetByIdRequest\x1a\x10.GetByIdResponse\x12)\n\x06\x43reate\x12\x0e.CreateRequest\x1a\x0f.CreateResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'users_services_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GETBYIDREQUEST._serialized_start=45
  _GETBYIDREQUEST._serialized_end=78
  _GETBYIDRESPONSE._serialized_start=80
  _GETBYIDRESPONSE._serialized_end=175
  _CREATEREQUEST._serialized_start=177
  _CREATEREQUEST._serialized_end=192
  _CREATERESPONSE._serialized_start=194
  _CREATERESPONSE._serialized_end=288
  _USERSSERVICE._serialized_start=290
  _USERSSERVICE._serialized_end=393
# @@protoc_insertion_point(module_scope)
