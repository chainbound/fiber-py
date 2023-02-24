# `fiber-py`

## Installation
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

### Filtering
The first argument to `subscribe_new_txs` is a filter, which can be empty if you want to get all transactions. A filter can be built with the filter package
```python
try:
  # Construct filter
  # example 1: all transactions with either of these addresses as the receiver
  f = filter.Filter(
          filter.filter_or([filter.filter_to("0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"), filter.filter_to("0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D")])
  )

  # example 2: all ERC20 transfers on the 2 tokens below
    f = filter.Filter(filter.filter_and(
        filter.method_id("0xa9059cbb"),
        filter.filter_or(
            filter.filter_to("0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"),
            filter.filter_to("0xdAC17F958D2ee523a2206206994597C13D831ec7"),
        ),
    ))
  
  sub = client.subscribe_new_txs(f)

  # Iterate over transaction stream
  for tx in sub:
    do_something(tx)
except Exception as e:
  print("error subscribing", e)
```
You can currently filter the following properties
* To
* From
* MethodID
* Value (greater than)

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

