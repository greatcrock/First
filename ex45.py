def checkio(line1: str, line2: str) -> str:
    # your code here
    return ",".join(sorted([i for i in line2.split(",") if i in line1.split(",")]))

print(checkio('one,two,three',
 'four,five,one,two,six,three'))
if __name__ == '__main__':
    print("Example:")
    print(checkio('hello,world', 'hello,earth'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert checkio('hello,world', 'hello,earth') == 'hello'
    assert checkio('one,two,three', 'four,five,six') == ''
    assert checkio('one,two,three',
 'four,five,one,two,six,three') == 'one,three,two'
    print("Coding complete? Click 'Check' to earn cool rewards!")


def check_pangram(text):
    '''
        is the given text is a pangram.
    '''
    # your code here
    alphabet = set([chr(i) for i in range(ord('a'), ord("z") + 1)])
    text = set([i for i in text.lower()])
    return len(alphabet.difference(text)) == 0
txt = "The quick brown fox jumps over the lazy dog."
print(check_pangram(txt))
beta = set([i for i in txt])
print(beta)
alpha = set([chr(i) for i in range(ord('a'), ord("z") + 1)])
print(alpha)
a = {"a", 'b', 'c'}
b = {'a', 'b'}
print(len(alpha.difference(beta)))