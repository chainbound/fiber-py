import unittest
from fiber.proto import api_pb2

from fiber.types import bytes_to_hex, hex_to_bytes, proto_to_tx


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

    def test_type_4_proto_to_tx(self):
        # odyssey tx: https://odyssey-explorer.ithaca.xyz/tx/0x6d0d0adbe21d4a523352dbd7f1d4bd118a5c9c291f05e54a0f4ffe0a537702c2?tab=index
        # obtained with: cast tx --rpc-url https://odyssey.ithaca.xyz 0x6d0d0adbe21d4a523352dbd7f1d4bd118a5c9c291f05e54a0f4ffe0a537702c2 --raw
        type_4_raw_tx = "0x04f901b1830de9fb8305dc3d018201f98302ec1b94a804a866ba73d07fd97afbbaf9b0ba20143d79e780b8e4a78fc244186d27c797d4359bf894fe0f0364e58f52a4fca41431cdbca0277f03ade81fe5c525416d3c0adbb3a701ca0ce648df967e3f5daaffce919e7538126e2c52a63600000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000607c5ce18e9b970e62c6030267bd547a8d199ce3765a55f3ab575a8935b373ee3b9e86dd04ba997b710582dcededeecbba05656b5c1254ec24574a18540a5f9c0000000000000000000000000000000000000000000000000000000000000001c0f85ff85d830de9fb9435202a6e6317f3cc3a177eeee562d3bcda4a6fcc8001a090cfc482b99208b4dbd7b62891df4259b8a69f1a875ad17829a62d19b549db40a03a377a348e1be92ec9ade2f5a6d587ba431274197182ea30aacd1323ac21404c01a0046725636e08deb390f02568562c78952a564506d92150f5effcd69be1502f13a05b0c6a789951b5ce89a0e70b443ce8dd79d013e8ed6b3dd6904343f93df2a164"
        sender = "0x1234562C27E07675Fe8ed90BbFB9a62853edCBb2"
        hash = "0x6d0d0adbe21d4a523352dbd7f1d4bd118a5c9c291f05e54a0f4ffe0a537702c2"

        proto_tx = api_pb2.TransactionWithSenderMsg(
            rlp_transaction=hex_to_bytes(type_4_raw_tx), sender=hex_to_bytes(sender))

        decoded = proto_to_tx(proto_tx)

        assert decoded.gas == 191515
        assert decoded.nonce == 384061
        assert decoded.sender.lower() == sender.lower()
        assert decoded.hash.lower() == hash.lower()
        assert len(decoded.authorization_list) == 1

        # source of truth:
        #
        # authorizationList: [{"chainId":"0xde9fb","address":"0x35202a6e6317f3cc3a177eeee562d3bcda4a6fcc",
        #     "nonce":"0x0","yParity":"0x1",
        #     "r":"0x90cfc482b99208b4dbd7b62891df4259b8a69f1a875ad17829a62d19b549db40",
        #     "s":"0x3a377a348e1be92ec9ade2f5a6d587ba431274197182ea30aacd1323ac21404c"
        #   }]

        assert decoded.authorization_list[0][0] == 911_867
        assert "0x" + bytes_to_hex(decoded.authorization_list[0][1]).lower(
        ) == "0x35202a6e6317f3cc3a177eeee562d3bcda4a6fcc".lower()
        assert decoded.authorization_list[0][2] == 0
        assert decoded.authorization_list[0][3] == 1


if __name__ == '__main__':
    unittest.main()
