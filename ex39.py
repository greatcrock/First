"""
In the previous mission, the start_watching parameter was introduced, and in this one - the end_watching parameter,
which tells the time when it’s necessary to end the observation.
If it’s not passed, the mission works as in the previous version, with no observation time limit.

One more update is that the amount of elements (button clicks) can be odd (previously there was a precondition, that the amount of elements is always even).


Input: Three arguments and only the first one is required. The first one is a list of datetime objects, the second and the third ones are the datetime objects.
Output: A number of seconds as an integer.

Precondition:
The array of pressing the button is always sorted in ascending order.
The array of pressing the button has no repeated elements.
The minimum possible date is 1970-01-01
The maximum possible date is 9999-12-31
"""



from datetime import datetime
from typing import List


def sum_light(els: List[datetime], start_watching=datetime(1970, 1, 1, 1, 1, 1),
              end_watching=datetime(9999, 12, 31, 23, 59, 59)) -> int:
    """
        how long the light bulb has been turned on
    """
    ret = 0
    for x, y in zip(els[::2], els[1::2]):
        if x < start_watching < y:
            x = start_watching
        elif y <= start_watching:
            y = x

        if x < end_watching < y:
            y = end_watching
        elif x >= end_watching:
            x = y
        ret += (y - x).total_seconds()
    if len(els) % 2 == 1:
        if els[-1] < end_watching:
            ret += (end_watching - els[-1]).total_seconds() if start_watching <= els[-1] \
                else (end_watching - start_watching).total_seconds()
    return int(ret)

print(sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
    ],
        datetime(2015, 1, 12, 11, 5, 0),
        datetime(2015, 1, 12, 11, 10, 0)) == 300)


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

if __name__ == '__main__':
    print("Example:")
    print(sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ],
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10)))

    assert sum_light(els=[
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ],
        start_watching=datetime(2015, 1, 12, 10, 0, 0),
        end_watching=datetime(2015, 1, 12, 10, 0, 10)) == 10

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ],
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 7)) == 7

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ],
        datetime(2015, 1, 12, 10, 0, 3),
        datetime(2015, 1, 12, 10, 0, 10)) == 7

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ],
        datetime(2015, 1, 12, 10, 0, 10),
        datetime(2015, 1, 12, 10, 0, 20)) == 0

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ],
        datetime(2015, 1, 12, 10, 30, 0),
        datetime(2015, 1, 12, 11, 0, 0)) == 0

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ],
        datetime(2015, 1, 12, 10, 10, 0),
        datetime(2015, 1, 12, 11, 0, 0)) == 10

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ],
        datetime(2015, 1, 12, 10, 10, 0),
        datetime(2015, 1, 12, 11, 0, 10)) == 20

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ],
        datetime(2015, 1, 12, 9, 50, 0),
        datetime(2015, 1, 12, 10, 0, 10)) == 10

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ],
        datetime(2015, 1, 12, 9, 0, 0),
        datetime(2015, 1, 12, 10, 5, 0)) == 300

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ],
        datetime(2015, 1, 12, 11, 5, 0),
        datetime(2015, 1, 12, 12, 0, 0)) == 310

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
    ],
        datetime(2015, 1, 12, 11, 5, 0),
        datetime(2015, 1, 12, 11, 10, 0)) == 300

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
    ],
        datetime(2015, 1, 12, 10, 10, 0),
        datetime(2015, 1, 12, 11, 0, 10)) == 20

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
    ],
        datetime(2015, 1, 12, 9, 10, 0),
        datetime(2015, 1, 12, 10, 20, 20)) == 610

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
    ],
        datetime(2015, 1, 12, 9, 10, 0),
        datetime(2015, 1, 12, 10, 20, 20)) == 1220

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
    ],
        datetime(2015, 1, 12, 9, 9, 0),
        datetime(2015, 1, 12, 10, 0, 0)) == 0

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
    ],
        datetime(2015, 1, 12, 9, 9, 0),
        datetime(2015, 1, 12, 10, 0, 10)) == 10

    print("The third mission in series is completed? Click 'Check' to earn cool rewards!")