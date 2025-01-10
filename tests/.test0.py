import uuid
from pathlib import Path

from bplustree import BPlusTree

path = Path(__file__).parent / f"tmp/test_{str(uuid.uuid4())[:8]}.bpt"
tree = BPlusTree(path, key_size=16, value_size=16, cache_size=0)

key = int(uuid.uuid4())
value = uuid.uuid4().bytes
print(f"Inserting key: {key}, value: {value}")

tree.insert(key, value)

# Retrieve the value
retrieved_value = tree.get(key)
print(f"Retrieved value: {retrieved_value}")
assert retrieved_value == value, f"Expected {value}, got {retrieved_value}"

tree.close()
