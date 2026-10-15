"""
42. Trapping Rain Water
https://leetcode.com/problems/trapping-rain-water/
Difficulty: Hard | Topics: Array, Two Pointers, Dynamic Programming

Approach:
    Water above a bar = min(tallest bar on its left, tallest on its right)
    minus the bar's height. Use two pointers from both ends and keep the
    max height seen from each side. Whichever side has the smaller max
    is the limiting wall, so we can settle that side's bar and move in.

Time: O(n)   Space: O(1)
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        water = 0
        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                water += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                water += right_max - height[right]
                right -= 1
        return water


if __name__ == "__main__":
    s = Solution()
    assert s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert s.trap([4, 2, 0, 3, 2, 5]) == 9
    assert s.trap([]) == 0
    print("All tests passed")
