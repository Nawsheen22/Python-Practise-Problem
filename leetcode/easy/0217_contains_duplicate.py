"""
217. Contains Duplicate
https://leetcode.com/problems/contains-duplicate/
Difficulty: Easy | Topics: Array, Hash Table

Approach:
    Add numbers to a set one by one. If a number is already in the set,
    we found a duplicate.

Time: O(n)   Space: O(n)
"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


if __name__ == "__main__":
    s = Solution()
    assert s.containsDuplicate([1, 2, 3, 1]) is True
    assert s.containsDuplicate([1, 2, 3, 4]) is False
    assert s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
    print("All tests passed")
