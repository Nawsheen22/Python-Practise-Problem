"""
238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/
Difficulty: Medium | Topics: Array, Prefix Sum

Approach:
    The answer at i is (product of everything left of i) times
    (product of everything right of i). First pass fills in the left
    products; second pass, going backward, multiplies in the right
    products. No division needed.

Time: O(n)   Space: O(1) extra, not counting the output
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        left = 1
        for i in range(n):
            answer[i] = left
            left *= nums[i]
        right = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right
            right *= nums[i]
        return answer


if __name__ == "__main__":
    s = Solution()
    assert s.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert s.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    print("All tests passed")
