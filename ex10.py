"""
In this mission your task is to determine the popularity of certain words in the text.

At the input of your function are given 2 arguments: the text and the array of words the popularity of which you need to determine.

When solving this task pay attention to the following points:
The words should be sought in all registers. This means that if you need to find a word "one" then words like "one", "One", "oNe", "ONE" etc. will do.
The search words are always indicated in the lowercase.
If the word wasn’t found even once, it has to be returned in the dictionary with 0 (zero) value.

Input: The text and the search words array.
Output: The dictionary where the search words are the keys and values are the number of times when those words are occurring in a given text.
"""

f = ["abc", "cbs", "lemon"]
dim = {}
for i in f:
    dim[i] = 0
print(dim)
for k in dim:
    for i in f:
        if i == k:
            dim[k] += 1
print(dim)

# my solution:
def popular_words(text: str, words: list) -> dict:
    freqs = {}
    for i in words:
        freqs[i] = 0
    text = text.split()

    for word in  text:
        for key in freqs:
            if key == word.lower():
                freqs[key] += 1
    return freqs


print(popular_words("When I was One I had just begun When I was Two I was nearly new", ['i', 'was', 'three', 'near']))

# slotuin from the internet:
def popular_words(text: str, words: list) -> dict:
    text = text.lower().split()
    return {w: text.count(w) or 0 for w in words}