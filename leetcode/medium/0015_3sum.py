"""
15. 3Sum
https://leetcode.com/problems/3sum/
Difficulty: Medium | Topics: Array, Two Pointers, Sorting

Approach:
    Sort the array. Fix one number, then use two pointers on the rest
    to find pairs that sum to its negative. Skip equal neighbours so
    each triplet is reported only once.

Time: O(n^2)   Space: O(1) extra, not counting the output
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return result


if __name__ == "__main__":
    s = Solution()
    assert s.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert s.threeSum([0, 1, 1]) == []
    assert s.threeSum([0, 0, 0]) == [[0, 0, 0]]
    print("All tests passed")
