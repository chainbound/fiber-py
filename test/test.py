from fiber.client import Client 

client = Client('beta.fiberapi.io:8080', 'test')
try:
  client.connect()
  print('Connected')

except Exception as e:
  print('Error connecting', e)


def do_something(tx):
  print(tx)

try:
  sub = client.subscribe_new_txs()

  # Iterate over transaction stream
  for tx in sub:
    do_something(tx)
except Exception as e:
  print("error subscribing", e)

