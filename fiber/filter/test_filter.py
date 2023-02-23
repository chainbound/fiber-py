import unittest
import json
from fiber.filter import filter

class TestFilter(unittest.TestCase):
    def test_or_filter(self):
        f = filter.Filter(filter.filter_or([filter.filter_to("0x1"), filter.filter_to("0x2")]))

        print(f.encode())

    def test_and_filter(self):
        f = filter.Filter(filter.filter_and([filter.filter_to("0x1"), filter.filter_to("0x2")]))

        print(f.encode())


if __name__ == '__main__':
    unittest.main()