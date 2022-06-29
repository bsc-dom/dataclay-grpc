# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/metadata_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dprotos/metadata_service.proto\x12\x17protos.metadata_service\x1a\x1bgoogle/protobuf/empty.proto\"7\n\x11NewAccountRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"%\n\x11GetAccountRequest\x12\x10\n\x08username\x18\x01 \x01(\t\"\x14\n\x12GetAccountResponse\"P\n\x11NewSessionRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x17\n\x0f\x64\x65\x66\x61ult_dataset\x18\x03 \x01(\t\" \n\x12NewSessionResponse\x12\n\n\x02id\x18\x01 \x01(\t\"!\n\x13\x43loseSessionRequest\x12\n\n\x02id\x18\x01 \x01(\t\"H\n\x11NewDatasetRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x0f\n\x07\x64\x61taset\x18\x03 \x01(\t\",\n\x15GetDataclayIDResponse\x12\x13\n\x0b\x64\x61taclay_id\x18\x01 \x01(\t2\xbe\x04\n\x0fMetadataService\x12R\n\nNewAccount\x12*.protos.metadata_service.NewAccountRequest\x1a\x16.google.protobuf.Empty\"\x00\x12g\n\nGetAccount\x12*.protos.metadata_service.GetAccountRequest\x1a+.protos.metadata_service.GetAccountResponse\"\x00\x12g\n\nNewSession\x12*.protos.metadata_service.NewSessionRequest\x1a+.protos.metadata_service.NewSessionResponse\"\x00\x12V\n\x0c\x43loseSession\x12,.protos.metadata_service.CloseSessionRequest\x1a\x16.google.protobuf.Empty\"\x00\x12R\n\nNewDataset\x12*.protos.metadata_service.NewDatasetRequest\x1a\x16.google.protobuf.Empty\"\x00\x12Y\n\rGetDataclayID\x12\x16.google.protobuf.Empty\x1a..protos.metadata_service.GetDataclayIDResponse\"\x00\x62\x06proto3')



_NEWACCOUNTREQUEST = DESCRIPTOR.message_types_by_name['NewAccountRequest']
_GETACCOUNTREQUEST = DESCRIPTOR.message_types_by_name['GetAccountRequest']
_GETACCOUNTRESPONSE = DESCRIPTOR.message_types_by_name['GetAccountResponse']
_NEWSESSIONREQUEST = DESCRIPTOR.message_types_by_name['NewSessionRequest']
_NEWSESSIONRESPONSE = DESCRIPTOR.message_types_by_name['NewSessionResponse']
_CLOSESESSIONREQUEST = DESCRIPTOR.message_types_by_name['CloseSessionRequest']
_NEWDATASETREQUEST = DESCRIPTOR.message_types_by_name['NewDatasetRequest']
_GETDATACLAYIDRESPONSE = DESCRIPTOR.message_types_by_name['GetDataclayIDResponse']
NewAccountRequest = _reflection.GeneratedProtocolMessageType('NewAccountRequest', (_message.Message,), {
  'DESCRIPTOR' : _NEWACCOUNTREQUEST,
  '__module__' : 'protos.metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:protos.metadata_service.NewAccountRequest)
  })
_sym_db.RegisterMessage(NewAccountRequest)

GetAccountRequest = _reflection.GeneratedProtocolMessageType('GetAccountRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETACCOUNTREQUEST,
  '__module__' : 'protos.metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:protos.metadata_service.GetAccountRequest)
  })
_sym_db.RegisterMessage(GetAccountRequest)

GetAccountResponse = _reflection.GeneratedProtocolMessageType('GetAccountResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETACCOUNTRESPONSE,
  '__module__' : 'protos.metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:protos.metadata_service.GetAccountResponse)
  })
_sym_db.RegisterMessage(GetAccountResponse)

NewSessionRequest = _reflection.GeneratedProtocolMessageType('NewSessionRequest', (_message.Message,), {
  'DESCRIPTOR' : _NEWSESSIONREQUEST,
  '__module__' : 'protos.metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:protos.metadata_service.NewSessionRequest)
  })
_sym_db.RegisterMessage(NewSessionRequest)

NewSessionResponse = _reflection.GeneratedProtocolMessageType('NewSessionResponse', (_message.Message,), {
  'DESCRIPTOR' : _NEWSESSIONRESPONSE,
  '__module__' : 'protos.metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:protos.metadata_service.NewSessionResponse)
  })
_sym_db.RegisterMessage(NewSessionResponse)

CloseSessionRequest = _reflection.GeneratedProtocolMessageType('CloseSessionRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLOSESESSIONREQUEST,
  '__module__' : 'protos.metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:protos.metadata_service.CloseSessionRequest)
  })
_sym_db.RegisterMessage(CloseSessionRequest)

NewDatasetRequest = _reflection.GeneratedProtocolMessageType('NewDatasetRequest', (_message.Message,), {
  'DESCRIPTOR' : _NEWDATASETREQUEST,
  '__module__' : 'protos.metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:protos.metadata_service.NewDatasetRequest)
  })
_sym_db.RegisterMessage(NewDatasetRequest)

GetDataclayIDResponse = _reflection.GeneratedProtocolMessageType('GetDataclayIDResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETDATACLAYIDRESPONSE,
  '__module__' : 'protos.metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:protos.metadata_service.GetDataclayIDResponse)
  })
_sym_db.RegisterMessage(GetDataclayIDResponse)

_METADATASERVICE = DESCRIPTOR.services_by_name['MetadataService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _NEWACCOUNTREQUEST._serialized_start=87
  _NEWACCOUNTREQUEST._serialized_end=142
  _GETACCOUNTREQUEST._serialized_start=144
  _GETACCOUNTREQUEST._serialized_end=181
  _GETACCOUNTRESPONSE._serialized_start=183
  _GETACCOUNTRESPONSE._serialized_end=203
  _NEWSESSIONREQUEST._serialized_start=205
  _NEWSESSIONREQUEST._serialized_end=285
  _NEWSESSIONRESPONSE._serialized_start=287
  _NEWSESSIONRESPONSE._serialized_end=319
  _CLOSESESSIONREQUEST._serialized_start=321
  _CLOSESESSIONREQUEST._serialized_end=354
  _NEWDATASETREQUEST._serialized_start=356
  _NEWDATASETREQUEST._serialized_end=428
  _GETDATACLAYIDRESPONSE._serialized_start=430
  _GETDATACLAYIDRESPONSE._serialized_end=474
  _METADATASERVICE._serialized_start=477
  _METADATASERVICE._serialized_end=1051
# @@protoc_insertion_point(module_scope)
