# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: network_manager.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15network_manager.proto\"\x19\n\tInterface\x12\x0c\n\x04name\x18\x01 \x01(\t\"$\n\x11InterfaceResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\xb0\x01\n\x07Manager\x12\x35\n\x11turn_on_interface\x12\n.Interface\x1a\x12.InterfaceResponse\"\x00\x12\x36\n\x12turn_off_interface\x12\n.Interface\x1a\x12.InterfaceResponse\"\x00\x12\x36\n\x12show_one_interface\x12\n.Interface\x1a\x12.InterfaceResponse\"\x00\x62\x06proto3')



_INTERFACE = DESCRIPTOR.message_types_by_name['Interface']
_INTERFACERESPONSE = DESCRIPTOR.message_types_by_name['InterfaceResponse']
Interface = _reflection.GeneratedProtocolMessageType('Interface', (_message.Message,), {
  'DESCRIPTOR' : _INTERFACE,
  '__module__' : 'network_manager_pb2'
  # @@protoc_insertion_point(class_scope:Interface)
  })
_sym_db.RegisterMessage(Interface)

InterfaceResponse = _reflection.GeneratedProtocolMessageType('InterfaceResponse', (_message.Message,), {
  'DESCRIPTOR' : _INTERFACERESPONSE,
  '__module__' : 'network_manager_pb2'
  # @@protoc_insertion_point(class_scope:InterfaceResponse)
  })
_sym_db.RegisterMessage(InterfaceResponse)

_MANAGER = DESCRIPTOR.services_by_name['Manager']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _INTERFACE._serialized_start=25
  _INTERFACE._serialized_end=50
  _INTERFACERESPONSE._serialized_start=52
  _INTERFACERESPONSE._serialized_end=88
  _MANAGER._serialized_start=91
  _MANAGER._serialized_end=267
# @@protoc_insertion_point(module_scope)
