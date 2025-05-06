from eth_utils import encode_hex, to_bytes
from typing import Any, List, Optional, Tuple
from eth_typing import HexStr

import fiber.rlp as rlp
from fiber.proto import eth_pb2
from fiber.proto import api_pb2
from fiber.ethereum.crypto_hash import keccak256
from fiber.ethereum.base_types import (Bytes20, Bytes32)


def hex_to_bytes(data: str) -> bytes:
    return to_bytes(hexstr=HexStr(data))


def bytes_to_hex(data: bytes) -> HexStr:
    return HexStr(data.hex())


def hex_to_int(data: str) -> int:
    return int(data[2:], 16)


def acl_to_tuple(acl: eth_pb2.AccessTuple) -> Tuple[Tuple[Bytes20, Tuple[Bytes32, ...]], ...]:
    return tuple(map(lambda tup: (tup.address, tuple(map(lambda bytes_: bytes_, tup.storage_keys))), acl))


# ================= TRANSACTION =================

class Transaction:
    to: HexStr
    gas: int
    hash: HexStr
    nonce: int
    value: int
    sender: HexStr
    type: int
    gas_price: int
    input: HexStr
    max_fee: int
    priority_fee: int
    v: int
    r: HexStr
    s: HexStr
    access_list: Any
    chain_id: int

    # EIP-4844
    blob_versioned_hashes: List[HexStr]
    max_fee_per_blob_gas: int

    # EIP-7702
    authorization_list: Any

    # internal fields
    _rlp_bytes: bytes

    def __repr__(self):
        return str(self.__dict__)

    def to_rlp_bytes(self) -> bytes:
        return self._rlp_bytes

    def to_rlp_hex(self) -> str:
        return encode_hex(self.to_rlp_bytes())


def proto_to_tx(raw: api_pb2.TransactionWithSenderMsg) -> Transaction:
    tx = rlp_to_tx(raw.rlp_transaction)

    tx._rlp_bytes = raw.rlp_transaction
    tx.hash = "0x" + keccak256(raw.rlp_transaction).hex()
    tx.sender = "0x" + raw.sender.hex()

    return tx


def rlp_to_tx(rlp_tx: bytes) -> Transaction:
    """
    Converts an RLP transaction to a Transaction object.
    Fields: hash, _rlp_bytes, sender are not set in this function.
    """

    [decoded_tx, tx_type] = rlp.decode_raw_transaction(rlp_tx)

    v = decoded_tx.v
    if tx_type > 0:
        if v > 1:
            v = v - 37

    tx = Transaction()
    tx.type = tx_type

    tx.to = "0x" + bytes_to_hex(decoded_tx.to)
    tx.chain_id = decoded_tx.chain_id if hasattr(
        decoded_tx, "chain_id") else 0

    tx.nonce = decoded_tx.nonce
    tx.value = decoded_tx.value
    tx.gas = decoded_tx.gas

    tx.gas_price = decoded_tx.gas_price if hasattr(
        decoded_tx, "gas_price") else None
    tx.max_fee = decoded_tx.max_fee_per_gas if hasattr(
        decoded_tx, "max_fee_per_gas") else None
    tx.priority_fee = decoded_tx.max_priority_fee_per_gas if hasattr(
        decoded_tx, "max_priority_fee_per_gas") else None

    # EIP-4844
    blob_versioned_hashes = []
    if hasattr(decoded_tx, "blob_versioned_hashes"):
        for hash in decoded_tx.blob_versioned_hashes:
            blob_versioned_hashes.append("0x" + bytes_to_hex(hash))

    tx.blob_versioned_hashes = blob_versioned_hashes

    tx.max_fee_per_blob_gas = decoded_tx.max_fee_per_blob_gas if hasattr(
        decoded_tx, "max_fee_per_blob_gas") else 0

    # EIP-7702
    tx.authorization_list = decoded_tx.authorization_list if hasattr(
        decoded_tx, "authorization_list") else []

    tx.input = bytes_to_hex(decoded_tx.data)
    tx.access_list = decoded_tx.access_list if hasattr(
        decoded_tx, "access_list") else []
    tx.v = v
    tx.r = decoded_tx.r
    tx.s = decoded_tx.s

    return tx


def tx_to_proto(tx: Transaction) -> eth_pb2.Transaction:
    """
    WARNING: does not work with tx type 3 and 4
    """
    proto = eth_pb2.Transaction()
    proto.chainId = tx.chain_id
    proto.to = bytes.fromhex(tx.to)
    proto.hash = bytes.fromhex(tx.hash)
    proto.nonce = tx.nonce
    proto.value = tx.value.to_bytes(32, 'big')
    proto.type = tx.type
    proto.gas_price = tx.gas_price
    proto.max_fee = tx.max_fee
    proto.priority_fee = tx.priority_fee
    proto.input = bytes.fromhex(tx.input)
    proto.access_list = tx.access_list
    proto.v = tx.v
    proto.r = bytes.fromhex(tx.r)
    proto.s = bytes.fromhex(tx.s)
    return proto

# ================= EXECUTION PAYLOAD =================


class ExecutionPayloadHeader:
    hash: HexStr
    number: int
    parent_hash: HexStr
    timestamp: int
    producer: HexStr
    base_fee_per_gas: int
    extra_data: HexStr
    fee_recipient: HexStr
    gas_limit: int
    gas_used: int
    logs_bloom: HexStr
    prev_randao: HexStr
    receipt_root: HexStr
    state_root: HexStr

    def __repr__(self):
        return str(self.__dict__)


class ExecutionPayload:
    header: ExecutionPayloadHeader
    transactions: list[Transaction]


def proto_to_execution_payload_header(proto: eth_pb2.ExecutionPayloadHeader) -> ExecutionPayloadHeader:
    header = ExecutionPayloadHeader()
    header.hash = encode_hex(proto.block_hash)
    header.number = proto.block_number
    header.parent_hash = encode_hex(proto.parent_hash)
    header.timestamp = proto.timestamp
    header.base_fee_per_gas = proto.base_fee_per_gas
    header.extra_data = encode_hex(proto.extra_data)
    header.fee_recipient = encode_hex(proto.fee_recipient)
    header.gas_limit = proto.gas_limit
    header.gas_used = proto.gas_used
    header.logs_bloom = encode_hex(proto.logs_bloom)
    header.prev_randao = encode_hex(proto.prev_randao)
    header.receipt_root = encode_hex(proto.receipts_root)
    header.state_root = encode_hex(proto.state_root)
    return header


def proto_to_execution_payload(proto: api_pb2.ExecutionPayloadMsg) -> ExecutionPayload:
    # TODO: decode ssz payload

    payload = ExecutionPayload()
    payload.header = proto_to_execution_payload_header(proto.header)
    payload.transactions = list(
        map(lambda proto: rlp_to_tx(proto), proto.transactions))
    return payload

# ================= BEACON BLOCK =================


class Checkpoint:
    epoch: int
    root: HexStr


class AttestationData:
    slot: int
    index: int
    beacon_block_root: HexStr
    source: Optional[Checkpoint]
    target: Optional[Checkpoint]


class IndexedAttestation:
    attesting_indices_list: List[int]
    data: Optional[AttestationData]
    signature: HexStr


class AttesterSlashing:
    attestation1: Optional[IndexedAttestation]
    attestation2: Optional[IndexedAttestation]


class BeaconBlockHeader:
    slot: int
    proposer_index: int
    parent_root: HexStr
    state_root: HexStr
    body_root: HexStr


class SignedBeaconBlockHeader:
    message: Optional[BeaconBlockHeader]
    signature: HexStr


class ProposerSlashing:
    header1: Optional[SignedBeaconBlockHeader]
    header2: Optional[SignedBeaconBlockHeader]


class DepositData:
    pubkey: HexStr
    withdrawal_credentials: HexStr
    amount: int
    signature: HexStr


class Deposit:
    proof_list: List[HexStr]
    data: Optional[DepositData]


class ExecutionChangeMessage:
    validator_index: int
    from_bls_pubkey: HexStr
    to_execution_address: HexStr


class ExecutionChange:
    message: ExecutionChangeMessage
    signature: HexStr


class Eth1Data:
    deposit_root: HexStr
    deposit_count: int
    block_hash: HexStr


class SyncAggregate:
    sync_committee_bits: HexStr
    sync_committee_signature: HexStr


class VoluntaryExit:
    epoch: int
    validator_index: int


class SignedVoluntaryExit:
    message: VoluntaryExit
    signature: HexStr


class Attestation:
    aggregation_bits: HexStr
    data: AttestationData
    signature: HexStr


class BeaconBlockBody:
    randao_reveal: HexStr
    eth1_data: Eth1Data
    graffiti: HexStr
    proposer_slashings: List[ProposerSlashing]
    attester_slashings: List[AttesterSlashing]
    attestations: List[Attestation]
    deposits: List[Deposit]
    voluntary_exits: List[SignedVoluntaryExit]
    sync_aggregate: SyncAggregate
    bls_to_execution_changes: List[ExecutionChange]


class BeaconBlock:
    slot: int
    proposer_index: int
    parent_root: HexStr
    state_root: HexStr
    body: BeaconBlockBody


def proto_to_beacon_block(block: eth_pb2.BeaconBlock) -> BeaconBlock:
    body = block.body

    beacon = BeaconBlock()
    beacon.slot = block.slot
    beacon.proposer_index = block.proposer_index
    beacon.parent_root = encode_hex(block.parent_root)
    beacon.state_root = encode_hex(block.state_root)
    beacon.body = {
        "randao_reveal": encode_hex(body.randao_reveal),
        "eth1_data": {
            "deposit_root": encode_hex(body.eth1_data.deposit_root),
            "deposit_count": body.eth1_data.deposit_count,
            "block_hash": encode_hex(body.eth1_data.block_hash)
        },
        "graffiti": encode_hex(body.graffiti),
        "proposer_slashings": list(map(lambda proto: proto_to_proposer_slashing(proto), body.proposer_slashings)),
        "attester_slashings": list(map(lambda proto: proto_to_attester_slashing(proto), body.attester_slashings)),
        "attestations": list(map(lambda proto: proto_to_attestation(proto), body.attestations)),
        "deposits": list(map(lambda proto: proto_to_deposit(proto), body.deposits)),
        "voluntary_exits": list(map(lambda proto: proto_to_voluntary_exit(proto), body.voluntary_exits)),
        "bls_to_execution_changes": list(map(lambda proto: proto_to_execution_change(proto), body.bls_to_execution_changes)),
        "sync_aggregate": {
            "sync_committee_bits": body.sync_aggregate.sync_committee_bits,
            "sync_committee_signature": body.sync_aggregate.sync_committee_signature
        }
    }

    return beacon


def proto_to_proposer_slashing(proto: eth_pb2.ProposerSlashing) -> ProposerSlashing:
    slashing = ProposerSlashing()
    slashing.header1 = proto_to_signed_beacon_block_header(proto.header_1)
    slashing.header2 = proto_to_signed_beacon_block_header(proto.header_2)
    return slashing


def proto_to_attester_slashing(proto: eth_pb2.AttesterSlashing) -> AttesterSlashing:
    slashing = AttesterSlashing()
    slashing.attestation1 = proto_to_indexed_attestation(proto.attestation_1)
    slashing.attestation2 = proto_to_indexed_attestation(proto.attestation_2)
    return slashing


def proto_to_indexed_attestation(proto: eth_pb2.IndexedAttestation) -> IndexedAttestation:
    attestation = IndexedAttestation()
    attestation.attesting_indices_list = proto.attesting_indices
    attestation.data = proto_to_attestation_data(proto.data)
    attestation.signature = encode_hex(proto.signature)
    return attestation


def proto_to_attestation(proto: eth_pb2.Attestation) -> Attestation:
    attestation = Attestation
    attestation.aggregation_bits = encode_hex(proto.aggregation_bits)
    attestation.data = proto_to_attestation_data(proto.data)
    attestation.signature: encode_hex(proto.signature)  # type: ignore
    return attestation


def proto_to_attestation_data(proto: eth_pb2.AttestationData) -> AttestationData:
    data = AttestationData()
    data.slot = proto.slot
    data.index = proto.index
    data.beacon_block_root = encode_hex(proto.beacon_block_root)
    data.source = proto_to_checkpoint(proto.source)
    data.target = proto_to_checkpoint(proto.target)
    return data


def proto_to_checkpoint(proto: eth_pb2.Checkpoint) -> Checkpoint:
    checkpoint = Checkpoint()
    checkpoint.epoch = proto.epoch
    checkpoint.root = encode_hex(proto.root)
    return checkpoint


def proto_to_signed_beacon_block_header(proto: eth_pb2.SignedBeaconBlockHeader) -> SignedBeaconBlockHeader:
    header = SignedBeaconBlockHeader()
    header.message = proto_to_beacon_block_header(proto.message)
    header.signature = encode_hex(proto.signature)
    return header


def proto_to_beacon_block_header(proto: eth_pb2.BeaconBlockHeader) -> BeaconBlockHeader:
    header = BeaconBlockHeader()
    header.slot = proto.slot
    header.proposer_index = proto.proposer_index
    header.parent_root = encode_hex(proto.parent_root)
    header.state_root = encode_hex(proto.state_root)
    header.body_root = encode_hex(proto.body_root)
    return header


def proto_to_deposit(proto: eth_pb2.Deposit) -> Deposit:
    deposit = Deposit()
    deposit.proof_list = list(
        map(lambda proof: encode_hex(proof), proto.proof))
    deposit.data = proto_to_deposit_data(proto.data)
    return deposit


def proto_to_deposit_data(proto: eth_pb2.DepositData) -> DepositData:
    data = DepositData()
    data.pubkey = encode_hex(proto.pubkey)
    data.withdrawal_credentials = encode_hex(proto.withdrawal_credentials)
    data.amount = proto.amount
    data.signature = encode_hex(proto.signature)
    return data


def proto_to_voluntary_exit(proto: eth_pb2.SignedVoluntaryExit) -> SignedVoluntaryExit:
    exit = SignedVoluntaryExit()
    exit.message = proto_to_voluntary_exit_message(proto.message)
    exit.signature = encode_hex(proto.signature)
    return exit


def proto_to_voluntary_exit_message(proto: eth_pb2.VoluntaryExit) -> VoluntaryExit:
    exit = VoluntaryExit()
    exit.epoch = proto.epoch
    exit.validator_index = proto.validator_index
    return exit


def proto_to_execution_change(proto: eth_pb2.SignedBLSToExecutionChange) -> ExecutionChange:
    change = ExecutionChange()
    change.message = proto_to_execution_change_message(proto.message)
    change.signature = encode_hex(proto.signature)
    return change


def proto_to_execution_change_message(proto: eth_pb2.BLSToExecutionChange) -> ExecutionChangeMessage:
    change = ExecutionChangeMessage()
    change.validator_index = proto.validator_index
    change.from_bls_pubkey = encode_hex(proto.from_bls_pubkey)
    change.to_execution_address = encode_hex(proto.to_execution_address)
    return change
