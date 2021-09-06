"""
You have already learned how to count the amount of time a light bulb has been on, or how long a room has been lit.
Now let's add one more parameter - the counting start time.

This means that the light continues to turn on and off as before. But now, as a result of the function,
I want not only to know how long there was light in the room, but how long the room was lit, starting from a certain moment.

One more argument is added – start_watching , and if it’s not passed, we count as in the previous version of the program
for the entire period.
"""

"""
The array of pressing the button is always sorted in ascending order
The array of pressing the button has no repeated elements
The amount of elements is always even (the light will eventually be off)
The minimum possible date is 1970-01-01
The maximum possible date is 9999-12-31
"""

from datetime import datetime
from typing import List


def sum_light(els: List[datetime], start_watching=datetime(1970, 1, 1, 1, 1, 1), end_watching=datetime(9999,12,31,23,59,59) )-> int:
    """
        how long the light bulb has been turned on
    """
    ret = 0
    for x, y in zip(els[::2], els[1::2]):
        print(x, y)

        if x < start_watching < y:
            
            ret += (y - start_watching).total_seconds()
            print("Monry", ret)
        elif x >= start_watching:
            print("Meow", ret)
            ret += (y - x).total_seconds()
        else:
            print(ret)
            continue
    print(int(ret))
    return int(ret)


if __name__ == '__main__':
    print("Example:")
    print(sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_light(els=[
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
    ]) == 610

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ]) == 1220

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
        datetime(2015, 1, 12, 11, 10, 10),
        datetime(2015, 1, 12, 12, 10, 10),
    ]) == 4820

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 1),
    ]) == 1

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 13, 11, 0, 0),
    ]) == 86410

    print("The first mission in series is completed? Click 'Check' to earn cool rewards!")






if __name__ == "__main__":
    print("Example:")
    print(
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            datetime(2015, 1, 12, 10, 0, 5),
        )
    )

    assert (
            sum_light(
                els=[
                    datetime(2015, 1, 12, 10, 0, 0),
                    datetime(2015, 1, 12, 10, 0, 10),
                ],
                start_watching=datetime(2015, 1, 12, 10, 0, 5),
            )
            == 5
    )

    assert (
            sum_light(
                [
                    datetime(2015, 1, 12, 10, 0, 0),
                    datetime(2015, 1, 12, 10, 0, 10),
                ],
                datetime(2015, 1, 12, 10, 0, 0),
            )
            == 10
    )

    assert (
            sum_light(
                [
                    datetime(2015, 1, 12, 10, 0, 0),
                    datetime(2015, 1, 12, 10, 10, 10),
                    datetime(2015, 1, 12, 11, 0, 0),
                    datetime(2015, 1, 12, 11, 10, 10),
                ],
                datetime(2015, 1, 12, 11, 0, 0),
            )
            == 610
    )

    assert (
            sum_light(
                [
                    datetime(2015, 1, 12, 10, 0, 0),
                    datetime(2015, 1, 12, 10, 10, 10),
                    datetime(2015, 1, 12, 11, 0, 0),
                    datetime(2015, 1, 12, 11, 10, 10),
                ],
                datetime(2015, 1, 12, 11, 0, 10),
            )
            == 600
    )

    assert (
            sum_light(
                [
                    datetime(2015, 1, 12, 10, 0, 0),
                    datetime(2015, 1, 12, 10, 10, 10),
                    datetime(2015, 1, 12, 11, 0, 0),
                    datetime(2015, 1, 12, 11, 10, 10),
                ],
                datetime(2015, 1, 12, 10, 10, 0),
            )
            == 620
    )

    assert (
            sum_light(
                [
                    datetime(2015, 1, 12, 10, 0, 0),
                    datetime(2015, 1, 12, 10, 10, 10),
                    datetime(2015, 1, 12, 11, 0, 0),
                    datetime(2015, 1, 12, 11, 10, 10),
                    datetime(2015, 1, 12, 11, 10, 11),
                    datetime(2015, 1, 12, 12, 10, 11),
                ],
                datetime(2015, 1, 12, 12, 10, 11),
            )
            == 0
    )

    assert (
            sum_light(
                [
                    datetime(2015, 1, 12, 10, 0, 0),
                    datetime(2015, 1, 12, 10, 10, 10),
                    datetime(2015, 1, 12, 11, 0, 0),
                    datetime(2015, 1, 12, 11, 10, 10),
                    datetime(2015, 1, 12, 11, 10, 11),
                    datetime(2015, 1, 12, 12, 10, 11),
                ],
                datetime(2015, 1, 12, 12, 9, 11),
            )
            == 60
    )

    print("The second mission in series is done? Click 'Check' to earn cool rewards!")
