#!/usr/bin/python3
"""
defines a function isWinner
"""


def isPrime(num):
    """
    checks if a number 'num' is a prime
    """
    primes = []
    temp = [True] * (num + 1)

    for i in range(2, num + 1):
        if temp[i]:
            primes.append(i)
            for j in range(i, num + 1, i):
                temp[j] = False

    return primes


def isWinner(x, nums):
    """
    determines the winner of x games
    """
    if x is None or not isinstance(x, int) or nums is None:
        return None
    if x < 1 or nums == []:
        return None

    ben, maria = 0, 0

    for i in range(x):
        primes = isPrime(nums[i])
        if primes == []:
            ben += 1
        elif len(primes) % 2 == 0:
            ben += 1
        else:
            maria += 1

    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"
    else:
        return None
