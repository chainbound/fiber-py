import grpc
import pkg_resources

from fiber.proto import api_pb2_grpc
from fiber.proto import api_pb2
from fiber.types import (
    proto_to_tx,
    tx_to_proto,
    Transaction,
)

empty = api_pb2.google_dot_protobuf_dot_empty__pb2.Empty()


class Client:
    def __init__(self, api: str, key: str):
        self.api = api
        self.key = key
        client_version = pkg_resources.get_distribution("fiber-py").version

        self.metadata = (
            ("x-api-key", self.key),
            ("x-client-version", f"fiber-py/v{client_version}"),
        )

    def connect(self):
        channel = grpc.insecure_channel(self.api)
        self.stub = api_pb2_grpc.APIStub(channel)

    def subscribe_new_txs(self):
        (lambda raw: proto_to_tx(raw),)
        self.stub.SubscribeNewTxsV2(
            api_pb2.TxFilter(),
        )

    def subscribe_new_raw_txs(self):
        """
        Subscribe to new raw transactions. This method returns a generator that yields
        raw transactions as they are propagated by the network. Example result:

        (sender, rlp_transaction) = next(client.subscribe_new_raw_txs())

        sender is the sender's address.
        rlp_transaction is the raw transaction in RLP format.
        """

        return map(
            lambda proto: (proto.sender, proto.rlp_transaction),
            self.stub.SubscribeNewTxsV2(api_pb2.TxFilter(), metadata=self.metadata),
        )

    # def subscribe_new_execution_payloads(self):
    #     return map(
    #         lambda proto: proto_to_execution_payload(
    #             proto),
    #         self.stub.SubscribeExecutionPayloadsV2(
    #             empty, metadata=self.metadata),
    #     )

    # def subscribe_new_beacon_blocks(self):
    #     return map(
    #         lambda proto: proto_to_beacon_block(proto),a proto: proto_to_beacon_block(proto),  # TODO: change this
    #         self.stub.SubscribeBeaconBlocksV2(empty, metadata=self.metadata),
    #     )

    def subscribe_new_raw_beacon_blocks(self):
        """
        Subscribe to new raw beacon blocks. This method returns a generator that yields
        raw beacon blocks as they are propagated by the network. Example result:

        (data_version, ssz_block) = next(client.subscribe_new_raw_beacon_blocks())

        data_version is the fork number (e.g. 3 for Merge)
        """
        return map(
            lambda proto: (proto.data_version, proto.ssz_block),
            self.stub.SubscribeBeaconBlocksV2(empty, metadata=self.metadata),
        )

    def send_transaction(self, tx: Transaction):
        res = self.stub.SendTransaction(tx_to_proto(tx), metadata=self.metadata)
        return res.hash, res.timestamp

    def send_transaction_sequence(self, txs: list[Transaction]):
        res = self.stub.SendTransactionSequence(txs, metadata=self.metadata)
        return map(lambda sequence_response: sequence_response.hash, res), res[
            0
        ].timestamp

    def send_raw_transaction(self, tx: bytes):
        res = self.stub.SendRawTransaction(tx_to_proto(tx), metadata=self.metadata)
        return res.hash, res.timestamp

    def send_raw_transaction_sequence(self, txs: list[bytes]):
        res = self.stub.SendRawTransactionSequence(txs, metadata=self.metadata)
        return map(lambda sequence_response: sequence_response.hash, res), res[
            0
        ].timestamp
