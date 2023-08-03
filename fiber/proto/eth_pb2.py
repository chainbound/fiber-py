# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: eth.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import types_pb2 as types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\teth.proto\x12\x03\x65th\x1a\x1bgoogle/protobuf/empty.proto\x1a\x0btypes.proto\"\x84\x01\n\x0b\x42lockNumber\x12(\n\x06latest\x18\x01 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00\x12)\n\x07pending\x18\x02 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00\x12\x10\n\x06number\x18\x03 \x01(\x04H\x00\x42\x0e\n\x0c\x62lock_number\"P\n\x07\x42lockId\x12\x1b\n\x04hash\x18\x01 \x01(\x0b\x32\x0b.types.H256H\x00\x12\"\n\x06number\x18\x02 \x01(\x0b\x32\x10.eth.BlockNumberH\x00\x42\x04\n\x02id\"`\n\x18\x43\x61nonicalTransactionData\x12\x1f\n\nblock_hash\x18\x01 \x01(\x0b\x32\x0b.types.H256\x12\x14\n\x0c\x62lock_number\x18\x02 \x01(\x04\x12\r\n\x05index\x18\x03 \x01(\x04\"J\n\x0e\x41\x63\x63\x65ssListItem\x12\x1c\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32\x0b.types.H160\x12\x1a\n\x05slots\x18\x02 \x03(\x0b\x32\x0b.types.H256\"\xaa\x02\n\x0bTransaction\x12\x0f\n\x02to\x18\x01 \x01(\x0cH\x00\x88\x01\x01\x12\x0b\n\x03gas\x18\x02 \x01(\x04\x12\x11\n\tgas_price\x18\x03 \x01(\x04\x12\x0c\n\x04hash\x18\x04 \x01(\x0c\x12\r\n\x05input\x18\x05 \x01(\x0c\x12\r\n\x05nonce\x18\x06 \x01(\x04\x12\r\n\x05value\x18\x07 \x01(\x0c\x12\x11\n\x04\x66rom\x18\x08 \x01(\x0cH\x01\x88\x01\x01\x12\x0c\n\x04type\x18\t \x01(\r\x12\x0f\n\x07max_fee\x18\n \x01(\x04\x12\x14\n\x0cpriority_fee\x18\x0b \x01(\x04\x12\t\n\x01v\x18\x0c \x01(\x04\x12\t\n\x01r\x18\r \x01(\x0c\x12\t\n\x01s\x18\x0e \x01(\x0c\x12\x0f\n\x07\x63hainId\x18\x0f \x01(\r\x12%\n\x0b\x61\x63\x63\x65ss_list\x18\x10 \x03(\x0b\x32\x10.eth.AccessTupleB\x05\n\x03_toB\x07\n\x05_from\"4\n\x0b\x41\x63\x63\x65ssTuple\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x12\x14\n\x0cstorage_keys\x18\x02 \x03(\x0c\"g\n\x10\x45xecutionPayload\x12+\n\x06header\x18\x01 \x01(\x0b\x32\x1b.eth.ExecutionPayloadHeader\x12&\n\x0ctransactions\x18\x02 \x03(\x0b\x32\x10.eth.Transaction\"\xf7\x02\n\x16\x45xecutionPayloadHeader\x12\x13\n\x0bparent_hash\x18\x01 \x01(\x0c\x12\x15\n\rfee_recipient\x18\x02 \x01(\x0c\x12\x12\n\nstate_root\x18\x03 \x01(\x0c\x12\x15\n\rreceipts_root\x18\x04 \x01(\x0c\x12\x12\n\nlogs_bloom\x18\x05 \x01(\x0c\x12\x13\n\x0bprev_randao\x18\x06 \x01(\x0c\x12\x14\n\x0c\x62lock_number\x18\x07 \x01(\x04\x12\x11\n\tgas_limit\x18\x08 \x01(\x04\x12\x10\n\x08gas_used\x18\t \x01(\x04\x12\x11\n\ttimestamp\x18\n \x01(\x04\x12\x12\n\nextra_data\x18\x0b \x01(\x0c\x12\x18\n\x10\x62\x61se_fee_per_gas\x18\x0c \x01(\x0c\x12\x12\n\nblock_hash\x18\r \x01(\x0c\x12\x19\n\x11transactions_root\x18\x0e \x01(\x0c\x12\x1d\n\x10withdrawals_root\x18\x0f \x01(\x0cH\x00\x88\x01\x01\x42\x13\n\x11_withdrawals_root\"\x80\x01\n\x0b\x42\x65\x61\x63onBlock\x12\x0c\n\x04slot\x18\x01 \x01(\x04\x12\x16\n\x0eproposer_index\x18\x02 \x01(\x04\x12\x13\n\x0bparent_root\x18\x03 \x01(\x0c\x12\x12\n\nstate_root\x18\x04 \x01(\x0c\x12\"\n\x04\x62ody\x18\x05 \x01(\x0b\x32\x14.eth.BeaconBlockBody\"\x8e\x01\n\x12\x43ompactBeaconBlock\x12\x0c\n\x04slot\x18\x01 \x01(\x04\x12\x16\n\x0eproposer_index\x18\x02 \x01(\x04\x12\x13\n\x0bparent_root\x18\x03 \x01(\x0c\x12\x12\n\nstate_root\x18\x04 \x01(\x0c\x12)\n\x04\x62ody\x18\x05 \x01(\x0b\x32\x1b.eth.CompactBeaconBlockBody\"I\n\x11SignedBeaconBlock\x12!\n\x07message\x18\x01 \x01(\x0b\x32\x10.eth.BeaconBlock\x12\x11\n\tsignature\x18\x02 \x01(\x0c\"\xde\x03\n\x0f\x42\x65\x61\x63onBlockBody\x12\x15\n\rrandao_reveal\x18\x01 \x01(\x0c\x12 \n\teth1_data\x18\x02 \x01(\x0b\x32\r.eth.Eth1Data\x12\x10\n\x08graffiti\x18\x03 \x01(\x0c\x12\x31\n\x12proposer_slashings\x18\x04 \x03(\x0b\x32\x15.eth.ProposerSlashing\x12\x31\n\x12\x61ttester_slashings\x18\x05 \x03(\x0b\x32\x15.eth.AttesterSlashing\x12&\n\x0c\x61ttestations\x18\x06 \x03(\x0b\x32\x10.eth.Attestation\x12\x1e\n\x08\x64\x65posits\x18\x07 \x03(\x0b\x32\x0c.eth.Deposit\x12\x31\n\x0fvoluntary_exits\x18\x08 \x03(\x0b\x32\x18.eth.SignedVoluntaryExit\x12*\n\x0esync_aggregate\x18\t \x01(\x0b\x32\x12.eth.SyncAggregate\x12\x30\n\x11\x65xecution_payload\x18\n \x01(\x0b\x32\x15.eth.ExecutionPayload\x12\x41\n\x18\x62ls_to_execution_changes\x18\x0b \x03(\x0b\x32\x1f.eth.SignedBLSToExecutionChange\"\xb3\x03\n\x16\x43ompactBeaconBlockBody\x12\x15\n\rrandao_reveal\x18\x01 \x01(\x0c\x12 \n\teth1_data\x18\x02 \x01(\x0b\x32\r.eth.Eth1Data\x12\x10\n\x08graffiti\x18\x03 \x01(\x0c\x12\x31\n\x12proposer_slashings\x18\x04 \x03(\x0b\x32\x15.eth.ProposerSlashing\x12\x31\n\x12\x61ttester_slashings\x18\x05 \x03(\x0b\x32\x15.eth.AttesterSlashing\x12&\n\x0c\x61ttestations\x18\x06 \x03(\x0b\x32\x10.eth.Attestation\x12\x1e\n\x08\x64\x65posits\x18\x07 \x03(\x0b\x32\x0c.eth.Deposit\x12\x31\n\x0fvoluntary_exits\x18\x08 \x03(\x0b\x32\x18.eth.SignedVoluntaryExit\x12*\n\x0esync_aggregate\x18\t \x01(\x0b\x32\x12.eth.SyncAggregate\x12\x41\n\x18\x62ls_to_execution_changes\x18\n \x03(\x0b\x32\x1f.eth.SignedBLSToExecutionChange\"U\n\x17SignedBeaconBlockHeader\x12\'\n\x07message\x18\x01 \x01(\x0b\x32\x16.eth.BeaconBlockHeader\x12\x11\n\tsignature\x18\x02 \x01(\x0c\"u\n\x11\x42\x65\x61\x63onBlockHeader\x12\x0c\n\x04slot\x18\x01 \x01(\x04\x12\x16\n\x0eproposer_index\x18\x02 \x01(\x04\x12\x13\n\x0bparent_root\x18\x03 \x01(\x0c\x12\x12\n\nstate_root\x18\x04 \x01(\x0c\x12\x11\n\tbody_root\x18\x05 \x01(\x0c\"K\n\x08\x45th1Data\x12\x14\n\x0c\x64\x65posit_root\x18\x01 \x01(\x0c\x12\x15\n\rdeposit_count\x18\x02 \x01(\x04\x12\x12\n\nblock_hash\x18\x03 \x01(\x0c\"M\n\x13SignedVoluntaryExit\x12#\n\x07message\x18\x01 \x01(\x0b\x32\x12.eth.VoluntaryExit\x12\x11\n\tsignature\x18\x02 \x01(\x0c\"7\n\rVoluntaryExit\x12\r\n\x05\x65poch\x18\x01 \x01(\x04\x12\x17\n\x0fvalidator_index\x18\x02 \x01(\x04\"r\n\x10ProposerSlashing\x12.\n\x08header_1\x18\x01 \x01(\x0b\x32\x1c.eth.SignedBeaconBlockHeader\x12.\n\x08header_2\x18\x02 \x01(\x0b\x32\x1c.eth.SignedBeaconBlockHeader\"r\n\x10\x41ttesterSlashing\x12.\n\rattestation_1\x18\x01 \x01(\x0b\x32\x17.eth.IndexedAttestation\x12.\n\rattestation_2\x18\x02 \x01(\x0b\x32\x17.eth.IndexedAttestation\"f\n\x12IndexedAttestation\x12\x19\n\x11\x61ttesting_indices\x18\x01 \x03(\x04\x12\"\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x14.eth.AttestationData\x12\x11\n\tsignature\x18\x03 \x01(\x0c\"\x8b\x01\n\x0f\x41ttestationData\x12\x0c\n\x04slot\x18\x01 \x01(\x04\x12\r\n\x05index\x18\x02 \x01(\x04\x12\x19\n\x11\x62\x65\x61\x63on_block_root\x18\x03 \x01(\x0c\x12\x1f\n\x06source\x18\x04 \x01(\x0b\x32\x0f.eth.Checkpoint\x12\x1f\n\x06target\x18\x05 \x01(\x0b\x32\x0f.eth.Checkpoint\")\n\nCheckpoint\x12\r\n\x05\x65poch\x18\x01 \x01(\x04\x12\x0c\n\x04root\x18\x02 \x01(\x0c\"^\n\x0b\x41ttestation\x12\x18\n\x10\x61ggregation_bits\x18\x01 \x01(\x0c\x12\"\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x14.eth.AttestationData\x12\x11\n\tsignature\x18\x03 \x01(\x0c\"8\n\x07\x44\x65posit\x12\r\n\x05proof\x18\x01 \x03(\x0c\x12\x1e\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x10.eth.DepositData\"`\n\x0b\x44\x65positData\x12\x0e\n\x06pubkey\x18\x01 \x01(\x0c\x12\x1e\n\x16withdrawal_credentials\x18\x02 \x01(\x0c\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x04\x12\x11\n\tsignature\x18\x04 \x01(\x0c\"N\n\rSyncAggregate\x12\x1b\n\x13sync_committee_bits\x18\x01 \x01(\x0c\x12 \n\x18sync_committee_signature\x18\x02 \x01(\x0c\"[\n\x1aSignedBLSToExecutionChange\x12*\n\x07message\x18\x01 \x01(\x0b\x32\x19.eth.BLSToExecutionChange\x12\x11\n\tsignature\x18\x02 \x01(\x0c\"f\n\x14\x42LSToExecutionChange\x12\x17\n\x0fvalidator_index\x18\x01 \x01(\x04\x12\x17\n\x0f\x66rom_bls_pubkey\x18\x02 \x01(\x0c\x12\x1c\n\x14to_execution_address\x18\x03 \x01(\x0c\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eth_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BLOCKNUMBER._serialized_start=61
  _BLOCKNUMBER._serialized_end=193
  _BLOCKID._serialized_start=195
  _BLOCKID._serialized_end=275
  _CANONICALTRANSACTIONDATA._serialized_start=277
  _CANONICALTRANSACTIONDATA._serialized_end=373
  _ACCESSLISTITEM._serialized_start=375
  _ACCESSLISTITEM._serialized_end=449
  _TRANSACTION._serialized_start=452
  _TRANSACTION._serialized_end=750
  _ACCESSTUPLE._serialized_start=752
  _ACCESSTUPLE._serialized_end=804
  _EXECUTIONPAYLOAD._serialized_start=806
  _EXECUTIONPAYLOAD._serialized_end=909
  _EXECUTIONPAYLOADHEADER._serialized_start=912
  _EXECUTIONPAYLOADHEADER._serialized_end=1287
  _BEACONBLOCK._serialized_start=1290
  _BEACONBLOCK._serialized_end=1418
  _COMPACTBEACONBLOCK._serialized_start=1421
  _COMPACTBEACONBLOCK._serialized_end=1563
  _SIGNEDBEACONBLOCK._serialized_start=1565
  _SIGNEDBEACONBLOCK._serialized_end=1638
  _BEACONBLOCKBODY._serialized_start=1641
  _BEACONBLOCKBODY._serialized_end=2119
  _COMPACTBEACONBLOCKBODY._serialized_start=2122
  _COMPACTBEACONBLOCKBODY._serialized_end=2557
  _SIGNEDBEACONBLOCKHEADER._serialized_start=2559
  _SIGNEDBEACONBLOCKHEADER._serialized_end=2644
  _BEACONBLOCKHEADER._serialized_start=2646
  _BEACONBLOCKHEADER._serialized_end=2763
  _ETH1DATA._serialized_start=2765
  _ETH1DATA._serialized_end=2840
  _SIGNEDVOLUNTARYEXIT._serialized_start=2842
  _SIGNEDVOLUNTARYEXIT._serialized_end=2919
  _VOLUNTARYEXIT._serialized_start=2921
  _VOLUNTARYEXIT._serialized_end=2976
  _PROPOSERSLASHING._serialized_start=2978
  _PROPOSERSLASHING._serialized_end=3092
  _ATTESTERSLASHING._serialized_start=3094
  _ATTESTERSLASHING._serialized_end=3208
  _INDEXEDATTESTATION._serialized_start=3210
  _INDEXEDATTESTATION._serialized_end=3312
  _ATTESTATIONDATA._serialized_start=3315
  _ATTESTATIONDATA._serialized_end=3454
  _CHECKPOINT._serialized_start=3456
  _CHECKPOINT._serialized_end=3497
  _ATTESTATION._serialized_start=3499
  _ATTESTATION._serialized_end=3593
  _DEPOSIT._serialized_start=3595
  _DEPOSIT._serialized_end=3651
  _DEPOSITDATA._serialized_start=3653
  _DEPOSITDATA._serialized_end=3749
  _SYNCAGGREGATE._serialized_start=3751
  _SYNCAGGREGATE._serialized_end=3829
  _SIGNEDBLSTOEXECUTIONCHANGE._serialized_start=3831
  _SIGNEDBLSTOEXECUTIONCHANGE._serialized_end=3922
  _BLSTOEXECUTIONCHANGE._serialized_start=3924
  _BLSTOEXECUTIONCHANGE._serialized_end=4026
# @@protoc_insertion_point(module_scope)