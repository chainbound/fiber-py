from google.protobuf import empty_pb2 as _empty_pb2
from .types_pb2 import types_pb2 as _types_pb2
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

class Attestation(_message.Message):
    __slots__ = ["aggregation_bits", "data", "signature"]
    AGGREGATION_BITS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    aggregation_bits: bytes
    data: AttestationData
    signature: bytes
    def __init__(self, aggregation_bits: _Optional[bytes] = ..., data: _Optional[_Union[AttestationData, _Mapping]] = ..., signature: _Optional[bytes] = ...) -> None: ...

class AttestationData(_message.Message):
    __slots__ = ["beacon_block_root", "index", "slot", "source", "target"]
    BEACON_BLOCK_ROOT_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    SLOT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    beacon_block_root: bytes
    index: int
    slot: int
    source: Checkpoint
    target: Checkpoint
    def __init__(self, slot: _Optional[int] = ..., index: _Optional[int] = ..., beacon_block_root: _Optional[bytes] = ..., source: _Optional[_Union[Checkpoint, _Mapping]] = ..., target: _Optional[_Union[Checkpoint, _Mapping]] = ...) -> None: ...

class AttesterSlashing(_message.Message):
    __slots__ = ["attestation_1", "attestation_2"]
    ATTESTATION_1_FIELD_NUMBER: _ClassVar[int]
    ATTESTATION_2_FIELD_NUMBER: _ClassVar[int]
    attestation_1: IndexedAttestation
    attestation_2: IndexedAttestation
    def __init__(self, attestation_1: _Optional[_Union[IndexedAttestation, _Mapping]] = ..., attestation_2: _Optional[_Union[IndexedAttestation, _Mapping]] = ...) -> None: ...

class BLSToExecutionChange(_message.Message):
    __slots__ = ["from_bls_pubkey", "to_execution_address", "validator_index"]
    FROM_BLS_PUBKEY_FIELD_NUMBER: _ClassVar[int]
    TO_EXECUTION_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_INDEX_FIELD_NUMBER: _ClassVar[int]
    from_bls_pubkey: bytes
    to_execution_address: bytes
    validator_index: int
    def __init__(self, validator_index: _Optional[int] = ..., from_bls_pubkey: _Optional[bytes] = ..., to_execution_address: _Optional[bytes] = ...) -> None: ...

class BeaconBlock(_message.Message):
    __slots__ = ["body", "parent_root", "proposer_index", "slot", "state_root"]
    BODY_FIELD_NUMBER: _ClassVar[int]
    PARENT_ROOT_FIELD_NUMBER: _ClassVar[int]
    PROPOSER_INDEX_FIELD_NUMBER: _ClassVar[int]
    SLOT_FIELD_NUMBER: _ClassVar[int]
    STATE_ROOT_FIELD_NUMBER: _ClassVar[int]
    body: BeaconBlockBody
    parent_root: bytes
    proposer_index: int
    slot: int
    state_root: bytes
    def __init__(self, slot: _Optional[int] = ..., proposer_index: _Optional[int] = ..., parent_root: _Optional[bytes] = ..., state_root: _Optional[bytes] = ..., body: _Optional[_Union[BeaconBlockBody, _Mapping]] = ...) -> None: ...

class BeaconBlockBody(_message.Message):
    __slots__ = ["attestations", "attester_slashings", "bls_to_execution_changes", "deposits", "eth1_data", "execution_payload", "graffiti", "proposer_slashings", "randao_reveal", "sync_aggregate", "voluntary_exits"]
    ATTESTATIONS_FIELD_NUMBER: _ClassVar[int]
    ATTESTER_SLASHINGS_FIELD_NUMBER: _ClassVar[int]
    BLS_TO_EXECUTION_CHANGES_FIELD_NUMBER: _ClassVar[int]
    DEPOSITS_FIELD_NUMBER: _ClassVar[int]
    ETH1_DATA_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    GRAFFITI_FIELD_NUMBER: _ClassVar[int]
    PROPOSER_SLASHINGS_FIELD_NUMBER: _ClassVar[int]
    RANDAO_REVEAL_FIELD_NUMBER: _ClassVar[int]
    SYNC_AGGREGATE_FIELD_NUMBER: _ClassVar[int]
    VOLUNTARY_EXITS_FIELD_NUMBER: _ClassVar[int]
    attestations: _containers.RepeatedCompositeFieldContainer[Attestation]
    attester_slashings: _containers.RepeatedCompositeFieldContainer[AttesterSlashing]
    bls_to_execution_changes: _containers.RepeatedCompositeFieldContainer[SignedBLSToExecutionChange]
    deposits: _containers.RepeatedCompositeFieldContainer[Deposit]
    eth1_data: Eth1Data
    execution_payload: ExecutionPayload
    graffiti: bytes
    proposer_slashings: _containers.RepeatedCompositeFieldContainer[ProposerSlashing]
    randao_reveal: bytes
    sync_aggregate: SyncAggregate
    voluntary_exits: _containers.RepeatedCompositeFieldContainer[SignedVoluntaryExit]
    def __init__(self, randao_reveal: _Optional[bytes] = ..., eth1_data: _Optional[_Union[Eth1Data, _Mapping]] = ..., graffiti: _Optional[bytes] = ..., proposer_slashings: _Optional[_Iterable[_Union[ProposerSlashing, _Mapping]]] = ..., attester_slashings: _Optional[_Iterable[_Union[AttesterSlashing, _Mapping]]] = ..., attestations: _Optional[_Iterable[_Union[Attestation, _Mapping]]] = ..., deposits: _Optional[_Iterable[_Union[Deposit, _Mapping]]] = ..., voluntary_exits: _Optional[_Iterable[_Union[SignedVoluntaryExit, _Mapping]]] = ..., sync_aggregate: _Optional[_Union[SyncAggregate, _Mapping]] = ..., execution_payload: _Optional[_Union[ExecutionPayload, _Mapping]] = ..., bls_to_execution_changes: _Optional[_Iterable[_Union[SignedBLSToExecutionChange, _Mapping]]] = ...) -> None: ...

class BeaconBlockHeader(_message.Message):
    __slots__ = ["body_root", "parent_root", "proposer_index", "slot", "state_root"]
    BODY_ROOT_FIELD_NUMBER: _ClassVar[int]
    PARENT_ROOT_FIELD_NUMBER: _ClassVar[int]
    PROPOSER_INDEX_FIELD_NUMBER: _ClassVar[int]
    SLOT_FIELD_NUMBER: _ClassVar[int]
    STATE_ROOT_FIELD_NUMBER: _ClassVar[int]
    body_root: bytes
    parent_root: bytes
    proposer_index: int
    slot: int
    state_root: bytes
    def __init__(self, slot: _Optional[int] = ..., proposer_index: _Optional[int] = ..., parent_root: _Optional[bytes] = ..., state_root: _Optional[bytes] = ..., body_root: _Optional[bytes] = ...) -> None: ...

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

class Checkpoint(_message.Message):
    __slots__ = ["epoch", "root"]
    EPOCH_FIELD_NUMBER: _ClassVar[int]
    ROOT_FIELD_NUMBER: _ClassVar[int]
    epoch: int
    root: bytes
    def __init__(self, epoch: _Optional[int] = ..., root: _Optional[bytes] = ...) -> None: ...

class CompactBeaconBlock(_message.Message):
    __slots__ = ["body", "parent_root", "proposer_index", "slot", "state_root"]
    BODY_FIELD_NUMBER: _ClassVar[int]
    PARENT_ROOT_FIELD_NUMBER: _ClassVar[int]
    PROPOSER_INDEX_FIELD_NUMBER: _ClassVar[int]
    SLOT_FIELD_NUMBER: _ClassVar[int]
    STATE_ROOT_FIELD_NUMBER: _ClassVar[int]
    body: CompactBeaconBlockBody
    parent_root: bytes
    proposer_index: int
    slot: int
    state_root: bytes
    def __init__(self, slot: _Optional[int] = ..., proposer_index: _Optional[int] = ..., parent_root: _Optional[bytes] = ..., state_root: _Optional[bytes] = ..., body: _Optional[_Union[CompactBeaconBlockBody, _Mapping]] = ...) -> None: ...

class CompactBeaconBlockBody(_message.Message):
    __slots__ = ["attestations", "attester_slashings", "bls_to_execution_changes", "deposits", "eth1_data", "graffiti", "proposer_slashings", "randao_reveal", "sync_aggregate", "voluntary_exits"]
    ATTESTATIONS_FIELD_NUMBER: _ClassVar[int]
    ATTESTER_SLASHINGS_FIELD_NUMBER: _ClassVar[int]
    BLS_TO_EXECUTION_CHANGES_FIELD_NUMBER: _ClassVar[int]
    DEPOSITS_FIELD_NUMBER: _ClassVar[int]
    ETH1_DATA_FIELD_NUMBER: _ClassVar[int]
    GRAFFITI_FIELD_NUMBER: _ClassVar[int]
    PROPOSER_SLASHINGS_FIELD_NUMBER: _ClassVar[int]
    RANDAO_REVEAL_FIELD_NUMBER: _ClassVar[int]
    SYNC_AGGREGATE_FIELD_NUMBER: _ClassVar[int]
    VOLUNTARY_EXITS_FIELD_NUMBER: _ClassVar[int]
    attestations: _containers.RepeatedCompositeFieldContainer[Attestation]
    attester_slashings: _containers.RepeatedCompositeFieldContainer[AttesterSlashing]
    bls_to_execution_changes: _containers.RepeatedCompositeFieldContainer[SignedBLSToExecutionChange]
    deposits: _containers.RepeatedCompositeFieldContainer[Deposit]
    eth1_data: Eth1Data
    graffiti: bytes
    proposer_slashings: _containers.RepeatedCompositeFieldContainer[ProposerSlashing]
    randao_reveal: bytes
    sync_aggregate: SyncAggregate
    voluntary_exits: _containers.RepeatedCompositeFieldContainer[SignedVoluntaryExit]
    def __init__(self, randao_reveal: _Optional[bytes] = ..., eth1_data: _Optional[_Union[Eth1Data, _Mapping]] = ..., graffiti: _Optional[bytes] = ..., proposer_slashings: _Optional[_Iterable[_Union[ProposerSlashing, _Mapping]]] = ..., attester_slashings: _Optional[_Iterable[_Union[AttesterSlashing, _Mapping]]] = ..., attestations: _Optional[_Iterable[_Union[Attestation, _Mapping]]] = ..., deposits: _Optional[_Iterable[_Union[Deposit, _Mapping]]] = ..., voluntary_exits: _Optional[_Iterable[_Union[SignedVoluntaryExit, _Mapping]]] = ..., sync_aggregate: _Optional[_Union[SyncAggregate, _Mapping]] = ..., bls_to_execution_changes: _Optional[_Iterable[_Union[SignedBLSToExecutionChange, _Mapping]]] = ...) -> None: ...

class Deposit(_message.Message):
    __slots__ = ["data", "proof"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    PROOF_FIELD_NUMBER: _ClassVar[int]
    data: DepositData
    proof: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, proof: _Optional[_Iterable[bytes]] = ..., data: _Optional[_Union[DepositData, _Mapping]] = ...) -> None: ...

class DepositData(_message.Message):
    __slots__ = ["amount", "pubkey", "signature", "withdrawal_credentials"]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    PUBKEY_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    WITHDRAWAL_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    amount: int
    pubkey: bytes
    signature: bytes
    withdrawal_credentials: bytes
    def __init__(self, pubkey: _Optional[bytes] = ..., withdrawal_credentials: _Optional[bytes] = ..., amount: _Optional[int] = ..., signature: _Optional[bytes] = ...) -> None: ...

class Eth1Data(_message.Message):
    __slots__ = ["block_hash", "deposit_count", "deposit_root"]
    BLOCK_HASH_FIELD_NUMBER: _ClassVar[int]
    DEPOSIT_COUNT_FIELD_NUMBER: _ClassVar[int]
    DEPOSIT_ROOT_FIELD_NUMBER: _ClassVar[int]
    block_hash: bytes
    deposit_count: int
    deposit_root: bytes
    def __init__(self, deposit_root: _Optional[bytes] = ..., deposit_count: _Optional[int] = ..., block_hash: _Optional[bytes] = ...) -> None: ...

class ExecutionPayload(_message.Message):
    __slots__ = ["header", "transactions"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    header: ExecutionPayloadHeader
    transactions: _containers.RepeatedCompositeFieldContainer[Transaction]
    def __init__(self, header: _Optional[_Union[ExecutionPayloadHeader, _Mapping]] = ..., transactions: _Optional[_Iterable[_Union[Transaction, _Mapping]]] = ...) -> None: ...

class ExecutionPayloadHeader(_message.Message):
    __slots__ = ["base_fee_per_gas", "block_hash", "block_number", "extra_data", "fee_recipient", "gas_limit", "gas_used", "logs_bloom", "parent_hash", "prev_randao", "receipts_root", "state_root", "timestamp", "transactions_root", "withdrawals_root"]
    BASE_FEE_PER_GAS_FIELD_NUMBER: _ClassVar[int]
    BLOCK_HASH_FIELD_NUMBER: _ClassVar[int]
    BLOCK_NUMBER_FIELD_NUMBER: _ClassVar[int]
    EXTRA_DATA_FIELD_NUMBER: _ClassVar[int]
    FEE_RECIPIENT_FIELD_NUMBER: _ClassVar[int]
    GAS_LIMIT_FIELD_NUMBER: _ClassVar[int]
    GAS_USED_FIELD_NUMBER: _ClassVar[int]
    LOGS_BLOOM_FIELD_NUMBER: _ClassVar[int]
    PARENT_HASH_FIELD_NUMBER: _ClassVar[int]
    PREV_RANDAO_FIELD_NUMBER: _ClassVar[int]
    RECEIPTS_ROOT_FIELD_NUMBER: _ClassVar[int]
    STATE_ROOT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONS_ROOT_FIELD_NUMBER: _ClassVar[int]
    WITHDRAWALS_ROOT_FIELD_NUMBER: _ClassVar[int]
    base_fee_per_gas: bytes
    block_hash: bytes
    block_number: int
    extra_data: bytes
    fee_recipient: bytes
    gas_limit: int
    gas_used: int
    logs_bloom: bytes
    parent_hash: bytes
    prev_randao: bytes
    receipts_root: bytes
    state_root: bytes
    timestamp: int
    transactions_root: bytes
    withdrawals_root: bytes
    def __init__(self, parent_hash: _Optional[bytes] = ..., fee_recipient: _Optional[bytes] = ..., state_root: _Optional[bytes] = ..., receipts_root: _Optional[bytes] = ..., logs_bloom: _Optional[bytes] = ..., prev_randao: _Optional[bytes] = ..., block_number: _Optional[int] = ..., gas_limit: _Optional[int] = ..., gas_used: _Optional[int] = ..., timestamp: _Optional[int] = ..., extra_data: _Optional[bytes] = ..., base_fee_per_gas: _Optional[bytes] = ..., block_hash: _Optional[bytes] = ..., transactions_root: _Optional[bytes] = ..., withdrawals_root: _Optional[bytes] = ...) -> None: ...

class IndexedAttestation(_message.Message):
    __slots__ = ["attesting_indices", "data", "signature"]
    ATTESTING_INDICES_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    attesting_indices: _containers.RepeatedScalarFieldContainer[int]
    data: AttestationData
    signature: bytes
    def __init__(self, attesting_indices: _Optional[_Iterable[int]] = ..., data: _Optional[_Union[AttestationData, _Mapping]] = ..., signature: _Optional[bytes] = ...) -> None: ...

class ProposerSlashing(_message.Message):
    __slots__ = ["header_1", "header_2"]
    HEADER_1_FIELD_NUMBER: _ClassVar[int]
    HEADER_2_FIELD_NUMBER: _ClassVar[int]
    header_1: SignedBeaconBlockHeader
    header_2: SignedBeaconBlockHeader
    def __init__(self, header_1: _Optional[_Union[SignedBeaconBlockHeader, _Mapping]] = ..., header_2: _Optional[_Union[SignedBeaconBlockHeader, _Mapping]] = ...) -> None: ...

class SignedBLSToExecutionChange(_message.Message):
    __slots__ = ["message", "signature"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    message: BLSToExecutionChange
    signature: bytes
    def __init__(self, message: _Optional[_Union[BLSToExecutionChange, _Mapping]] = ..., signature: _Optional[bytes] = ...) -> None: ...

class SignedBeaconBlock(_message.Message):
    __slots__ = ["message", "signature"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    message: BeaconBlock
    signature: bytes
    def __init__(self, message: _Optional[_Union[BeaconBlock, _Mapping]] = ..., signature: _Optional[bytes] = ...) -> None: ...

class SignedBeaconBlockHeader(_message.Message):
    __slots__ = ["message", "signature"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    message: BeaconBlockHeader
    signature: bytes
    def __init__(self, message: _Optional[_Union[BeaconBlockHeader, _Mapping]] = ..., signature: _Optional[bytes] = ...) -> None: ...

class SignedVoluntaryExit(_message.Message):
    __slots__ = ["message", "signature"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    message: VoluntaryExit
    signature: bytes
    def __init__(self, message: _Optional[_Union[VoluntaryExit, _Mapping]] = ..., signature: _Optional[bytes] = ...) -> None: ...

class SyncAggregate(_message.Message):
    __slots__ = ["sync_committee_bits", "sync_committee_signature"]
    SYNC_COMMITTEE_BITS_FIELD_NUMBER: _ClassVar[int]
    SYNC_COMMITTEE_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    sync_committee_bits: bytes
    sync_committee_signature: bytes
    def __init__(self, sync_committee_bits: _Optional[bytes] = ..., sync_committee_signature: _Optional[bytes] = ...) -> None: ...

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

class VoluntaryExit(_message.Message):
    __slots__ = ["epoch", "validator_index"]
    EPOCH_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_INDEX_FIELD_NUMBER: _ClassVar[int]
    epoch: int
    validator_index: int
    def __init__(self, epoch: _Optional[int] = ..., validator_index: _Optional[int] = ...) -> None: ...
