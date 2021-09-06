"""
Sort the given iterable so that its elements end up in the decreasing frequency order, that is, the number of times they appear in elements.
If two elements have the same frequency, they should end up in the same order as the first appearance in the iterable.

Input: Iterable
Output: Iterable
"""

def frequency_sort(items):
    return sum([[k] * v for k, v in dict(sorted({x: items.count(x) for x in items}.items(), key=lambda item: -item[1])).items()],[])

print(frequency_sort([1,2,2,1, 1]))