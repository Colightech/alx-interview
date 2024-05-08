#!/usr/bin/python3
""" Minimum Operations
    """


def minOperations(n: int) -> int:
    """ Minimum Operations needed to get n H characters """
    next = 'H'
    frame = 'H'
    opera = 0
    while (len(frame) < n):
        if n % len(frame) == 0:
            opera += 2
            next = frame
            frame += frame
        else:
            opera += 1
            frame += next
    if len(frame) != n:
        return 0
    return opera
