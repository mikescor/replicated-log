# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: log.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tlog.proto\x1a\x1bgoogle/protobuf/empty.proto\"W\n\nLogRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x1a\n\rwrite_concern\x18\x03 \x01(\x05H\x00\x88\x01\x01\x42\x10\n\x0e_write_concern\"0\n\x0bLogResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x10\n\x08received\x18\x02 \x01(\x08\"\x1f\n\x0bMessageList\x12\x10\n\x08messages\x18\x01 \x03(\t2g\n\x03Log\x12)\n\x0csend_message\x12\x0b.LogRequest\x1a\x0c.LogResponse\x12\x35\n\rlist_messages\x12\x16.google.protobuf.Empty\x1a\x0c.MessageListb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'log_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LOGREQUEST._serialized_start=42
  _LOGREQUEST._serialized_end=129
  _LOGRESPONSE._serialized_start=131
  _LOGRESPONSE._serialized_end=179
  _MESSAGELIST._serialized_start=181
  _MESSAGELIST._serialized_end=212
  _LOG._serialized_start=214
  _LOG._serialized_end=317
# @@protoc_insertion_point(module_scope)
