"""
121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Difficulty: Easy | Topics: Array, Dynamic Programming

Approach:
    Track the lowest price seen so far. On each day, the best profit if
    we sell today is (price - lowest). Keep the maximum of those.

Time: O(n)   Space: O(1)
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = float("inf")
        best = 0
        for price in prices:
            lowest = min(lowest, price)
            best = max(best, price - lowest)
        return best


if __name__ == "__main__":
    s = Solution()
    assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert s.maxProfit([7, 6, 4, 3, 1]) == 0
    print("All tests passed")
