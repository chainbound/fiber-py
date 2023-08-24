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

    def test_type_2_with_acl(self):
        type_2_with_acl_raw = "0x02f9040c0183012ec786023199fa3df88602e59652e99b8303851d9400000000003b3cc22af3ae1eac0440bcee416b4080b8530100d5a0afa68dd8cb83097765263adad881af6eed479c4a33ab293dce330b92aa52bc2a7cd3816edaa75f890b00000000000000000000000000000000000000000000007eb2e82c51126a5dde0a2e2a52f701f90344f9024994a68dd8cb83097765263adad881af6eed479c4a33f90231a00000000000000000000000000000000000000000000000000000000000000004a0745448ebd86f892e3973b919a6686b32d8505f8eb2e02df5a36797f187adb881a00000000000000000000000000000000000000000000000000000000000000003a00000000000000000000000000000000000000000000000000000000000000011a0a580422a537c1b63e41b8febf02c6c28bef8713a2a44af985cc8d4c2b24b1c86a091e3d6ffd1390da3bfbc0e0875515e89982841b064fcda9b67cffc63d8082ab6a091e3d6ffd1390da3bfbc0e0875515e89982841b064fcda9b67cffc63d8082ab8a0bf9ee777cf4683df01da9dfd7aeab60490278463b1d516455d67d23c750f96dca00000000000000000000000000000000000000000000000000000000000000012a0000000000000000000000000000000000000000000000000000000000000000fa00000000000000000000000000000000000000000000000000000000000000010a0a580422a537c1b63e41b8febf02c6c28bef8713a2a44af985cc8d4c2b24b1c88a0bd9bbcf6ef1c613b05ca02fcfe3d4505eb1c5d375083cb127bda8b8afcd050fba06306683371f43cb3203ee553ce8ac90eb82e4721cc5335d281e1e556d3edcdbca00000000000000000000000000000000000000000000000000000000000000013a0bd9bbcf6ef1c613b05ca02fcfe3d4505eb1c5d375083cb127bda8b8afcd050f9a00000000000000000000000000000000000000000000000000000000000000014f89b94ab293dce330b92aa52bc2a7cd3816edaa75f890bf884a0000000000000000000000000000000000000000000000000000000000000000ca00000000000000000000000000000000000000000000000000000000000000008a00000000000000000000000000000000000000000000000000000000000000006a00000000000000000000000000000000000000000000000000000000000000007f85994c02aaa39b223fe8d0a0e5c4f27ead9083c756cc2f842a051c9df7cdd01b5cb5fb293792b1e67ec1ac1048ae7e4c7cf6cf46883589dfbd4a03c679e5fc421e825187f885e3dcd7f4493f886ceeb4930450588e35818a32b9c80a020d7f34682e1c2834fcb0838e08be184ea6eba5189eda34c9a7561a209f7ed04a07c63c158f32d26630a9732d7553cfc5b16cff01f0a72c41842da693821ccdfcb"
        type_2_with_acl_decoded = decode_raw_transaction(type_2_with_acl_raw)
        type_2_with_acl_encoded = encode_transaction(type_2_with_acl_decoded)
        assert type_2_with_acl_raw == Web3.to_hex(type_2_with_acl_encoded)


if __name__ == '__main__':
    unittest.main()
