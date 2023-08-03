from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

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
