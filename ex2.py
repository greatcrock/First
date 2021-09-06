"""In a given text you need to sum the numbers while excluding
any digits that form part of a word.
The text consists of numbers, spaces and letters from the English alphabet.
Input: A string.
Output: An int."""

def sum_numbers(text: str):
    nums = [int(i) for i in text.split() if i.isnumeric()]
    return sum(nums)


print(sum_numbers(''))