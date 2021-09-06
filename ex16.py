"""
In this mission you should check if all elements in the given list are equal.

Input: List.
Output: Bool.
"""
from typing import List, Any

a = [1] * 3
print(a)
b = [1,2,3]
c = [b[0]] * len(b)
if c == a:
    print('Ow')
print(c)
print()
def all_the_same(elements: List[Any]) -> bool:
    # creates additional list, which consits of copies of 1 element from given list, then compares them.
    return True if len(elements) <= 1 or ([elements[0]] * len(elements) == elements) else False
print(all_the_same([1, 1]))
# another solution
def all_the_same(elements: List[Any]) -> bool:
    # creates additional list, which consits of copies of 1 element from given list, then compares them.
    return len(set(elements)) < 2
