"""
For the input of your function, you will be given one sentence.
You have to return a corrected version, that starts with a capital letter and ends with a period (dot).
Pay attention to the fact that not all of the fixes are necessary.
If a sentence already ends with a period (dot), then adding another one will be a mistake.
"""

a = "fdasf"
print(a.capitalize())
def correct_sentence(text: str) -> str:
    """
        returns a corrected sentence which starts with a capital letter
        and ends with a dot.
    """
    # your code here
    if text[-1] not in "!.?":
        text += "."

    return text[0].capitalize()+text[1:]

print(correct_sentence("Hello, My dear"))