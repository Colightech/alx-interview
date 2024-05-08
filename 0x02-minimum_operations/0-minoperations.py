#!/usr/bin/python3
"""Module for Minimum Operations
"""


def minOperations(n):
    """Calculates the fewest number of operations needed to result in
    exactly n H characters in the file.

    In a text file, there is a single character H. Your text editor can
    execute only two operations in this file: Copy All and Paste characters
    in the file.

    Args:
        n (int): The number of desired H characters.

    Returns:
        int: The number of minimal operations needed to get n H characters
    or 0 if it is impossible to achieve n.
    """
    if not isinstance(n, int):
        return 0
    operatn_count = 0
    curr_value = 0
    position = 1
    while position < n:
        if curr_value == 0:
            curr_value = position
            position += curr_value
            operatn_count += 2
        elif n - position > 0 and (n - position) % position == 0:
            curr_value = position
            position += curr_value
            operatn_count += 2
        elif curr_value > 0:
            position += curr_value
            operatn_count += 1
    return operatn_count
