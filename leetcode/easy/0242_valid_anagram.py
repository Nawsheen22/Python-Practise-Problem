"""
242. Valid Anagram
https://leetcode.com/problems/valid-anagram/
Difficulty: Easy | Topics: Hash Table, String, Sorting

Approach:
    Two strings are anagrams if every character appears the same number
    of times in both. Count the characters in each and compare.

Time: O(n)   Space: O(1), at most 26 lowercase letters
"""
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return len(s) == len(t) and Counter(s) == Counter(t)


if __name__ == "__main__":
    s = Solution()
    assert s.isAnagram("anagram", "nagaram") is True
    assert s.isAnagram("rat", "car") is False
    print("All tests passed")
