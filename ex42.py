"""
You prefer a good old 12-hour time format. But the modern world we live in would rather use the 24-hour format and you see it everywhere. Your task is to convert the time from the 24-h format into 12-h format by following the next rules:
- the output format should be 'hh:mm a.m.' (for hours before midday) or 'hh:mm p.m.' (for hours after midday)
- if hours is less than 10 - don't write a '0' before it. For example: '9:05 a.m.'
Here you can find some useful information about the 12-hour format .

example

Input: Time in a 24-hour format (as a string).

Output: Time in a 12-hour format (as a string).

Precondition :
'00:00' <= time <= '23:59'
"""

def time_converter(time):
    h, m = time.split(":")
    h = int(h)
    return f"{h % 12 if h != 12 and h != 0 else 12}:{m} {'p.m.' if int(h) >= 12 else 'a.m.'}"


# solution from the internet:
def time_converter_cpied(time):

     return f"{(h:=int(time[:2]))%12 or 12}{time[2:]} {'p' if h>11 else 'a'}.m."


if __name__ == '__main__':
    print("Example:")
    print(time_converter('11:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")

a = "."
print("".join([str(i) for i in range(len(input()))]))
if a.isalpha():
    print(a)