from math import pi, pow, ceil
from string import ascii_uppercase, digits

NUMBERS = digits + ascii_uppercase

import pytest

def converter(n, decimals=0, base=pi):
    """takes n in base 10 and returns it in any base (default is pi
    with optional x decimals"""
    #your code here

    sum = 0
    quo = n
    lst = []
    while True:
        quo, rem = int(quo / base), quo % base
        lst.append(rem)
        if quo < base:
            lst.append(quo)
            break

    # if n == pi: pytest.set_trace()

    print(lst)

    ret_str = [NUMBERS[ceil(i)] for i in lst[::-1]]
    print(ret_str)

    return ''.join(ret_str)


@pytest.mark.parametrize("a,decimals,base,expected",
                         [
                              (13, 0, 2, "1101"),
                              (13, 0, 8, "15"),
                              (1334, 0, 8, "2466"),
                              (1334, 0, 16, "536"),
                              (13, 0, pi, "103"),
                             (pi, 0, pi, "10")
                          ])
def test_converter(a,decimals,base,expected):
    assert converter(a, decimals, base) == expected
