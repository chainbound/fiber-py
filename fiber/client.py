from fiber import eth_pb2
from fiber import api_pb2_grpc
from fiber import api_pb2
import grpc

from eth_typing import Address
from eth_utils import encode_hex, big_endian_to_int
from typing import Any

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
    else:
        if v > 28:
            v = v - 10

    tx = Transaction()
    tx.chain_id = proto.chainId
    tx.to = encode_hex(proto.to)
    tx.hash = encode_hex(proto.hash)
    tx.nonce = proto.nonce
    tx.value = big_endian_to_int(proto.value)
    tx.sender = encode_hex(getattr(proto, "from"))
    tx.type = proto.type
    tx.gas_price = proto.gas_price
    tx.max_fee = proto.max_fee
    tx.priority_fee = proto.priority_fee
    tx.input = encode_hex(proto.input)
    tx.access_list = proto.access_list
    tx.v = v
    tx.r = encode_hex(proto.r)
    tx.s = encode_hex(proto.s)
    return tx

class Block:
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
    transactions: list[Transaction]

    def __repr__(self):
        return str(self.__dict__)
    
def proto_to_block(proto: eth_pb2.Block):
    block = Block()
    block.hash = encode_hex(proto.hash)
    block.number = proto.number
    block.parent_hash = encode_hex(proto.parent_hash)
    block.timestamp = proto.timestamp
    block.base_fee_per_gas = proto.base_fee_per_gas
    block.extra_data = encode_hex(proto.extra_data)
    block.fee_recipient = encode_hex(proto.fee_recipient)
    block.gas_limit = proto.gas_limit
    block.gas_used = proto.gas_used
    block.logs_bloom = proto.logs_bloom
    block.prev_randao = proto.prev_randao
    block.receipt_root = proto.receipt_root
    block.state_root = proto.state_root
    block.transactions = list(map(lambda proto: proto_to_tx(proto), proto.transactions))
    return block

def proto_to_header(proto: eth_pb2.Block):
    block = Block()
    block.hash = encode_hex(proto.hash)
    block.number = proto.number
    block.parent_hash = encode_hex(proto.parent_hash)
    block.timestamp = proto.timestamp
    block.base_fee_per_gas = proto.base_fee_per_gas
    block.extra_data = encode_hex(proto.extra_data)
    block.fee_recipient = encode_hex(proto.fee_recipient)
    block.gas_limit = proto.gas_limit
    block.gas_used = proto.gas_used
    block.logs_bloom = encode_hex(proto.logs_bloom)
    block.prev_randao = encode_hex(proto.prev_randao)
    block.receipt_root = encode_hex(proto.receipt_root)
    block.state_root = encode_hex(proto.state_root)
    return block

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

class Client:
    def __init__(self, api: str, key: str):
        self.api = api
        self.key = key
        self.metadata = (('x-api-key', self.key),)
    
    def connect(self):
        channel = grpc.insecure_channel(self.api)
        self.stub = api_pb2_grpc.APIStub(channel)
    
    def subscribe_new_txs(self):
        return map(lambda proto: proto_to_tx(proto), self.stub.SubscribeNewTxs(api_pb2.TxFilter(), metadata=self.metadata))

    def subscribe_new_blocks(self):
        return map(lambda proto: proto_to_block(proto), self.stub.SubscribeNewBlocks(api_pb2.google_dot_protobuf_dot_empty__pb2.Empty(), metadata=self.metadata))

    def subscribe_new_headers(self):
        return map(lambda proto: proto_to_header(proto), self.stub.SubscribeNewHeaders(api_pb2.google_dot_protobuf_dot_empty__pb2.Empty(), metadata=self.metadata))
    
    def send_transaction(self, tx: Transaction):
        res = self.stub.SendTransaction(tx_to_proto(tx), metadata=self.metadata)
        
        return res.hash, res.timestamp

    def send_transaction_sequence(self, txs: list[Transaction]):
        res = self.stub.SendTransactionSequence(txs, metadata=self.metadata)
        
        return map(lambda sequence_response: sequence_response.hash, res), res[0].timestamp

    def send_raw_transaction(self, tx: bytes):
        res = self.stub.SendRawTransaction(tx_to_proto(tx), metadata=self.metadata)
        
        return res.hash, res.timestamp

    def send_raw_transaction_sequence(self, txs: list[bytes]):
        res = self.stub.SendRawTransactionSequence(txs, metadata=self.metadata)
        
        return map(lambda sequence_response: sequence_response.hash, res), res[0].timestamp 
