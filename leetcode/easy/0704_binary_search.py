"""
704. Binary Search
https://leetcode.com/problems/binary-search/
Difficulty: Easy | Topics: Array, Binary Search

Approach:
    Keep a search window [left, right]. Check the middle element:
    if it is too small, search the right half; if too big, the left half.
    Each step halves the window.

Time: O(log n)   Space: O(1)
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


if __name__ == "__main__":
    s = Solution()
    assert s.search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert s.search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert s.search([5], 5) == 0
    print("All tests passed")
