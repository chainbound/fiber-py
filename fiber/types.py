from eth_utils import encode_hex, big_endian_to_int
from typing import Any, List, Optional

from fiber.proto import eth_pb2

# ================= TRANSACTION =================

class Transaction:
    to: str
    gas: int
    hash: str
    nonce: int
    value: int
    sender: str
    type: int
    gas_price: int
    input: str
    max_fee: int
    priority_fee: int
    v: int
    r: str
    s: str
    access_list: Any
    chain_id: int

    def __repr__(self):
        return str(self.__dict__)

def proto_to_tx(proto: eth_pb2.Transaction):
    v = proto.v
    if proto.type > 0:
        if v > 1:
            v = v - 37

    tx = Transaction()
    tx.chain_id = proto.chainId
    tx.to = encode_hex(proto.to)
    tx.hash = encode_hex(proto.hash)
    tx.nonce = proto.nonce
    tx.value = big_endian_to_int(proto.value)
    tx.sender = encode_hex(getattr(proto, "from"))
    tx.type = proto.type
    tx.gas = proto.gas
    tx.gas_price = proto.gas_price
    tx.max_fee = proto.max_fee
    tx.priority_fee = proto.priority_fee
    tx.input = encode_hex(proto.input)
    tx.access_list = proto.access_list
    tx.v = v
    tx.r = encode_hex(proto.r)
    tx.s = encode_hex(proto.s)
    return tx

def tx_to_proto(tx: Transaction):
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
    hash: str
    number: int
    parent_hash: str
    timestamp: int
    producer: str
    base_fee_per_gas: int
    extra_data: str
    fee_recipient: str
    gas_limit: int
    gas_used: int
    logs_bloom: bytes
    prev_randao: bytes
    receipt_root: bytes
    state_root: bytes

    def __repr__(self):
        return str(self.__dict__)
    
class ExecutionPayload:
    header: ExecutionPayloadHeader
    transactions: list[Transaction]

def proto_to_execution_payload_header(proto: eth_pb2.ExecutionPayloadHeader):
    header = ExecutionPayloadHeader()
    header.hash = encode_hex(proto.hash)
    header.number = proto.number
    header.parent_hash = encode_hex(proto.parent_hash)
    header.timestamp = proto.timestamp
    header.base_fee_per_gas = proto.base_fee_per_gas
    header.extra_data = encode_hex(proto.extra_data)
    header.fee_recipient = encode_hex(proto.fee_recipient)
    header.gas_limit = proto.gas_limit
    header.gas_used = proto.gas_used
    header.logs_bloom = encode_hex(proto.logs_bloom)
    header.prev_randao = encode_hex(proto.prev_randao)
    header.receipt_root = encode_hex(proto.receipt_root)
    header.state_root = encode_hex(proto.state_root)
    return header

def proto_to_execution_payload(proto: eth_pb2.ExecutionPayload):
    payload = ExecutionPayload()
    payload.header = proto_to_execution_payload_header(proto.header)
    payload.transactions = list(map(lambda proto: proto_to_tx(proto), proto.transactions))
    return payload

# ================= BEACON BLOCK =================

class Checkpoint:
    epoch: int
    root: bytes

class AttestationData:
    slot: int
    index: int
    beacon_block_root: bytes
    source: Optional[Checkpoint]
    target: Optional[Checkpoint]

class IndexedAttestation:
    attesting_indices_list: List[int]
    data: Optional[AttestationData]
    signature: bytes

class AttesterSlashing:
    attestation1: Optional[IndexedAttestation]
    attestation2: Optional[IndexedAttestation]

class BeaconBlockHeader:
    slot: int
    proposer_index: int
    parent_root: bytes
    state_root: bytes
    body_root: bytes

class SignedBeaconBlockHeader:
    message: Optional[BeaconBlockHeader]
    signature: bytes

class ProposerSlashing:
    header1: Optional[SignedBeaconBlockHeader]
    header2: Optional[SignedBeaconBlockHeader]

class DepositData:
    pubkey: bytes
    withdrawal_credentials: bytes
    amount: int
    signature: bytes

class Deposit:
    proof_list: List[bytes]
    data: Optional[DepositData]

class ExecutionChangeMessage:
    validator_index: int
    from_bls_pubkey: bytes
    to_execution_address: bytes

class ExecutionChange:
    message: ExecutionChangeMessage
    signature: bytes

class Eth1Data:
    deposit_root: bytes
    deposit_count: int
    block_hash: bytes

class SyncAggregate:
    sync_committee_bits: bytes
    sync_committee_signature: bytes

class VoluntaryExit:
    epoch: int
    validator_index: int

class SignedVoluntaryExit:
    message: VoluntaryExit
    signature: bytes

class BeaconBlockBody:
    randao_reveal: bytes
    eth1_data: Eth1Data
    graffiti: bytes
    proposer_slashings: List[ProposerSlashing]
    attester_slashings: List[AttesterSlashing]
    attestations: List[IndexedAttestation]
    deposits: List[Deposit]
    voluntary_exits: List[SignedVoluntaryExit]
    sync_aggregate: SyncAggregate
    bls_to_execution_changes: List[ExecutionChange]

class BeaconBlock:
    slot: int
    proposer_index: int
    parent_root: bytes
    state_root: bytes
    body: BeaconBlockBody


def proto_to_beacon_block(block: eth_pb2.BeaconBlock):
    body = block.body

    beacon = BeaconBlock()
    beacon.slot = block.slot
    beacon.proposer_index = block.proposer_index
    beacon.parent_root = block.parent_root
    beacon.state_root = block.state_root
    beacon.body = {
        "randao_reveal": body.randao_reveal,
        "eth1_data": {
            "deposit_root": body.eth1_data.deposit_root,
            "deposit_count": body.eth1_data.deposit_count,
            "block_hash": body.eth1_data.block_hash
        },
        "graffiti": body.graffiti,
        "proposer_slashings": list(map(lambda proto: proto_to_proposer_slashing(proto), body.proposer_slashings)),
        "attester_slashings": list(map(lambda proto: proto_to_attester_slashing(proto), body.attester_slashings)),
        "attestations": list(map(lambda proto: proto_to_indexed_attestation(proto), body.attestations)),
        "deposits": list(map(lambda proto: proto_to_deposit(proto), body.deposits)),
        "voluntary_exits": list(map(lambda proto: proto_to_voluntary_exit(proto), body.voluntary_exits)),
        "bls_to_execution_changes": list(map(lambda proto: proto_to_execution_change(proto), body.bls_to_execution_changes)),
        "sync_aggregate": {
            "sync_committee_bits": body.sync_aggregate.sync_committee_bits,
            "sync_committee_signature": body.sync_aggregate.sync_committee_signature
        }
    }

    return beacon

def proto_to_proposer_slashing(proto: eth_pb2.ProposerSlashing):
    slashing = ProposerSlashing()
    slashing.header1 = proto_to_signed_beacon_block_header(proto.header1)
    slashing.header2 = proto_to_signed_beacon_block_header(proto.header2)
    return slashing

def proto_to_attester_slashing(proto: eth_pb2.AttesterSlashing):
    slashing = AttesterSlashing()
    slashing.attestation1 = proto_to_indexed_attestation(proto.attestation1)
    slashing.attestation2 = proto_to_indexed_attestation(proto.attestation2)
    return slashing

def proto_to_indexed_attestation(proto: eth_pb2.IndexedAttestation):
    attestation = IndexedAttestation()
    attestation.attesting_indices_list = proto.attesting_indices_list
    attestation.data = proto_to_attestation_data(proto.data)
    attestation.signature = proto.signature
    return attestation

def proto_to_attestation_data(proto: eth_pb2.AttestationData):
    data = AttestationData()
    data.slot = proto.slot
    data.index = proto.index
    data.beacon_block_root = proto.beacon_block_root
    data.source = proto_to_checkpoint(proto.source)
    data.target = proto_to_checkpoint(proto.target)
    return data

def proto_to_checkpoint(proto: eth_pb2.Checkpoint):
    checkpoint = Checkpoint()
    checkpoint.epoch = proto.epoch
    checkpoint.root = proto.root
    return checkpoint

def proto_to_signed_beacon_block_header(proto: eth_pb2.SignedBeaconBlockHeader):
    header = SignedBeaconBlockHeader()
    header.message = proto_to_beacon_block_header(proto.message)
    header.signature = proto.signature
    return header

def proto_to_beacon_block_header(proto: eth_pb2.BeaconBlockHeader):
    header = BeaconBlockHeader()
    header.slot = proto.slot
    header.proposer_index = proto.proposer_index
    header.parent_root = proto.parent_root
    header.state_root = proto.state_root
    header.body_root = proto.body_root
    return header

def proto_to_deposit(proto: eth_pb2.Deposit):
    deposit = Deposit()
    deposit.proof_list = proto.proof_list
    deposit.data = proto_to_deposit_data(proto.data)
    return deposit

def proto_to_deposit_data(proto: eth_pb2.DepositData):
    data = DepositData()
    data.pubkey = proto.pubkey
    data.withdrawal_credentials = proto.withdrawal_credentials
    data.amount = proto.amount
    data.signature = proto.signature
    return data

def proto_to_voluntary_exit(proto: eth_pb2.SignedVoluntaryExit):
    exit = SignedVoluntaryExit()
    exit.message = proto_to_voluntary_exit_message(proto.message)
    exit.signature = proto.signature
    return exit

def proto_to_voluntary_exit_message(proto: eth_pb2.VoluntaryExit):
    exit = VoluntaryExit()
    exit.epoch = proto.epoch
    exit.validator_index = proto.validator_index
    return exit

def proto_to_execution_change(proto: eth_pb2.ExecutionChange):
    change = ExecutionChange()
    change.message = proto_to_execution_change_message(proto.message)
    change.signature = proto.signature
    return change

def proto_to_execution_change_message(proto: eth_pb2.ExecutionChangeMessage):
    change = ExecutionChangeMessage()
    change.validator_index = proto.validator_index
    change.from_bls_pubkey = proto.from_bls_pubkey
    change.to_execution_address = proto.to_execution_address
    return change