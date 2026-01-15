#!/usr/bin/python3
"""
Module for calculating minimum operations needed to achieve n characters.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in
    exactly n H characters in the file.

    The function uses prime factorization: the minimum number of operations
    is the sum of all prime factors of n (with repetition).

    Args:
        n (int): Target number of H characters

    Returns:
        int: Minimum number of operations needed, or 0 if impossible

    Example:
        >>> minOperations(9)
        6
        >>> minOperations(4)
        4
        >>> minOperations(12)
        7
    """
    if not isinstance(n, int) or n <= 1:
        return 0

    operations = 0
    divisor = 2

    # Find all prime factors and sum them
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
