"""You are given a string where you have to find its first word.
When solving a task pay attention to the following points:
There can be dots and commas in a string.
A string can start with a letter or, for example, a dot or space.
A word can contain an apostrophe and it's a part of a word.
The whole text can be represented with one word and that's it.

Input: A string.
Output: A string."""
def first_word(text: str) -> str:
    answ = ''
    for pos in range(len(text)):
        if text[pos].isalpha() or text[pos] == "'" :
            while (text[pos].isalpha() or text[pos] == "'"):
                answ += text[pos]
                pos += 1
                if pos == len(text):
                    break
            break
    return answ

print("Back", first_word("don"))
if " ".isalpha():
    print('Space')

