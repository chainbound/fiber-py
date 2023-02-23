# `fiber-py`

## Installation
With Poetry:
```
poetry add git+https://github.com/chainbound/fiber-py
```

## Usage
### Connecting
```python
client = Client('FIBER_ENDPOINT', 'YOUR_API_KEY')
try:
  client.connect()
except Exception as e:
  print('Error connecting', e)
```

### Subscribing to transactions
```python
try:
  sub = client.subscribe_new_txs()

  for tx in sub:
    do_something(tx)
except Exception as e:
  print("error subscribing", e)
```
