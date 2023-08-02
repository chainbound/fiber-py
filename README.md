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

#### Execution Payload Headers (no transactions)

```python
try:
  sub = client.subscribe_new_execution_payload_headers()

  for header in sub:
    do_something(header)
except Exception as e:
  print("error subscribing", e)
```

**Header Type**
We export our own payload header type. All the bytes fields are encoded as hexadecimal strings.

```python
class ExecutionPayloadHeader:
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
    logs_bloom: bytes
    prev_randao: bytes
    receipt_root: bytes
    state_root: bytes
```

#### Execution Payloads (full blocks + transactions)

```python
try:
  sub = client.subscribe_new_execution_payloads()

  for block in sub:
    do_something(block)
except Exception as e:
  print("error subscribing", e)
```

**Payload Type**
We export our own payload type, which extends the header type above.

```python
class ExecutionPayload:
    header: ExecutionPayloadHeader
    transactions: list[Transaction]
```

#### Beacon Blocks

```python
try:
  sub = client.subscribe_new_beacon_blocks()

  for block in sub:
    do_something(block)
except Exception as e:
  print("error subscribing", e)
```

**Beacon Block Type**
For now, we don't export a custom BeaconBlock type, but you can rely on the protobuf definition
found in [`fiber/eth_pb2.pyi`](./fiber/eth_pb2.pyi). Feel free to open an issue or feature request if you need a custom type.
