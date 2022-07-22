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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15network_manager.proto\"\x19\n\tInterface\x12\x0c\n\x04name\x18\x01 \x01(\t\"$\n\x11InterfaceResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x0e\n\x0c\x45mptyRequest\"!\n\x0e\x43onfigResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"_\n\x0cStaticConfig\x12\x11\n\tinterface\x18\x01 \x01(\t\x12\x14\n\x0cipv4_address\x18\x02 \x01(\t\x12\x14\n\x0cipv4_gateway\x18\x03 \x01(\t\x12\x10\n\x08ipv4_dns\x18\x04 \x01(\t\"D\n\x0bRouteConfig\x12\x13\n\x0b\x64\x65stination\x18\x01 \x01(\t\x12\r\n\x05route\x18\x02 \x01(\t\x12\x11\n\tinterface\x18\x03 \x01(\t2\xd1\x03\n\x07Manager\x12\x35\n\x11turn_on_interface\x12\n.Interface\x1a\x12.InterfaceResponse\"\x00\x12\x36\n\x12turn_off_interface\x12\n.Interface\x1a\x12.InterfaceResponse\"\x00\x12\x36\n\x12show_one_interface\x12\n.Interface\x1a\x12.InterfaceResponse\"\x00\x12:\n\x13show_all_interfaces\x12\r.EmptyRequest\x1a\x12.InterfaceResponse\"\x00\x12\x36\n\x0flist_interfaces\x12\r.EmptyRequest\x1a\x12.InterfaceResponse\"\x00\x12\x37\n\x16set_configuration_dhcp\x12\n.Interface\x1a\x0f.ConfigResponse\"\x00\x12<\n\x18set_configuration_static\x12\r.StaticConfig\x1a\x0f.ConfigResponse\"\x00\x12\x34\n\x11\x61\x64\x64_network_route\x12\x0c.RouteConfig\x1a\x0f.ConfigResponse\"\x00\x62\x06proto3')



_INTERFACE = DESCRIPTOR.message_types_by_name['Interface']
_INTERFACERESPONSE = DESCRIPTOR.message_types_by_name['InterfaceResponse']
_EMPTYREQUEST = DESCRIPTOR.message_types_by_name['EmptyRequest']
_CONFIGRESPONSE = DESCRIPTOR.message_types_by_name['ConfigResponse']
_STATICCONFIG = DESCRIPTOR.message_types_by_name['StaticConfig']
_ROUTECONFIG = DESCRIPTOR.message_types_by_name['RouteConfig']
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

EmptyRequest = _reflection.GeneratedProtocolMessageType('EmptyRequest', (_message.Message,), {
  'DESCRIPTOR' : _EMPTYREQUEST,
  '__module__' : 'network_manager_pb2'
  # @@protoc_insertion_point(class_scope:EmptyRequest)
  })
_sym_db.RegisterMessage(EmptyRequest)

ConfigResponse = _reflection.GeneratedProtocolMessageType('ConfigResponse', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGRESPONSE,
  '__module__' : 'network_manager_pb2'
  # @@protoc_insertion_point(class_scope:ConfigResponse)
  })
_sym_db.RegisterMessage(ConfigResponse)

StaticConfig = _reflection.GeneratedProtocolMessageType('StaticConfig', (_message.Message,), {
  'DESCRIPTOR' : _STATICCONFIG,
  '__module__' : 'network_manager_pb2'
  # @@protoc_insertion_point(class_scope:StaticConfig)
  })
_sym_db.RegisterMessage(StaticConfig)

RouteConfig = _reflection.GeneratedProtocolMessageType('RouteConfig', (_message.Message,), {
  'DESCRIPTOR' : _ROUTECONFIG,
  '__module__' : 'network_manager_pb2'
  # @@protoc_insertion_point(class_scope:RouteConfig)
  })
_sym_db.RegisterMessage(RouteConfig)

_MANAGER = DESCRIPTOR.services_by_name['Manager']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _INTERFACE._serialized_start=25
  _INTERFACE._serialized_end=50
  _INTERFACERESPONSE._serialized_start=52
  _INTERFACERESPONSE._serialized_end=88
  _EMPTYREQUEST._serialized_start=90
  _EMPTYREQUEST._serialized_end=104
  _CONFIGRESPONSE._serialized_start=106
  _CONFIGRESPONSE._serialized_end=139
  _STATICCONFIG._serialized_start=141
  _STATICCONFIG._serialized_end=236
  _ROUTECONFIG._serialized_start=238
  _ROUTECONFIG._serialized_end=306
  _MANAGER._serialized_start=309
  _MANAGER._serialized_end=774
# @@protoc_insertion_point(module_scope)
