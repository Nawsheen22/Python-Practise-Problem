"""
53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray/
Difficulty: Medium | Topics: Array, Dynamic Programming (Kadane's Algorithm)

Approach:
    Kadane's algorithm. At each number, either extend the current
    subarray or start fresh from this number, whichever is larger.
    Track the best sum seen.

Time: O(n)   Space: O(1)
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = best = nums[0]
        for num in nums[1:]:
            current = max(num, current + num)
            best = max(best, current)
        return best


if __name__ == "__main__":
    s = Solution()
    assert s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert s.maxSubArray([1]) == 1
    assert s.maxSubArray([5, 4, -1, 7, 8]) == 23
    assert s.maxSubArray([-3, -1, -2]) == -1
    print("All tests passed")
