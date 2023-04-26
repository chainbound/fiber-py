# `fiber-py`

## Installation
With pip:
```
pip install git+https://github.com/chainbound/fiber-py
```
With Poetry:
```
poetry add git+https://github.com/chainbound/fiber-py
```

## Usage
### Connecting
```python
from fiber.client import Client 

client = Client('FIBER_ENDPOINT', 'YOUR_API_KEY')
try:
  client.connect()
except Exception as e:
  print('Error connecting', e)
```

### Subscribing to transactions
The transaction stream is supported but without any filtering for now. `subscribe_new_txs`
returns a stream of `fiber.client.Transaction`, shown below.
```python
try:
  sub = client.subscribe_new_txs()

  # Iterate over transaction stream
  for tx in sub:
    do_something(tx)
except Exception as e:
  print("error subscribing", e)
```

**Transaction type**:
We export our own transaction type. All the bytes fields are encoded as hexadecimal strings.
```python
class Transaction:
  to: str
  gas: int
  hash: str
  nonce: int
  value: int
  sender: str
  type: int
  gas_price: int
  input: str
  max_fee: int
  priority_fee: int
  v: int
  r: str
  s: str
  access_list: Any
  chain_id: int
```

### Subscribing to blocks
```python
try:
  sub = client.subscribe_new_blocks()

  for block in sub:
    do_something(block)
except Exception as e:
  print("error subscribing", e)
```

**Block Type**
We export our own block type. All the bytes fields are encoded as hexadecimal strings.
```python
class Block:
    hash: str
    number: int
    parent_hash: str
    timestamp: int
    producer: str
    base_fee_per_gas: int
    extra_data: str
    fee_recipient: str
    gas_limit: int
    gas_used: int
    logs_bloom: str
    prev_randao: str
    receipt_root: str
    state_root: str
    transactions: list[Transaction]
```

### Subscribing to headers
```python
try:
  sub = client.subscribe_new_headers()

  for header in sub:
    do_something(header)
except Exception as e:
  print("error subscribing", e)
```

**Header Type**
We export our own header type, which is identical to the block type seen above minus the transactions field. All the bytes fields are encoded as hexadecimal strings.

