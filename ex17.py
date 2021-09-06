"""
Computer date and time format consists only of numbers, for example: 21.05.2018 16:30
Humans prefer to see something like this: 21 May 2018 year, 16 hours 30 minutes
Your task is simple - convert the input date and time from computer format into a "human" format.

Input: Date and time as a string
Output: The same date and time, but in a more readable format
"""

# date_time("19.09.2999 01:59") == "19 September 2999 year 1 hour 59 minutes"
# date_time("21.10.1999 18:01") == "21 October 1999 year 18 hours 1 minute"
# NB: words "hour" and "minute" are to be used only when time is 01:mm (1 hour) or hh:01 (1 minute).
# In other cases "hours" and "minutes" should be used.

def date_time(time: str):
    day, time = time.strip().split()
    m = ["January", "February",
         "March", "April", "May",
         "June", "July", "August",
         "September", "October", "November",
         "December"]
    day, month, year = map(int, day.split("."))
    month -= 1
    hours, minutes = map(int, time.split(":"))
    return f"{day} {m[month - 1]} {year} year {hours} {'hour' if hours == 1 else 'hours'} {minutes} {'minute' if minutes == 1 else'minutes'}"




print(date_time("12.2.2000 00:00"))
