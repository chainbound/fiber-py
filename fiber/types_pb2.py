# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: types.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0btypes.proto\x12\x05types\"\x1e\n\x04H128\x12\n\n\x02hi\x18\x01 \x01(\x04\x12\n\n\x02lo\x18\x02 \x01(\x04\"+\n\x04H160\x12\x17\n\x02hi\x18\x01 \x01(\x0b\x32\x0b.types.H128\x12\n\n\x02lo\x18\x02 \x01(\r\"8\n\x04H256\x12\x17\n\x02hi\x18\x01 \x01(\x0b\x32\x0b.types.H128\x12\x17\n\x02lo\x18\x02 \x01(\x0b\x32\x0b.types.H128\"8\n\x04H512\x12\x17\n\x02hi\x18\x01 \x01(\x0b\x32\x0b.types.H256\x12\x17\n\x02lo\x18\x02 \x01(\x0b\x32\x0b.types.H256\"9\n\x05H1024\x12\x17\n\x02hi\x18\x01 \x01(\x0b\x32\x0b.types.H512\x12\x17\n\x02lo\x18\x02 \x01(\x0b\x32\x0b.types.H512\";\n\x05H2048\x12\x18\n\x02hi\x18\x01 \x01(\x0b\x32\x0c.types.H1024\x12\x18\n\x02lo\x18\x02 \x01(\x0b\x32\x0c.types.H1024\";\n\x0cVersionReply\x12\r\n\x05major\x18\x01 \x01(\r\x12\r\n\x05minor\x18\x02 \x01(\r\x12\r\n\x05patch\x18\x03 \x01(\r\"\x8e\x03\n\x10\x45xecutionPayload\x12\x1f\n\nparentHash\x18\x01 \x01(\x0b\x32\x0b.types.H256\x12\x1d\n\x08\x63oinbase\x18\x02 \x01(\x0b\x32\x0b.types.H160\x12\x1e\n\tstateRoot\x18\x03 \x01(\x0b\x32\x0b.types.H256\x12 \n\x0breceiptRoot\x18\x04 \x01(\x0b\x32\x0b.types.H256\x12\x1f\n\tlogsBloom\x18\x05 \x01(\x0b\x32\x0c.types.H2048\x12\x1f\n\nprevRandao\x18\x06 \x01(\x0b\x32\x0b.types.H256\x12\x13\n\x0b\x62lockNumber\x18\x07 \x01(\x04\x12\x10\n\x08gasLimit\x18\x08 \x01(\x04\x12\x0f\n\x07gasUsed\x18\t \x01(\x04\x12\x11\n\ttimestamp\x18\n \x01(\x04\x12\x11\n\textraData\x18\x0b \x01(\x0c\x12\"\n\rbaseFeePerGas\x18\x0c \x01(\x0b\x32\x0b.types.H256\x12\x1e\n\tblockHash\x18\r \x01(\x0b\x32\x0b.types.H256\x12\x14\n\x0ctransactions\x18\x0e \x03(\x0c\"4\n\rNodeInfoPorts\x12\x11\n\tdiscovery\x18\x01 \x01(\r\x12\x10\n\x08listener\x18\x02 \x01(\r\"\x93\x01\n\rNodeInfoReply\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x65node\x18\x03 \x01(\t\x12\x0b\n\x03\x65nr\x18\x04 \x01(\t\x12#\n\x05ports\x18\x05 \x01(\x0b\x32\x14.types.NodeInfoPorts\x12\x14\n\x0clistenerAddr\x18\x06 \x01(\t\x12\x11\n\tprotocols\x18\x07 \x01(\x0c\"\xc1\x01\n\x08PeerInfo\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x65node\x18\x03 \x01(\t\x12\x0b\n\x03\x65nr\x18\x04 \x01(\t\x12\x0c\n\x04\x63\x61ps\x18\x05 \x03(\t\x12\x15\n\rconnLocalAddr\x18\x06 \x01(\t\x12\x16\n\x0e\x63onnRemoteAddr\x18\x07 \x01(\t\x12\x15\n\rconnIsInbound\x18\x08 \x01(\x08\x12\x15\n\rconnIsTrusted\x18\t \x01(\x08\x12\x14\n\x0c\x63onnIsStatic\x18\n \x01(\x08\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'types_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _H128._serialized_start=22
  _H128._serialized_end=52
  _H160._serialized_start=54
  _H160._serialized_end=97
  _H256._serialized_start=99
  _H256._serialized_end=155
  _H512._serialized_start=157
  _H512._serialized_end=213
  _H1024._serialized_start=215
  _H1024._serialized_end=272
  _H2048._serialized_start=274
  _H2048._serialized_end=333
  _VERSIONREPLY._serialized_start=335
  _VERSIONREPLY._serialized_end=394
  _EXECUTIONPAYLOAD._serialized_start=397
  _EXECUTIONPAYLOAD._serialized_end=795
  _NODEINFOPORTS._serialized_start=797
  _NODEINFOPORTS._serialized_end=849
  _NODEINFOREPLY._serialized_start=852
  _NODEINFOREPLY._serialized_end=999
  _PEERINFO._serialized_start=1002
  _PEERINFO._serialized_end=1195
# @@protoc_insertion_point(module_scope)
