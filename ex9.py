"""
You are given a non-empty list of integers (X). For this task, you should return a list consisting of only the non-unique elements in this list.
To do so you will need to remove all unique elements (elements which are contained in a given list only once).
When solving this task, do not change the order of the list. Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements and result will be [1, 3, 1, 3].

non-unique-elements

Input: A list of integers.
Output: An iterable of integers.
"""

def checkio(data: list) -> list:
    answ = [i for i in data if data.count(i) == 1]
    return answ
print(checkio([1,2,4,5,6,7,7,7]))