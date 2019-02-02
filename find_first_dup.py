
# Note: Write a solution with O(n) time complexity and O(1) additional space complexity, since this is what you would be asked to do during a real interview.

# Given an array a that contains only numbers in the range from 1 to a.length, find the first duplicate number for which the second occurrence has the minimal index. In other words, if there are more than 1 duplicated numbers, return the number for which the second occurrence has a smaller index than the second occurrence of the other number does. If there are no such elements, return -1.

# Example

# For a = [2, 3, 3, 1, 5, 2], the output should be
# firstDuplicate(a) = 3.

# There are 2 duplicates: numbers 2 and 3. The second occurrence of 3 has a smaller index than than second occurrence of 2 does, so the answer is 3.

# For a = [2, 4, 3, 5, 1], the output should be
# firstDuplicate(a) = -1.

# Input/Output

# [time limit] 500ms (cpp)
# [input] array.integer a

# Guaranteed constraints:
# 1 ≤ a.length ≤ 105,
# 1 ≤ a[i] ≤ a.length.

# [output] integer

# The element in a that occurs in the array more than once and has the minimal index for its second occurrence. If there are no such elements, return -1.

import pytest

def first_duplicate(l):
    if not l:
        return -1

    if len(l) == 1:
        return -1

    l_dict = {k: 0 for k in range(min(l), max(l)+1)}  # in range max value should increase by 1!!!

    for i in l:
        if l_dict[i] == 1:
            return i

        l_dict[i] += 1
    return -1


@pytest.mark.parametrize("input,expected", [
    ([2, 3, 3, 1, 5, 2], 3),
    ([2, 4, 3, 5, 1], -1),
    ([1], -1),
    ([2, 2], 2),
    ([8, 4, 6, 2, 6, 4, 7, 9, 5, 8], 6),
    ([10, 6, 8, 4, 9, 1, 7, 2, 5, 3], -1),
    ([8, 1, 4, 8, 10, 1, 5, 7, 8, 7], 8),
    ([28, 19, 13, 6, 34, 48, 50, 3, 47, 18, 15, 34, 16, 11, 13, 3, 2, 4, 46, 6, 7, 3, 18, 9, 32, 21, 3, 21, 50, 10, 45, 13, 22, 1, 27, 18, 3, 27, 30, 44, 12, 30, 40, 1, 1, 31, 6, 18, 33, 5], 34)
    ])
def test_first_duplicate(input,expected):
    assert first_duplicate(input) == expected