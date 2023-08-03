import eth_pb2 as _eth_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BlockFilter(_message.Message):
    __slots__ = ["producer"]
    PRODUCER_FIELD_NUMBER: _ClassVar[int]
    producer: str
    def __init__(self, producer: _Optional[str] = ...) -> None: ...

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

class TransactionResponse(_message.Message):
    __slots__ = ["hash", "timestamp"]
    HASH_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    hash: str
    timestamp: int
    def __init__(self, hash: _Optional[str] = ..., timestamp: _Optional[int] = ...) -> None: ...

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

class TxSequenceResponse(_message.Message):
    __slots__ = ["sequence_response"]
    SEQUENCE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    sequence_response: _containers.RepeatedCompositeFieldContainer[TransactionResponse]
    def __init__(self, sequence_response: _Optional[_Iterable[_Union[TransactionResponse, _Mapping]]] = ...) -> None: ...
