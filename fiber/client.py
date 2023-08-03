import grpc

from fiber.proto import api_pb2_grpc
from fiber.proto import api_pb2
from fiber.types import *

empty = api_pb2.google_dot_protobuf_dot_empty__pb2.Empty()

class Client:
    def __init__(self, api: str, key: str):
        self.api = api
        self.key = key
        self.metadata = (('x-api-key', self.key),)
    
    def connect(self):
        channel = grpc.insecure_channel(self.api)
        self.stub = api_pb2_grpc.APIStub(channel)
    
    def subscribe_new_txs(self):
        return map(lambda proto: proto_to_tx(proto), 
                   self.stub.SubscribeNewTxs(api_pb2.TxFilter(), metadata=self.metadata))

    def subscribe_new_execution_payload_headers(self):
        return map(lambda proto: proto_to_execution_payload_header(proto), 
                   self.stub.SubscribeExecutionHeaders(empty, metadata=self.metadata))
    
    def subscribe_new_execution_payloads(self):
        return map(lambda proto: proto_to_execution_payload(proto), 
                   self.stub.SubscribeExecutionPayloads(empty, metadata=self.metadata))

    def subscribe_new_beacon_blocks(self):
        return map(lambda proto: proto_to_beacon_block(proto), 
                   self.stub.SubscribeBeaconBlocks(empty, metadata=self.metadata))
    
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
