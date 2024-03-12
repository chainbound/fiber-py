import eth_pb2 as _eth_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BeaconBlockMsg(_message.Message):
    __slots__ = ["data_version", "ssz_block"]
    DATA_VERSION_FIELD_NUMBER: _ClassVar[int]
    SSZ_BLOCK_FIELD_NUMBER: _ClassVar[int]
    data_version: int
    ssz_block: bytes
    def __init__(self, data_version: _Optional[int] = ..., ssz_block: _Optional[bytes] = ...) -> None: ...

class BlockFilter(_message.Message):
    __slots__ = ["producer"]
    PRODUCER_FIELD_NUMBER: _ClassVar[int]
    producer: str
    def __init__(self, producer: _Optional[str] = ...) -> None: ...

class BlockSubmissionMsg(_message.Message):
    __slots__ = ["ssz_block"]
    SSZ_BLOCK_FIELD_NUMBER: _ClassVar[int]
    ssz_block: bytes
    def __init__(self, ssz_block: _Optional[bytes] = ...) -> None: ...

class BlockSubmissionResponse(_message.Message):
    __slots__ = ["slot", "state_root", "timestamp"]
    SLOT_FIELD_NUMBER: _ClassVar[int]
    STATE_ROOT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    slot: int
    state_root: bytes
    timestamp: int
    def __init__(self, slot: _Optional[int] = ..., state_root: _Optional[bytes] = ..., timestamp: _Optional[int] = ...) -> None: ...

class ExecutionPayloadMsg(_message.Message):
    __slots__ = ["data_version", "ssz_payload"]
    DATA_VERSION_FIELD_NUMBER: _ClassVar[int]
    SSZ_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    data_version: int
    ssz_payload: bytes
    def __init__(self, data_version: _Optional[int] = ..., ssz_payload: _Optional[bytes] = ...) -> None: ...

class RawTxMsg(_message.Message):
    __slots__ = ["rawTx"]
    RAWTX_FIELD_NUMBER: _ClassVar[int]
    rawTx: bytes
    def __init__(self, rawTx: _Optional[bytes] = ...) -> None: ...

class RawTxSequenceMsg(_message.Message):
    __slots__ = ["raw_txs"]
    RAW_TXS_FIELD_NUMBER: _ClassVar[int]
    raw_txs: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, raw_txs: _Optional[_Iterable[bytes]] = ...) -> None: ...

class TransactionMsg(_message.Message):
    __slots__ = ["rlp_transaction"]
    RLP_TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    rlp_transaction: bytes
    def __init__(self, rlp_transaction: _Optional[bytes] = ...) -> None: ...

class TransactionResponse(_message.Message):
    __slots__ = ["hash", "timestamp"]
    HASH_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    hash: str
    timestamp: int
    def __init__(self, hash: _Optional[str] = ..., timestamp: _Optional[int] = ...) -> None: ...

class TransactionWithSenderMsg(_message.Message):
    __slots__ = ["rlp_transaction", "sender"]
    RLP_TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    rlp_transaction: bytes
    sender: bytes
    def __init__(self, rlp_transaction: _Optional[bytes] = ..., sender: _Optional[bytes] = ...) -> None: ...

class TxFilter(_message.Message):
    __slots__ = ["encoded"]
    ENCODED_FIELD_NUMBER: _ClassVar[int]
    encoded: bytes
    def __init__(self, encoded: _Optional[bytes] = ...) -> None: ...

class TxSequenceMsg(_message.Message):
    __slots__ = ["sequence"]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    sequence: _containers.RepeatedCompositeFieldContainer[_eth_pb2.Transaction]
    def __init__(self, sequence: _Optional[_Iterable[_Union[_eth_pb2.Transaction, _Mapping]]] = ...) -> None: ...

class TxSequenceMsgV2(_message.Message):
    __slots__ = ["sequence"]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    sequence: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, sequence: _Optional[_Iterable[bytes]] = ...) -> None: ...

class TxSequenceResponse(_message.Message):
    __slots__ = ["sequence_response"]
    SEQUENCE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    sequence_response: _containers.RepeatedCompositeFieldContainer[TransactionResponse]
    def __init__(self, sequence_response: _Optional[_Iterable[_Union[TransactionResponse, _Mapping]]] = ...) -> None: ...
