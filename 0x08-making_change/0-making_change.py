#!/usr/bin/python3
"""
defines a function makeChange
"""


def makeChange(coins, total):
    """
    determines the fewest number of coins needed to meet a
    give amount total
    Return:
        the fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0

    count = 0
    temp = 0
    coins.sort(reverse=True)

    for coin in coins:
        if coin < total:
            while temp < total:
                temp += coin
                if temp <= total:
                    count += 1
                else:
                    temp -= coin
                    break

    if temp == total:
        return count

    return -1
