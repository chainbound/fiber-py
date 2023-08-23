import unittest
from web3 import Web3

from fiber.rlp import decode_raw_transaction, encode_transaction


class RlpTest(unittest.TestCase):

    def test_type_0_pre_eip_155(self):
        type_0_pre_155_raw = "0xf8ac82026685065cde23c48301a70494d26114cd6ee289accf82350c8d8487fedb8a0c0780b844a9059cbb000000000000000000000000bb2645925f6310a245da8a72dbe4f69fe132055b000000000000000000000000000000000000000000000021583a2f0f7ec600001ca078118f77f0bb3f65ee8d31628aec113de7518ad5300aeea7737297805ec2cffca04334754c4a6065dfecc190a57a11be3fde35269ec03227326787c607d52c6d7d"
        type_0_pre_155_decoded = decode_raw_transaction(type_0_pre_155_raw)
        type_0_pre_155_encoded = encode_transaction(type_0_pre_155_decoded)
        assert type_0_pre_155_raw == Web3.to_hex(type_0_pre_155_encoded)

    def test_type_0_post_eip_155(self):
        type_0_post_155_raw = "0xf86e823795851ebbd0280082520894b411d9ebf77eb2b5e08eabeefc1f2d8b7dc5208988017896703a3100008026a06fa3645fcee44bbd22ed22526bdfa1572d50b593ad0d5a683da89156e434ab7ba040888b027df45539a56b7b7d58dd14dd0efeda6f3d61d5e34849b3d30d9699ea"
        type_0_post_155_decoded = decode_raw_transaction(type_0_post_155_raw)
        type_0_post_155_encoded = encode_transaction(type_0_post_155_decoded)
        assert type_0_post_155_raw == Web3.to_hex(type_0_post_155_encoded)

    def test_type_1(self):
        # type_1_raw = ""
        # type_1_decoded = decode_raw_transaction(type_1_raw)
        # type_1_encoded = encode_transaction(type_1_decoded)
        # assert type_1_raw == Web3.to_hex(type_1_encoded)
        pass

    def test_type_2(self):
        type_2_raw = "0x02f90135013b8402faf080850358f86d6b8303ebde941111111254fb6c44bac0bed2854e76f90643097d80b8c82e95b6c8000000000000000000000000dac17f958d2ee523a2206206994597c13d831ec700000000000000000000000000000000000000000000000000000000012edb3b000000000000000000000000000000000000000000000000002a93ef5a66546800000000000000000000000000000000000000000000000000000000000000800000000000000000000000000000000000000000000000000000000000000001c0000000000000003b6d034006da0fd433c1a5d7a4faa01111c044910a184553f012a792c001a06773e8d08a522eadd804dc0382fb04d098e1ea38e46aced04650230c2708b4eca034740575eb91ada517a2cd4b4e46ed6e3374c8d82a6c30b4aedb615fd81b3c25"
        type_2_decoded = decode_raw_transaction(type_2_raw)
        type_2_encoded = encode_transaction(type_2_decoded)
        assert type_2_raw == Web3.to_hex(type_2_encoded)


if __name__ == '__main__':
    unittest.main()
