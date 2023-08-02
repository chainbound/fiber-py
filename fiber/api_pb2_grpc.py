# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import api_pb2 as api__pb2
import eth_pb2 as eth__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class APIStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SubscribeNewTxs = channel.unary_stream(
                '/api.API/SubscribeNewTxs',
                request_serializer=api__pb2.TxFilter.SerializeToString,
                response_deserializer=eth__pb2.Transaction.FromString,
                )
        self.SendTransaction = channel.stream_stream(
                '/api.API/SendTransaction',
                request_serializer=eth__pb2.Transaction.SerializeToString,
                response_deserializer=api__pb2.TransactionResponse.FromString,
                )
        self.SendRawTransaction = channel.stream_stream(
                '/api.API/SendRawTransaction',
                request_serializer=api__pb2.RawTxMsg.SerializeToString,
                response_deserializer=api__pb2.TransactionResponse.FromString,
                )
        self.SendTransactionSequence = channel.stream_stream(
                '/api.API/SendTransactionSequence',
                request_serializer=api__pb2.TxSequenceMsg.SerializeToString,
                response_deserializer=api__pb2.TxSequenceResponse.FromString,
                )
        self.SendRawTransactionSequence = channel.stream_stream(
                '/api.API/SendRawTransactionSequence',
                request_serializer=api__pb2.RawTxSequenceMsg.SerializeToString,
                response_deserializer=api__pb2.TxSequenceResponse.FromString,
                )
        self.SubscribeExecutionPayloads = channel.unary_stream(
                '/api.API/SubscribeExecutionPayloads',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=eth__pb2.ExecutionPayload.FromString,
                )
        self.SubscribeExecutionHeaders = channel.unary_stream(
                '/api.API/SubscribeExecutionHeaders',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=eth__pb2.ExecutionPayloadHeader.FromString,
                )
        self.SubscribeBeaconBlocks = channel.unary_stream(
                '/api.API/SubscribeBeaconBlocks',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=eth__pb2.CompactBeaconBlock.FromString,
                )


class APIServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SubscribeNewTxs(self, request, context):
        """Opens a new transaction stream with the given filter.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendTransaction(self, request_iterator, context):
        """Sends a signed transaction to the network.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendRawTransaction(self, request_iterator, context):
        """Sends a signed, RLP encoded transaction to the network
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendTransactionSequence(self, request_iterator, context):
        """Sends a sequence of signed transactions to the network.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendRawTransactionSequence(self, request_iterator, context):
        """Sends a sequence of signed, RLP encoded transactions to the network.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeExecutionPayloads(self, request, context):
        """Opens a stream of new execution payloads.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeExecutionHeaders(self, request, context):
        """Opens a stream of new execution payload headers.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeBeaconBlocks(self, request, context):
        """Opens a stream of new beacon blocks. The beacon blocks are "compacted", meaning that the
        execution payload is not included.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_APIServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SubscribeNewTxs': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeNewTxs,
                    request_deserializer=api__pb2.TxFilter.FromString,
                    response_serializer=eth__pb2.Transaction.SerializeToString,
            ),
            'SendTransaction': grpc.stream_stream_rpc_method_handler(
                    servicer.SendTransaction,
                    request_deserializer=eth__pb2.Transaction.FromString,
                    response_serializer=api__pb2.TransactionResponse.SerializeToString,
            ),
            'SendRawTransaction': grpc.stream_stream_rpc_method_handler(
                    servicer.SendRawTransaction,
                    request_deserializer=api__pb2.RawTxMsg.FromString,
                    response_serializer=api__pb2.TransactionResponse.SerializeToString,
            ),
            'SendTransactionSequence': grpc.stream_stream_rpc_method_handler(
                    servicer.SendTransactionSequence,
                    request_deserializer=api__pb2.TxSequenceMsg.FromString,
                    response_serializer=api__pb2.TxSequenceResponse.SerializeToString,
            ),
            'SendRawTransactionSequence': grpc.stream_stream_rpc_method_handler(
                    servicer.SendRawTransactionSequence,
                    request_deserializer=api__pb2.RawTxSequenceMsg.FromString,
                    response_serializer=api__pb2.TxSequenceResponse.SerializeToString,
            ),
            'SubscribeExecutionPayloads': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeExecutionPayloads,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=eth__pb2.ExecutionPayload.SerializeToString,
            ),
            'SubscribeExecutionHeaders': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeExecutionHeaders,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=eth__pb2.ExecutionPayloadHeader.SerializeToString,
            ),
            'SubscribeBeaconBlocks': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeBeaconBlocks,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=eth__pb2.CompactBeaconBlock.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.API', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class API(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SubscribeNewTxs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/api.API/SubscribeNewTxs',
            api__pb2.TxFilter.SerializeToString,
            eth__pb2.Transaction.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendTransaction(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/api.API/SendTransaction',
            eth__pb2.Transaction.SerializeToString,
            api__pb2.TransactionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendRawTransaction(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/api.API/SendRawTransaction',
            api__pb2.RawTxMsg.SerializeToString,
            api__pb2.TransactionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendTransactionSequence(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/api.API/SendTransactionSequence',
            api__pb2.TxSequenceMsg.SerializeToString,
            api__pb2.TxSequenceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendRawTransactionSequence(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/api.API/SendRawTransactionSequence',
            api__pb2.RawTxSequenceMsg.SerializeToString,
            api__pb2.TxSequenceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeExecutionPayloads(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/api.API/SubscribeExecutionPayloads',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            eth__pb2.ExecutionPayload.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeExecutionHeaders(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/api.API/SubscribeExecutionHeaders',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            eth__pb2.ExecutionPayloadHeader.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeBeaconBlocks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/api.API/SubscribeBeaconBlocks',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            eth__pb2.CompactBeaconBlock.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
