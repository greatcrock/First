"""
In a given string you should reverse every word, but the words should stay in their places.

Input: A string.
Output: A string.
"""

def backward_string_by_word(text: str) -> str:
    # your code here
    answ = ''
    temp_w = ''
    for i in range(len(text)):
        if text[i] == " ":
            answ += text[i]
        else:
            temp_w += text[i]
            if i == len(text) - 1 or text[i + 1] == " ":
                for symbol in temp_w[::-1]:
                    answ += symbol
                temp_w = ""
    return answ

print(backward_string_by_word("Hel           lo").rstrip())
print("a  b".split())