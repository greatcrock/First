"""
In this mission you need to create a password verification function.

Those are the verification conditions:

the length should be bigger than 6;
should contain at least one digit, but it cannot consist of just digits;
having numbers or containing just numbers does not apply to the password longer than 9.
a string should not contain the word "password" in any case;
should contain 3 different letters (or digits) even if it is longer than 10

Input: A string.
Output: A bool.
"""


def is_acceptable_password(password: str) -> bool:
    if len(password) >= 6 and "password" not in password.lower() and len(set(password)) >= 3:
        if len([i for i in password if i.isdigit()]) in range(1, len(password)):
            return True
        elif len(password) >= 9:
            return len([i for i in set(password) if i.isdigit() or i.isalpha()]) >= 3
        else:
            return False
    else:
        return False




#def is_acceptable_password(password: str) -> bool:
#    import re

#    return True if (len(password) >= 6 and ((len(password) >= 9) or re.match(r"[A-z]+[\d]+",password)) and "password" not in password.lower()) else False
