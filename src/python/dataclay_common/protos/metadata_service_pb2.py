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
from . import common_messages_pb2 as protos_dot_common__messages__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dprotos/metadata_service.proto\x12\x17protos.metadata_service\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cprotos/common_messages.proto\"7\n\x11NewAccountRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"%\n\x11GetAccountRequest\x12\x10\n\x08username\x18\x01 \x01(\t\"\x14\n\x12GetAccountResponse\"P\n\x11NewSessionRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x17\n\x0f\x64\x65\x66\x61ult_dataset\x18\x03 \x01(\t\" \n\x12NewSessionResponse\x12\n\n\x02id\x18\x01 \x01(\t\"!\n\x13\x43loseSessionRequest\x12\n\n\x02id\x18\x01 \x01(\t\"H\n\x11NewDatasetRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x0f\n\x07\x64\x61taset\x18\x03 \x01(\t\"x\n\"GetAllExecutionEnvironmentsRequest\x12&\n\x08language\x18\x01 \x01(\x0e\x32\x14.protos.common.Langs\x12\x14\n\x0cget_external\x18\x02 \x01(\x08\x12\x14\n\x0c\x66rom_backend\x18\x03 \x01(\x08\"\xd7\x01\n#GetAllExecutionEnvironmentsResponse\x12[\n\x08\x65xe_envs\x18\x01 \x03(\x0b\x32I.protos.metadata_service.GetAllExecutionEnvironmentsResponse.ExeEnvsEntry\x1aS\n\x0c\x45xeEnvsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x32\n\x05value\x18\x02 \x01(\x0b\x32#.protos.common.ExecutionEnvironment:\x02\x38\x01\",\n\x15GetDataclayIDResponse\x12\x13\n\x0b\x64\x61taclay_id\x18\x01 \x01(\t\"u\n\x15\x41utoRegisterEERequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08hostname\x18\x03 \x01(\t\x12\x0c\n\x04port\x18\x04 \x01(\x05\x12\"\n\x04lang\x18\x05 \x01(\x0e\x32\x14.protos.common.Langs2\xb7\x06\n\x0fMetadataService\x12R\n\nNewAccount\x12*.protos.metadata_service.NewAccountRequest\x1a\x16.google.protobuf.Empty\"\x00\x12g\n\nGetAccount\x12*.protos.metadata_service.GetAccountRequest\x1a+.protos.metadata_service.GetAccountResponse\"\x00\x12g\n\nNewSession\x12*.protos.metadata_service.NewSessionRequest\x1a+.protos.metadata_service.NewSessionResponse\"\x00\x12V\n\x0c\x43loseSession\x12,.protos.metadata_service.CloseSessionRequest\x1a\x16.google.protobuf.Empty\"\x00\x12R\n\nNewDataset\x12*.protos.metadata_service.NewDatasetRequest\x1a\x16.google.protobuf.Empty\"\x00\x12\x9a\x01\n\x1bGetAllExecutionEnvironments\x12;.protos.metadata_service.GetAllExecutionEnvironmentsRequest\x1a<.protos.metadata_service.GetAllExecutionEnvironmentsResponse\"\x00\x12Y\n\rGetDataclayID\x12\x16.google.protobuf.Empty\x1a..protos.metadata_service.GetDataclayIDResponse\"\x00\x12Z\n\x0e\x41utoregisterEE\x12..protos.metadata_service.AutoRegisterEERequest\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3')



_NEWACCOUNTREQUEST = DESCRIPTOR.message_types_by_name['NewAccountRequest']
_GETACCOUNTREQUEST = DESCRIPTOR.message_types_by_name['GetAccountRequest']
_GETACCOUNTRESPONSE = DESCRIPTOR.message_types_by_name['GetAccountResponse']
_NEWSESSIONREQUEST = DESCRIPTOR.message_types_by_name['NewSessionRequest']
_NEWSESSIONRESPONSE = DESCRIPTOR.message_types_by_name['NewSessionResponse']
_CLOSESESSIONREQUEST = DESCRIPTOR.message_types_by_name['CloseSessionRequest']
_NEWDATASETREQUEST = DESCRIPTOR.message_types_by_name['NewDatasetRequest']
_GETALLEXECUTIONENVIRONMENTSREQUEST = DESCRIPTOR.message_types_by_name['GetAllExecutionEnvironmentsRequest']
_GETALLEXECUTIONENVIRONMENTSRESPONSE = DESCRIPTOR.message_types_by_name['GetAllExecutionEnvironmentsResponse']
_GETALLEXECUTIONENVIRONMENTSRESPONSE_EXEENVSENTRY = _GETALLEXECUTIONENVIRONMENTSRESPONSE.nested_types_by_name['ExeEnvsEntry']
_GETDATACLAYIDRESPONSE = DESCRIPTOR.message_types_by_name['GetDataclayIDResponse']
_AUTOREGISTEREEREQUEST = DESCRIPTOR.message_types_by_name['AutoRegisterEERequest']
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

GetAllExecutionEnvironmentsRequest = _reflection.GeneratedProtocolMessageType('GetAllExecutionEnvironmentsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETALLEXECUTIONENVIRONMENTSREQUEST,
  '__module__' : 'protos.metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:protos.metadata_service.GetAllExecutionEnvironmentsRequest)
  })
_sym_db.RegisterMessage(GetAllExecutionEnvironmentsRequest)

GetAllExecutionEnvironmentsResponse = _reflection.GeneratedProtocolMessageType('GetAllExecutionEnvironmentsResponse', (_message.Message,), {

  'ExeEnvsEntry' : _reflection.GeneratedProtocolMessageType('ExeEnvsEntry', (_message.Message,), {
    'DESCRIPTOR' : _GETALLEXECUTIONENVIRONMENTSRESPONSE_EXEENVSENTRY,
    '__module__' : 'protos.metadata_service_pb2'
    # @@protoc_insertion_point(class_scope:protos.metadata_service.GetAllExecutionEnvironmentsResponse.ExeEnvsEntry)
    })
  ,
  'DESCRIPTOR' : _GETALLEXECUTIONENVIRONMENTSRESPONSE,
  '__module__' : 'protos.metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:protos.metadata_service.GetAllExecutionEnvironmentsResponse)
  })
_sym_db.RegisterMessage(GetAllExecutionEnvironmentsResponse)
_sym_db.RegisterMessage(GetAllExecutionEnvironmentsResponse.ExeEnvsEntry)

GetDataclayIDResponse = _reflection.GeneratedProtocolMessageType('GetDataclayIDResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETDATACLAYIDRESPONSE,
  '__module__' : 'protos.metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:protos.metadata_service.GetDataclayIDResponse)
  })
_sym_db.RegisterMessage(GetDataclayIDResponse)

AutoRegisterEERequest = _reflection.GeneratedProtocolMessageType('AutoRegisterEERequest', (_message.Message,), {
  'DESCRIPTOR' : _AUTOREGISTEREEREQUEST,
  '__module__' : 'protos.metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:protos.metadata_service.AutoRegisterEERequest)
  })
_sym_db.RegisterMessage(AutoRegisterEERequest)

_METADATASERVICE = DESCRIPTOR.services_by_name['MetadataService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GETALLEXECUTIONENVIRONMENTSRESPONSE_EXEENVSENTRY._options = None
  _GETALLEXECUTIONENVIRONMENTSRESPONSE_EXEENVSENTRY._serialized_options = b'8\001'
  _NEWACCOUNTREQUEST._serialized_start=117
  _NEWACCOUNTREQUEST._serialized_end=172
  _GETACCOUNTREQUEST._serialized_start=174
  _GETACCOUNTREQUEST._serialized_end=211
  _GETACCOUNTRESPONSE._serialized_start=213
  _GETACCOUNTRESPONSE._serialized_end=233
  _NEWSESSIONREQUEST._serialized_start=235
  _NEWSESSIONREQUEST._serialized_end=315
  _NEWSESSIONRESPONSE._serialized_start=317
  _NEWSESSIONRESPONSE._serialized_end=349
  _CLOSESESSIONREQUEST._serialized_start=351
  _CLOSESESSIONREQUEST._serialized_end=384
  _NEWDATASETREQUEST._serialized_start=386
  _NEWDATASETREQUEST._serialized_end=458
  _GETALLEXECUTIONENVIRONMENTSREQUEST._serialized_start=460
  _GETALLEXECUTIONENVIRONMENTSREQUEST._serialized_end=580
  _GETALLEXECUTIONENVIRONMENTSRESPONSE._serialized_start=583
  _GETALLEXECUTIONENVIRONMENTSRESPONSE._serialized_end=798
  _GETALLEXECUTIONENVIRONMENTSRESPONSE_EXEENVSENTRY._serialized_start=715
  _GETALLEXECUTIONENVIRONMENTSRESPONSE_EXEENVSENTRY._serialized_end=798
  _GETDATACLAYIDRESPONSE._serialized_start=800
  _GETDATACLAYIDRESPONSE._serialized_end=844
  _AUTOREGISTEREEREQUEST._serialized_start=846
  _AUTOREGISTEREEREQUEST._serialized_end=963
  _METADATASERVICE._serialized_start=966
  _METADATASERVICE._serialized_end=1789
# @@protoc_insertion_point(module_scope)
