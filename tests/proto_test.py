import unittest
from web3 import Web3
from fiber.proto import api_pb2

from fiber.types import hex_to_bytes, proto_to_tx


class ProtoTest(unittest.TestCase):

    def test_type_2_proto_to_tx(self):
        type_2_raw_tx = "0x02f90135013b8402faf080850358f86d6b8303ebde941111111254fb6c44bac0bed2854e76f90643097d80b8c82e95b6c8000000000000000000000000dac17f958d2ee523a2206206994597c13d831ec700000000000000000000000000000000000000000000000000000000012edb3b000000000000000000000000000000000000000000000000002a93ef5a66546800000000000000000000000000000000000000000000000000000000000000800000000000000000000000000000000000000000000000000000000000000001c0000000000000003b6d034006da0fd433c1a5d7a4faa01111c044910a184553f012a792c001a06773e8d08a522eadd804dc0382fb04d098e1ea38e46aced04650230c2708b4eca034740575eb91ada517a2cd4b4e46ed6e3374c8d82a6c30b4aedb615fd81b3c25"
        sender = "0x03ebde941111111254fb6c44bac0bed2854e76f9"

        proto_tx = api_pb2.TransactionWithSenderMsg(rlp_transaction=hex_to_bytes(
            type_2_raw_tx), sender=hex_to_bytes(sender))

        decoded = proto_to_tx(proto_tx)

        assert decoded.gas == 256990
        assert decoded.nonce == 59
        assert decoded.sender == sender

    def test_type_3_proto_to_tx(self):
        # sepolia tx: https://sepolia.etherscan.io/tx/0x49875d037b17fb256f7487a14b333c09a2bfb676912a61c4a859b27cd55b449e
        type_3_raw_tx = "0x03f89783aa36a782f1b0843b9aca00850137764d5282520894ff000000000000000000000000000000000742488080c0843b9aca00e1a001c1bc7a568ba0304b38ac6309683ad8baed24a58abce77259b8b28da34f29f901a0c1e8fd7ddca057a91cc719c282e63b51f30008b49e0d8e4a6d3bc5d0ec30869fa05ffb393318c9dc9fadcef32f6aede2476a3627a23d465b3ee9c0462c02eea329"
        sender = "0x4e6bA705D14b2237374cF3a308ec466cAb24cA6a"
        hash = "0x49875d037b17fb256f7487a14b333c09a2bfb676912a61c4a859b27cd55b449e"

        proto_tx = api_pb2.TransactionWithSenderMsg(rlp_transaction=hex_to_bytes(
            type_3_raw_tx), sender=hex_to_bytes(sender))

        decoded = proto_to_tx(proto_tx)

        assert decoded.gas == 21000
        assert decoded.nonce == 61872
        assert decoded.sender.lower() == sender.lower()
        assert decoded.hash.lower() == hash.lower()
        assert decoded.max_fee_per_blob_gas == 1000000000
        assert decoded.blob_versioned_hashes[0] == "0x01c1bc7a568ba0304b38ac6309683ad8baed24a58abce77259b8b28da34f29f9"


if __name__ == '__main__':
    unittest.main()
