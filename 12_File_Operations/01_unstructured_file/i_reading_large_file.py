#!/usr/bin/python3
"""
Purpose: To read large file
"""
from functools import partial
from typing import Iterator

def read_from_file(file_name: str) -> Iterator:
    """Method 1 - reading one line per iteration"""
    with open(file_name, "r") as fp:
        yield fp.readline()


def read_from_file2(file_name: str, block_size: int=1024 * 8) ->Iterator:
    """Method 2 - reading block size per iteration"""
    with open(file_name, "r") as fp:
        while True:
            chunk = fp.read(block_size)
            if not chunk:
                break
            yield chunk


def read_from_file3(file_name: str, block_size: int=1024 * 8) -> Iterator:
    """Method 3 - reading block size per iteration (clean code)"""
    with open(file_name, "r") as fp:
        for chunk in iter(partial(fp.read, block_size), ""):
            yield chunk


# Assignment -- use these functions on large datasets (download from opendata)