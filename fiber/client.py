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
    tx.v = proto.v
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
    block.producer = encode_hex(proto.producer)
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