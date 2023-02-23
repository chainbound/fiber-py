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
        return self.stub.SubscribeNewBlocks(api_pb2.google_dot_protobuf_dot_empty__pb2.Empty(), metadata=self.metadata)
    
    def send_transaction(self, tx: Transaction):
        res = self.stub.SendTransaction(tx, metadata=self.metadata)
        
        return res.hash, res.timestamp

    def send_transaction_sequence(self, txs: list[Transaction]):
        res = self.stub.SendTransactionSequence(txs, metadata=self.metadata)
        
        return map(lambda sequence_response: sequence_response.hash, res), res[0].timestamp

    def send_raw_transaction(self, tx: bytes):
        res = self.stub.SendRawTransaction(tx, metadata=self.metadata)
        
        return res.hash, res.timestamp

    def send_raw_transaction_sequence(self, txs: list[bytes]):
        res = self.stub.SendRawTransactionSequence(txs, metadata=self.metadata)
        
        return map(lambda sequence_response: sequence_response.hash, res), res[0].timestamp 
