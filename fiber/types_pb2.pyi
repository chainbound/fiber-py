from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExecutionPayload(_message.Message):
    __slots__ = ["baseFeePerGas", "blockHash", "blockNumber", "coinbase", "extraData", "gasLimit", "gasUsed", "logsBloom", "parentHash", "prevRandao", "receiptRoot", "stateRoot", "timestamp", "transactions"]
    BASEFEEPERGAS_FIELD_NUMBER: _ClassVar[int]
    BLOCKHASH_FIELD_NUMBER: _ClassVar[int]
    BLOCKNUMBER_FIELD_NUMBER: _ClassVar[int]
    COINBASE_FIELD_NUMBER: _ClassVar[int]
    EXTRADATA_FIELD_NUMBER: _ClassVar[int]
    GASLIMIT_FIELD_NUMBER: _ClassVar[int]
    GASUSED_FIELD_NUMBER: _ClassVar[int]
    LOGSBLOOM_FIELD_NUMBER: _ClassVar[int]
    PARENTHASH_FIELD_NUMBER: _ClassVar[int]
    PREVRANDAO_FIELD_NUMBER: _ClassVar[int]
    RECEIPTROOT_FIELD_NUMBER: _ClassVar[int]
    STATEROOT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    baseFeePerGas: H256
    blockHash: H256
    blockNumber: int
    coinbase: H160
    extraData: bytes
    gasLimit: int
    gasUsed: int
    logsBloom: H2048
    parentHash: H256
    prevRandao: H256
    receiptRoot: H256
    stateRoot: H256
    timestamp: int
    transactions: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, parentHash: _Optional[_Union[H256, _Mapping]] = ..., coinbase: _Optional[_Union[H160, _Mapping]] = ..., stateRoot: _Optional[_Union[H256, _Mapping]] = ..., receiptRoot: _Optional[_Union[H256, _Mapping]] = ..., logsBloom: _Optional[_Union[H2048, _Mapping]] = ..., prevRandao: _Optional[_Union[H256, _Mapping]] = ..., blockNumber: _Optional[int] = ..., gasLimit: _Optional[int] = ..., gasUsed: _Optional[int] = ..., timestamp: _Optional[int] = ..., extraData: _Optional[bytes] = ..., baseFeePerGas: _Optional[_Union[H256, _Mapping]] = ..., blockHash: _Optional[_Union[H256, _Mapping]] = ..., transactions: _Optional[_Iterable[bytes]] = ...) -> None: ...

class H1024(_message.Message):
    __slots__ = ["hi", "lo"]
    HI_FIELD_NUMBER: _ClassVar[int]
    LO_FIELD_NUMBER: _ClassVar[int]
    hi: H512
    lo: H512
    def __init__(self, hi: _Optional[_Union[H512, _Mapping]] = ..., lo: _Optional[_Union[H512, _Mapping]] = ...) -> None: ...

class H128(_message.Message):
    __slots__ = ["hi", "lo"]
    HI_FIELD_NUMBER: _ClassVar[int]
    LO_FIELD_NUMBER: _ClassVar[int]
    hi: int
    lo: int
    def __init__(self, hi: _Optional[int] = ..., lo: _Optional[int] = ...) -> None: ...

class H160(_message.Message):
    __slots__ = ["hi", "lo"]
    HI_FIELD_NUMBER: _ClassVar[int]
    LO_FIELD_NUMBER: _ClassVar[int]
    hi: H128
    lo: int
    def __init__(self, hi: _Optional[_Union[H128, _Mapping]] = ..., lo: _Optional[int] = ...) -> None: ...

class H2048(_message.Message):
    __slots__ = ["hi", "lo"]
    HI_FIELD_NUMBER: _ClassVar[int]
    LO_FIELD_NUMBER: _ClassVar[int]
    hi: H1024
    lo: H1024
    def __init__(self, hi: _Optional[_Union[H1024, _Mapping]] = ..., lo: _Optional[_Union[H1024, _Mapping]] = ...) -> None: ...

class H256(_message.Message):
    __slots__ = ["hi", "lo"]
    HI_FIELD_NUMBER: _ClassVar[int]
    LO_FIELD_NUMBER: _ClassVar[int]
    hi: H128
    lo: H128
    def __init__(self, hi: _Optional[_Union[H128, _Mapping]] = ..., lo: _Optional[_Union[H128, _Mapping]] = ...) -> None: ...

class H512(_message.Message):
    __slots__ = ["hi", "lo"]
    HI_FIELD_NUMBER: _ClassVar[int]
    LO_FIELD_NUMBER: _ClassVar[int]
    hi: H256
    lo: H256
    def __init__(self, hi: _Optional[_Union[H256, _Mapping]] = ..., lo: _Optional[_Union[H256, _Mapping]] = ...) -> None: ...

class NodeInfoPorts(_message.Message):
    __slots__ = ["discovery", "listener"]
    DISCOVERY_FIELD_NUMBER: _ClassVar[int]
    LISTENER_FIELD_NUMBER: _ClassVar[int]
    discovery: int
    listener: int
    def __init__(self, discovery: _Optional[int] = ..., listener: _Optional[int] = ...) -> None: ...

class NodeInfoReply(_message.Message):
    __slots__ = ["enode", "enr", "id", "listenerAddr", "name", "ports", "protocols"]
    ENODE_FIELD_NUMBER: _ClassVar[int]
    ENR_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LISTENERADDR_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PORTS_FIELD_NUMBER: _ClassVar[int]
    PROTOCOLS_FIELD_NUMBER: _ClassVar[int]
    enode: str
    enr: str
    id: str
    listenerAddr: str
    name: str
    ports: NodeInfoPorts
    protocols: bytes
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., enode: _Optional[str] = ..., enr: _Optional[str] = ..., ports: _Optional[_Union[NodeInfoPorts, _Mapping]] = ..., listenerAddr: _Optional[str] = ..., protocols: _Optional[bytes] = ...) -> None: ...

class PeerInfo(_message.Message):
    __slots__ = ["caps", "connIsInbound", "connIsStatic", "connIsTrusted", "connLocalAddr", "connRemoteAddr", "enode", "enr", "id", "name"]
    CAPS_FIELD_NUMBER: _ClassVar[int]
    CONNISINBOUND_FIELD_NUMBER: _ClassVar[int]
    CONNISSTATIC_FIELD_NUMBER: _ClassVar[int]
    CONNISTRUSTED_FIELD_NUMBER: _ClassVar[int]
    CONNLOCALADDR_FIELD_NUMBER: _ClassVar[int]
    CONNREMOTEADDR_FIELD_NUMBER: _ClassVar[int]
    ENODE_FIELD_NUMBER: _ClassVar[int]
    ENR_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    caps: _containers.RepeatedScalarFieldContainer[str]
    connIsInbound: bool
    connIsStatic: bool
    connIsTrusted: bool
    connLocalAddr: str
    connRemoteAddr: str
    enode: str
    enr: str
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., enode: _Optional[str] = ..., enr: _Optional[str] = ..., caps: _Optional[_Iterable[str]] = ..., connLocalAddr: _Optional[str] = ..., connRemoteAddr: _Optional[str] = ..., connIsInbound: bool = ..., connIsTrusted: bool = ..., connIsStatic: bool = ...) -> None: ...

class VersionReply(_message.Message):
    __slots__ = ["major", "minor", "patch"]
    MAJOR_FIELD_NUMBER: _ClassVar[int]
    MINOR_FIELD_NUMBER: _ClassVar[int]
    PATCH_FIELD_NUMBER: _ClassVar[int]
    major: int
    minor: int
    patch: int
    def __init__(self, major: _Optional[int] = ..., minor: _Optional[int] = ..., patch: _Optional[int] = ...) -> None: ...
