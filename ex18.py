"""
Your task is to decrypt the secret message using the Morse code .
The message will consist of words with 3 spaces between them and 1 space between each letter of each word.
If the decrypted text starts with a letter then you'll have to print this letter in uppercase.


Input: The secret message.
Output: The decrypted text.
"""

MORSE = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
}


def morse_decoder(code):
    line, w = "", ""
    while len(code) > 0:
        if code[0] != " ":
            w += code[0]
            code = code[1:]
        elif code[0] == " " and code[1] != " ":
            line += MORSE[w]
            w = ""
            code = code[1:]
        elif code[0] == code[1] == code[2] == " ":
            line += MORSE[w]
            w = ""
            line += " "
            code = code[3:]
    line += MORSE[w]
    return line.capitalize()

def morse_dedoder(code):
    txt = code.split(" " * 3)
    line = ""
    for word in txt:
        for letter in word.split():
            line += MORSE[letter]
        line += " "
    return line


print(morse_decoder("...   ---   ..."))

# These "asserts" using only for self-checking and not necessary for auto-testing
print(morse_decoder("... --- -- .   - . -..- -"))
print(morse_decoder("..--- ----- .---- ---.."))
morse_dedoder("... --- -- .   - . -..- -")
"""
 # if code[0] != " ":
        #     w += code[0]
        #     code = code[1:]
        # elif code[0] == " " and code[1] != " ":
        #     line += MORSE[w]
        #     w = ""
        #     code = code[1:]
        # elif code[0] == code[1] == code[2] == " ":
        #     line += MORSE[w]
        #     line += " "
        #     code = code[2:]
    # if w != "":
    #     line += MORSE[w]
    # return line
"""