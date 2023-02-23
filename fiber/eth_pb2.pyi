from google.protobuf import empty_pb2 as _empty_pb2
import types_pb2 as _types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AccessListItem(_message.Message):
    __slots__ = ["address", "slots"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SLOTS_FIELD_NUMBER: _ClassVar[int]
    address: _types_pb2.H160
    slots: _containers.RepeatedCompositeFieldContainer[_types_pb2.H256]
    def __init__(self, address: _Optional[_Union[_types_pb2.H160, _Mapping]] = ..., slots: _Optional[_Iterable[_Union[_types_pb2.H256, _Mapping]]] = ...) -> None: ...

class AccessTuple(_message.Message):
    __slots__ = ["address", "storage_keys"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_KEYS_FIELD_NUMBER: _ClassVar[int]
    address: bytes
    storage_keys: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, address: _Optional[bytes] = ..., storage_keys: _Optional[_Iterable[bytes]] = ...) -> None: ...

class Block(_message.Message):
    __slots__ = ["base_fee_per_gas", "extra_data", "fee_recipient", "gas_limit", "gas_used", "hash", "logs_bloom", "number", "parent_hash", "prev_randao", "receipt_root", "state_root", "timestamp", "transactions"]
    BASE_FEE_PER_GAS_FIELD_NUMBER: _ClassVar[int]
    EXTRA_DATA_FIELD_NUMBER: _ClassVar[int]
    FEE_RECIPIENT_FIELD_NUMBER: _ClassVar[int]
    GAS_LIMIT_FIELD_NUMBER: _ClassVar[int]
    GAS_USED_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    LOGS_BLOOM_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    PARENT_HASH_FIELD_NUMBER: _ClassVar[int]
    PREV_RANDAO_FIELD_NUMBER: _ClassVar[int]
    RECEIPT_ROOT_FIELD_NUMBER: _ClassVar[int]
    STATE_ROOT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    base_fee_per_gas: bytes
    extra_data: bytes
    fee_recipient: bytes
    gas_limit: int
    gas_used: int
    hash: bytes
    logs_bloom: bytes
    number: int
    parent_hash: bytes
    prev_randao: bytes
    receipt_root: bytes
    state_root: bytes
    timestamp: int
    transactions: _containers.RepeatedCompositeFieldContainer[Transaction]
    def __init__(self, number: _Optional[int] = ..., hash: _Optional[bytes] = ..., parent_hash: _Optional[bytes] = ..., prev_randao: _Optional[bytes] = ..., state_root: _Optional[bytes] = ..., receipt_root: _Optional[bytes] = ..., fee_recipient: _Optional[bytes] = ..., extra_data: _Optional[bytes] = ..., gas_limit: _Optional[int] = ..., gas_used: _Optional[int] = ..., timestamp: _Optional[int] = ..., logs_bloom: _Optional[bytes] = ..., base_fee_per_gas: _Optional[bytes] = ..., transactions: _Optional[_Iterable[_Union[Transaction, _Mapping]]] = ...) -> None: ...

class BlockId(_message.Message):
    __slots__ = ["hash", "number"]
    HASH_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    hash: _types_pb2.H256
    number: BlockNumber
    def __init__(self, hash: _Optional[_Union[_types_pb2.H256, _Mapping]] = ..., number: _Optional[_Union[BlockNumber, _Mapping]] = ...) -> None: ...

class BlockNumber(_message.Message):
    __slots__ = ["latest", "number", "pending"]
    LATEST_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    PENDING_FIELD_NUMBER: _ClassVar[int]
    latest: _empty_pb2.Empty
    number: int
    pending: _empty_pb2.Empty
    def __init__(self, latest: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., pending: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., number: _Optional[int] = ...) -> None: ...

class CanonicalTransactionData(_message.Message):
    __slots__ = ["block_hash", "block_number", "index"]
    BLOCK_HASH_FIELD_NUMBER: _ClassVar[int]
    BLOCK_NUMBER_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    block_hash: _types_pb2.H256
    block_number: int
    index: int
    def __init__(self, block_hash: _Optional[_Union[_types_pb2.H256, _Mapping]] = ..., block_number: _Optional[int] = ..., index: _Optional[int] = ...) -> None: ...

class Transaction(_message.Message):
    __slots__ = ["access_list", "chainId", "gas", "gas_price", "hash", "input", "max_fee", "nonce", "priority_fee", "r", "s", "to", "type", "v", "value"]
    ACCESS_LIST_FIELD_NUMBER: _ClassVar[int]
    CHAINID_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    GAS_FIELD_NUMBER: _ClassVar[int]
    GAS_PRICE_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    MAX_FEE_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FEE_FIELD_NUMBER: _ClassVar[int]
    R_FIELD_NUMBER: _ClassVar[int]
    S_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    V_FIELD_NUMBER: _ClassVar[int]
    access_list: _containers.RepeatedCompositeFieldContainer[AccessTuple]
    chainId: int
    gas: int
    gas_price: int
    hash: bytes
    input: bytes
    max_fee: int
    nonce: int
    priority_fee: int
    r: bytes
    s: bytes
    to: bytes
    type: int
    v: int
    value: bytes
    def __init__(self, to: _Optional[bytes] = ..., gas: _Optional[int] = ..., gas_price: _Optional[int] = ..., hash: _Optional[bytes] = ..., input: _Optional[bytes] = ..., nonce: _Optional[int] = ..., value: _Optional[bytes] = ..., type: _Optional[int] = ..., max_fee: _Optional[int] = ..., priority_fee: _Optional[int] = ..., v: _Optional[int] = ..., r: _Optional[bytes] = ..., s: _Optional[bytes] = ..., chainId: _Optional[int] = ..., access_list: _Optional[_Iterable[_Union[AccessTuple, _Mapping]]] = ..., **kwargs) -> None: ...
