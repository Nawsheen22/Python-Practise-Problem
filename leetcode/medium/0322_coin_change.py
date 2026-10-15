"""
322. Coin Change
https://leetcode.com/problems/coin-change/
Difficulty: Medium | Topics: Array, Dynamic Programming, Breadth-First Search

Approach:
    Bottom-up DP. dp[x] = fewest coins to make amount x.
    dp[0] = 0, and for each amount x, try every coin:
    dp[x] = min(dp[x], dp[x - coin] + 1).
    If dp[amount] is still "infinity", the amount cannot be made.

Time: O(amount * number of coins)   Space: O(amount)
"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = amount + 1
        dp = [0] + [INF] * amount
        for x in range(1, amount + 1):
            for coin in coins:
                if coin <= x:
                    dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != INF else -1


if __name__ == "__main__":
    s = Solution()
    assert s.coinChange([1, 2, 5], 11) == 3
    assert s.coinChange([2], 3) == -1
    assert s.coinChange([1], 0) == 0
    print("All tests passed")
