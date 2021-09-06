"""
In this mission you need to create a password verification function.
Those are the verification conditions:
the length should be bigger than 6;
should contain at least one digit, but it cannot consist of just digits;
if the password is longer than 9 - previous rule (about one digit), is not required.

Input: A string.
Output: A bool.
"""

def is_acceptable_password(password: str) -> bool:
    import re
    return True if len(password) >= 6 and ((len(password) >= 9) or re.match(r"[A-z]+[\d]+",password)) else False

print(is_acceptable_password("short54"))
print(is_acceptable_password("01234567"))
print(is_acceptable_password("asdfdfdasfasdf"))