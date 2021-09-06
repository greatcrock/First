"""
Nicola has solved this puzzle (and I am sure that you will do equally well).
To be prepared for more such puzzles, Nicola wants to invent a method to search for words inside poetry.
You can help him create a function to search for certain words.

You are given a rhyme (a multiline string), in which lines are separated by "newline" (\n).
Casing does not matter for your search, but whitespaces should be removed before your search.
You should find the word inside the rhyme in the horizontal (from left to right) or vertical (from up to down) lines.
For this you need envision the rhyme as a matrix (2D array).

Find the coordinates of the word in the cut rhyme (without whitespaces).
"""

"""
The result must be represented as a list -- [row_start,column_start,row_end,column_end] , where

row_start is the line number for the first letter of the word.
column_start is the column number for the first letter of the word.
row_end is the line number for the last letter of the word.
column_end is the column number for the last letter of the word.
Counting of the rows and columns start from 1.
"""

print(list(enumerate("hello")))
def checkio(text, word):
    txt = [i.replace("#", "").replace(" ", "").lower() for i in text.split("\n")]

    # makes all lines equal by using "."
    for i in range(len(txt)):
        while len(txt[i]) < len(max(txt)):
            txt[i] += "."

    # horizontal checking
    for i in txt:
        if word in i.lower():
            return [txt.index(i) + 1, i.index(word) + 1, txt.index(i) + 1, i.index(word) + len(word)]

    # vertical checking
    temp = list(zip(*txt))
    for i in temp:
        if word in "".join(i):
            return ["".join(i).index(word)+1, temp.index(i) + 1, "".join(i).index(word) + len(word), temp.index(i) + 1]


# Solution from the internet:
def checkio_copied(text, word):
    text = text.replace(" ","").lower().split('\n')

    cols = ['']*300
    for i, line in enumerate(text):
        if word in line:
            return [i+1, line.index(word)+1, i+1, line.index(word) + len(word)]
        for j, c in enumerate(line):
            cols[j] += c
            if word in cols[j]:
                return [i-len(word)+2, j+1, i+1, j+1]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ten") == [2, 14, 2, 16]
    assert checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]
print("Coding complete? Click 'Check' to earn cool rewards!")

print(11 % 12)