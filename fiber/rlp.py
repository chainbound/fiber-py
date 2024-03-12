from dataclasses import dataclass
from typing import Tuple, Union
from eth_utils import to_bytes
from eth_typing import HexStr
from enum import Enum

from fiber.ethereum.rlp import decode_to, encode
from fiber.ethereum.base_types import (
    U64,
    U256,
    Bytes,
    Bytes0,
    Bytes20,
    Bytes32,
    Uint,
    slotted_freezable,
)

Address = Bytes20


def hex_to_bytes(data: str) -> bytes:
    return to_bytes(hexstr=HexStr(data))


@slotted_freezable
@dataclass
class LegacyTransaction:
    """
    Atomic operation performed on the block chain.
    """

    nonce: U256
    gas_price: Uint
    gas: Uint
    to: Union[Bytes0, Address]
    value: U256
    data: Bytes
    v: U256
    r: U256
    s: U256


@slotted_freezable
@dataclass
class AccessListTransaction:
    """
    The transaction type added in EIP-2930 to support access lists.
    """

    chain_id: U64
    nonce: U256
    gas_price: Uint
    gas: Uint
    to: Union[Bytes0, Address]
    value: U256
    data: Bytes
    access_list: Tuple[Tuple[Address, Tuple[Bytes32, ...]], ...]
    v: U256
    r: U256
    s: U256


@slotted_freezable
@dataclass
class FeeMarketTransaction:
    """
    The transaction type added in EIP-1559.
    """

    chain_id: U64
    nonce: U256
    max_priority_fee_per_gas: Uint
    max_fee_per_gas: Uint
    gas: Uint
    to: Union[Bytes0, Address]
    value: U256
    data: Bytes
    access_list: Tuple[Tuple[Address, Tuple[Bytes32, ...]], ...]
    v: U256
    r: U256
    s: U256


@slotted_freezable
@dataclass
class BlobTransaction:
    """
    The transaction type added in EIP-4844.
    """

    chain_id: U64
    nonce: U256
    max_priority_fee_per_gas: Uint
    max_fee_per_gas: Uint
    gas: Uint
    to: Union[Bytes0, Address]
    value: U256
    data: Bytes
    access_list: Tuple[Tuple[Address, Tuple[Bytes32, ...]], ...]
    max_fee_per_blob_gas: Uint
    blob_versioned_hashes: Tuple[Bytes32, ...]
    v: U256
    r: U256
    s: U256


RlpTransaction = Union[
    LegacyTransaction, AccessListTransaction, FeeMarketTransaction, BlobTransaction
]


def encode_transaction(tx: RlpTransaction) -> Bytes:
    if isinstance(tx, LegacyTransaction):
        return encode(tx)
    elif isinstance(tx, AccessListTransaction):
        return b"\x01" + encode(tx)
    elif isinstance(tx, FeeMarketTransaction):
        return b"\x02" + encode(tx)
    else:
        raise Exception(f"Unable to encode transaction of type {type(tx)}")


def decode_raw_transaction(tx: bytes) -> tuple[RlpTransaction, Uint]:
    """
    Decodes a raw transaction into a transaction object and returns the
    decoded transaction and the transaction type. It is `None` if the
    transaction is a legacy transaction.
    """

    tx_type = tx[0]

    if tx[0] == 1:
        decoded = decode_to(AccessListTransaction, tx[1:])
    elif tx[0] == 2:
        decoded = decode_to(FeeMarketTransaction, tx[1:])
    elif tx[0] == 3:
        decoded = decode_to(BlobTransaction, tx[1:])
    else:
        decoded = decode_to(LegacyTransaction, tx)
        tx_type = 0

    return (decoded, tx_type)
