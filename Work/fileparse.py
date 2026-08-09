# fileparse.py
#
# Exercise 3.3

from typing import Callable, Any

# Input: rows (comma separated), types, headers
# Output: List of dictionaries, each dictionary is header -> row value keyed (normalized to type)
def parse_csv(rows: list[list[str]], headers: list[str], types: list[Callable[..., Any]]) -> list[dict[str, Any]]:
    data = []
    for row in rows:
        record = { name: func(val) for name, func, val in zip(headers, types, row) }
        data.append(record)
    return data
