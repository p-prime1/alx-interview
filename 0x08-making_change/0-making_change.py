#!/usr/bin/python3
"""Module contains the makingChange function"""


def makeChange(coins, total):
    """The function finds determines te fewes number required to get
        a given amount (total)"""
    if total <= 0:
        return 0

    # Initialize dp table
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed for amount 0

    # Fill the dp table
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # Check if a solution exists
    return dp[total] if dp[total] != float('inf') else -1
