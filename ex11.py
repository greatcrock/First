"""
You are given two strings and you have to find an index of the second occurrence of the second string in the first one.
Let's go through the first example where you need to find the second occurrence of "s" in a word "sims".
It’s easy to find its first occurrence with a function index or find which will point out that "s" is the first symbol in a word "sims" and therefore the index of the first occurrence is 0.
But we have to find the second "s" which is 4th in a row and that means that the index of the second occurrence (and the answer to a question) is 3.

Input: Two strings.
Output: Int or None
"""

def second_index(text: str, symbol: str) -> [int, None]:
    if text.count(symbol) < 2:
        return None
    else:
        # parses the text and searchs the SECOND position of the SYMBOL. Than returns zero position in list (because there could me more than 1 satisfying symbols, like Hololo,
        # there index of o should be 3).
        return [pos for pos in range(len(text)) if pos != text.find(symbol) and text[pos] == symbol][0]

print(second_index("sims", "s"))