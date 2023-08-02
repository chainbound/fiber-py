from fiber import eth_pb2
from fiber import api_pb2_grpc
from fiber import api_pb2
import grpc
import json

from eth_utils import decode_hex
from typing import Any

FILTER_AND = 0
FILTER_OR = 1

class FilterKv:
    key: str
    value: str

    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value


class Node:
    operand: FilterKv
    operator: int
    children: list

    def __init__(self, operand: int, operator: int, children: list):
        self.operand = operand
        self.operator = operator
        self.children = children

class Filter:
    root: Node

    def __init__(self, root: Node):
        self.root = root

    def encode(self) -> str:
        return json.JSONEncoder.encode(self)


def filter_and(ops: list) -> callable[[Filter, Node], None]:
    def f(f, n):
        new = {}

        if n == None:
            new = Node(None, FILTER_OR, None)

            f.root = new
        else:
            new = Node(None, FILTER_OR, None)

            n.children.append(new)

        for op in ops:
            op(f, n)

    return f

def filter_or(ops: list) -> callable[[Filter, Node], None]:
    def f(f, n):
        new = {}

        if n == None:
            new = Node(None, FILTER_AND, None)

            f.root = new
        else:
            new = Node(None, FILTER_AND, None)

            n.children.append(new)

        for op in ops:
            op(f, n)

    return f

def filter_to(to: str) -> callable[[Filter, Node], None]:
    def f (f, n):
        if n == None:
            f.root = Node(FilterKv("to", decode_hex(to)), None, None)
        else:
            n.children.append(Node(FilterKv("to", decode_hex(to)), None, None))

    return f

def filter_from(from_: str) -> callable[[Filter, Node], None]:
    def f (f, n):
        if n == None:
            f.root = Node(FilterKv("from", decode_hex(from_)), None, None)
        else:
            n.children.append(Node(FilterKv("from", decode_hex(from_)), None, None))

    return f

def method_id(id: str) -> callable[[Filter, Node], None]:
    def f (f, n):
        if n == None:
            f.root = Node(FilterKv("method_id", id), None, None)
        else:
            n.children.append(Node(FilterKv("method_id", id), None, None))

    return f

def filter_value(value: int) -> callable[[Filter, Node], None]:
    def f (f, n):
        if n == None:
            f.root = Node(FilterKv("value", str(value)), None, None)
        else:
            n.children.append(Node(FilterKv("value", str(value)), None, None))

    return f