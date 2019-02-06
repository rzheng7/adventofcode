from math import pow
from copy import deepcopy
import pytest

def subset_matrix(matrix, row, col):
    ret_matrix = []
    cp_m = deepcopy(matrix)
    del cp_m[row]
    for el in cp_m:
        del el[col]
        ret_matrix.append(el)

    return ret_matrix

def determinant(matrix):
    #your code here

    if not matrix:
        return None

    if len(matrix) == 1 and len(matrix[0]) == 1:
        return matrix[0][0]

    # if len(matrix) == 2 and len(matrix[0]) == 2:
    #     return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    sum = 0
    for indx, el in enumerate(matrix[0]):
        sub_m = subset_matrix(matrix, 0, indx)
        sum += el * (int(pow(-1, indx))) * determinant(sub_m)

    return sum


@pytest.mark.parametrize(
    "m,r,c,expected",
    [
        ([[2,5,3], [1,-2,-1], [1, 3, 4]], 0, 0, [[-2,-1], [3, 4]]),
        ([[1,2,3,4], [1,2,3,4], [1,2,3,4], [1,2, 3, 4]], 0, 0, [[2,3,4],[2,3,4],[2,3,4]]),
        ([[1,2,3,4], [1,2,3,4], [1,2,3,4], [1,2, 3, 4]], 1, 2, [[1,2,4],[1,2,4],[1,2,4]]),
    ]
)
def test_subset_matrix(m, r, c, expected):
    assert subset_matrix(m, r, c) == expected


@pytest.mark.parametrize(
    "m,expected",
    [
        ([[1]], 1),
        ([[1, 3], [2, 5]], -1),
        ([[2, 5, 3], [1, -2, -1], [1, 3, 4]], -20)
    ]
)
def test_determinant(m, expected):
    assert determinant(m) == expected
