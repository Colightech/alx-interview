#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """
    a function that returns a list
    of integers representing the
    pascal triangle of n:
       . Returns an empty list if n <= 0
       . assume n will be always an integer
    """
    pascal_tri = []

    if n <= 0:
        return []

    for x in range(n):
        if (x == 0):
            pascal_tri.append([1])
        else:
            cur_row = []
            for j in range(x + 1):
                if (j == 0 or j == x):
                    cur_row.append(1)
                else:
                    cur_row.append(pascal_tri[x - 1][j - 1] +
                                   pascal_tri[x - 1][j])

            pascal_tri.append(cur_row)

    return (pascal_tri)
