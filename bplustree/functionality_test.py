from __future__ import annotations

from pathlib import Path

import pytest
from beartype import beartype

from bplustree.const import TreeConf
from bplustree.memory import FileMemory
from bplustree.node import LeafNode
from bplustree.serializer import (
    IntSerializer,
)
from bplustree.tree import BPlusTree


@beartype
def test_create_and_load_file(tmp_path: Path):
    clean_file = tmp_path / "testfile.index"
    btree = BPlusTree(clean_file)
    assert isinstance(btree._mem, FileMemory)
    btree.insert(5, b"foo")
    btree.close()

    btree = BPlusTree(clean_file)
    assert isinstance(btree._mem, FileMemory)
    assert btree.get(5) == b"foo"
    btree.close()


@beartype
def test_insert_and_get(tmp_path: Path):
    clean_file = tmp_path / "testfile.index"
    btree = BPlusTree(clean_file, key_size=16, value_size=16, order=4)
    btree.insert(1, b"foo")
    assert btree.get(1) == b"foo"
    btree.close()


@beartype
def test_batch_insert(tmp_path: Path):
    clean_file = tmp_path / "testfile.index"
    btree = BPlusTree(clean_file, key_size=16, value_size=16, order=4)

    def generate(from_, to):
        for i in range(from_, to):
            yield i, str(i).encode()

    btree.batch_insert(generate(0, 1000))
    btree.batch_insert(generate(1000, 2000))

    i = 0
    for k, v in btree.items():
        assert k == i
        assert v == str(i).encode()
        i += 1
    assert i == 2000
    btree.close()


@beartype
def test_file_memory_node(tmp_path: Path):
    clean_file = tmp_path / "testfile.index"
    tree_conf = TreeConf(4096, 4, 16, 16, IntSerializer())
    node = LeafNode(tree_conf, page=3)
    mem = FileMemory(clean_file, tree_conf)

    with pytest.raises(FileMemory.ReachedEndOfFile):
        mem.get_node(3)

    mem.set_node(node)
