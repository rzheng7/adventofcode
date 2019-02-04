# https://www.codewars.com/kata/are-they-the-same

import pytest

def same(l1, l2):

    if l1 is None or l2 is None:
        return False

    sq_l1 = list(map(lambda x : x*x, l1))

    return sorted(sq_l1)  == sorted(l2)


@pytest.mark.parametrize("a,b, expected", [
    ([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 361, 25921, 361, 20736, 361], True),
    ([], [], True),
    (None, [], False),
    ([121, 144, 19, 161, 19, 144, 19, 11], [132, 14641, 20736, 361, 25921, 361, 20736, 361], False),
    ([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 36100, 25921, 361, 20736, 361], False),
    ([2, 2, 3], [4, 9, 9], False)
])
def test_same(a,b, expected):
    assert same(a,b) == expected