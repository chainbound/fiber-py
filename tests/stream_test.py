# Test the Fiber stream functionality of the client.
# 
# In order to run this test, you need to provide your working API key 
# as an environment variable, like so:
#
# FIBER_TEST_KEY=<your_key> python tests/stream_test.py


import os
import unittest
from fiber.client import Client 

key = os.getenv("FIBER_TEST_KEY")
client = Client('beta.fiberapi.io:8080', key)

class StreamTest(unittest.TestCase):
  def test_tx_stream(self):
    try:
      client.connect()
      print('Connected')

    except Exception as e:
      print('Error connecting: ', e)

    try:
      sub = client.subscribe_new_txs()
      print('Subscribed')

      i = 0
      for tx in sub:
        print(tx.hash)
        # optionally print the RLP-encoded transaction hex:
        print(tx.to_rlp_hex(), "\n")

        i += 1
        if i == 10:
          break

    except Exception as e:
      print("error subscribing: ", e)


if __name__ == '__main__':
    unittest.main()
