# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: greet.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bgreet.proto\"\x1c\n\x0cGreetRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\" \n\rGreetResponse\x12\x0f\n\x07message\x18\x01 \x01(\t26\n\x0cGreetService\x12&\n\x05Greet\x12\r.GreetRequest\x1a\x0e.GreetResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'greet_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_GREETREQUEST']._serialized_start=15
  _globals['_GREETREQUEST']._serialized_end=43
  _globals['_GREETRESPONSE']._serialized_start=45
  _globals['_GREETRESPONSE']._serialized_end=77
  _globals['_GREETSERVICE']._serialized_start=79
  _globals['_GREETSERVICE']._serialized_end=133
# @@protoc_insertion_point(module_scope)
