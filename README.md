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

The transaction stream is supported but without any filtering for now.
This stream yields [`fiber.types.Transaction`](/fiber/types.py#L9) objects.
All the bytes fields are encoded as hexadecimal strings.

```python
try:
  sub = client.subscribe_new_txs()

  # Iterate over transaction stream
  for tx in sub:
    do_something(tx)
except Exception as e:
  print("error subscribing", e)
```

### Subscribing to blocks

#### Execution Payload Headers

This stream yields only the new block headers as [`fiber.types.ExecutionPayloadHeader`](/fiber/types.py#L75) objects.
All the bytes fields are encoded as hexadecimal strings.

```python
try:
  sub = client.subscribe_new_execution_payload_headers()

  for header in sub:
    do_something(header)
except Exception as e:
  print("error subscribing", e)
```

#### Execution Payloads

This stream yields the new blocks as full [`fiber.types.ExecutionPayload`](/fiber/types.py#L94) objects.
All the bytes fields are encoded as hexadecimal strings.

```python
try:
  sub = client.subscribe_new_execution_payloads()

  for block in sub:
    do_something(block)
except Exception as e:
  print("error subscribing", e)
```

#### Beacon Blocks

This stream yields the blocks as seen by the Ethereum consensus layer, in the form of [`fiber.types.BeaconBlock`](/fiber/types.py#L211) objects. All the bytes fields are encoded as hexadecimal strings.

> **Note**
> Beacon blocks **do not** contain the execution payloads. To also get the execution payloads, please subscribe to the execution payload stream `subscribe_new_execution_payloads()` separately.

```python
try:
  sub = client.subscribe_new_beacon_blocks()

  for block in sub:
    do_something(block)
except Exception as e:
  print("error subscribing", e)
```
