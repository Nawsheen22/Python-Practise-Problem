"""
11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/
Difficulty: Medium | Topics: Array, Two Pointers, Greedy

Approach:
    Start with the widest container (both ends). The water is limited by
    the shorter wall, so moving the taller wall inward can never help.
    Always move the shorter wall and track the best area.

Time: O(n)   Space: O(1)
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        best = 0
        while left < right:
            area = (right - left) * min(height[left], height[right])
            best = max(best, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return best


if __name__ == "__main__":
    s = Solution()
    assert s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert s.maxArea([1, 1]) == 1
    print("All tests passed")
