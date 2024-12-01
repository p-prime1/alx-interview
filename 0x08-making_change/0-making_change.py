#!/usr/bin/python3
"""Module contains the makingChange function"""


def makeChange(coins, total):
    """The function finds determines te fewes number required to get
        a given amount (total)"""
    if total <= 0:
        return 0

    dynamic_table = [float('inf')] * (total + 1)
    dynamic_table[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dynamic_table[i] = min(dynamic_table[i],
                                   dynamic_table[i - coin] + 1)

    return dynamic_table[total] if dynamic_table[total] != float('inf')else -1
