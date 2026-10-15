"""
1. Two Sum
https://leetcode.com/problems/two-sum/
Difficulty: Easy | Topics: Array, Hash Table

Approach:
    Walk through the list once. For each number, check if the number we
    need (target - num) was already seen. A dictionary maps each seen
    value to its index, so the lookup is O(1).

Time: O(n)   Space: O(n)
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in seen:
                return [seen[need], i]
            seen[num] = i
        return []


if __name__ == "__main__":
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert s.twoSum([3, 2, 4], 6) == [1, 2]
    assert s.twoSum([3, 3], 6) == [0, 1]
    print("All tests passed")
