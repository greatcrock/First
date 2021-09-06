"""
In a given list the last element should become the first one.
An empty list or list with only one element should stay the same
"""

from collections import deque

def replace_last(line: list) -> list:
    d = deque(line)
    if len(d) != 0:
        d.appendleft(d.pop())
    return list(d)

print(replace_last([1, 2, 3, 4]))
print(replace_last([]))