# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SuperStream.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='SuperStream.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11SuperStream.proto\"\x1d\n\rClientMessage\x12\x0c\n\x04text\x18\x01 \x01(\t\"\x1b\n\x0bServerReply\x12\x0c\n\x04text\x18\x01 \x01(\t2>\n\x0bSuperStream\x12/\n\tgetAnswer\x12\x0e.ClientMessage\x1a\x0c.ServerReply\"\x00(\x01\x30\x01\x62\x06proto3'
)




_CLIENTMESSAGE = _descriptor.Descriptor(
  name='ClientMessage',
  full_name='ClientMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='ClientMessage.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=21,
  serialized_end=50,
)


_SERVERREPLY = _descriptor.Descriptor(
  name='ServerReply',
  full_name='ServerReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='ServerReply.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=52,
  serialized_end=79,
)

DESCRIPTOR.message_types_by_name['ClientMessage'] = _CLIENTMESSAGE
DESCRIPTOR.message_types_by_name['ServerReply'] = _SERVERREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientMessage = _reflection.GeneratedProtocolMessageType('ClientMessage', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTMESSAGE,
  '__module__' : 'SuperStream_pb2'
  # @@protoc_insertion_point(class_scope:ClientMessage)
  })
_sym_db.RegisterMessage(ClientMessage)

ServerReply = _reflection.GeneratedProtocolMessageType('ServerReply', (_message.Message,), {
  'DESCRIPTOR' : _SERVERREPLY,
  '__module__' : 'SuperStream_pb2'
  # @@protoc_insertion_point(class_scope:ServerReply)
  })
_sym_db.RegisterMessage(ServerReply)



_SUPERSTREAM = _descriptor.ServiceDescriptor(
  name='SuperStream',
  full_name='SuperStream',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=81,
  serialized_end=143,
  methods=[
  _descriptor.MethodDescriptor(
    name='getAnswer',
    full_name='SuperStream.getAnswer',
    index=0,
    containing_service=None,
    input_type=_CLIENTMESSAGE,
    output_type=_SERVERREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SUPERSTREAM)

DESCRIPTOR.services_by_name['SuperStream'] = _SUPERSTREAM

# @@protoc_insertion_point(module_scope)
