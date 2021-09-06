"""
Maybe it's a cipher? Maybe, but we don’t know for sure.
Maybe you can call it "homomorphism" ? I wish I knew this word before.
You need to check that the 2 given strings are isometric.
This means that a character from one string can become a match for characters from another string.
One character from one string can correspond only to one character from another string.
Two or more characters of one string can correspond to one character of another string, but not vice versa.

Input: Two arguments. Both strings.
Output: Boolean.

Precondition:
both strings are the same length
"""


def isometric_strings(a, b):
    a1, b1 = "", ""
    for i in range(len(a)):
        if a[i] not in a1:
            a1 += a[i]
        if b[i] not in b1:
            b1 += b[i]
    worder = {a1[i] : b1[i] for i in range(len(a1))}
    for i in a:
        a = a.replace(i, worder[i])
    return a == b

#solution from the internet
def isometric_strings2(a,b):
        # your code here
    return len(set(a)) == len(set(zip(a, b)))
print(set(zip("ab", "ab")))
        # for letter in set(b)

        # your code here
print(isometric_strings2("add", "egg") == True)
print(isometric_strings2("foo", "bar"))
print(isometric_strings("", ""))
# assert isometric_strings("all", "all") == True
# assert isometric_strings("gogopy", "doodle") == False