"""
49. Group Anagrams
https://leetcode.com/problems/group-anagrams/
Difficulty: Medium | Topics: Array, Hash Table, String, Sorting

Approach:
    Anagrams become the same string when their letters are sorted.
    Use the sorted word as a dictionary key and group words under it.

Time: O(n * k log k), k = longest word length   Space: O(n * k)
"""
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            groups["".join(sorted(word))].append(word)
        return list(groups.values())


if __name__ == "__main__":
    s = Solution()
    result = s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert sorted(sorted(g) for g in result) == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
    assert s.groupAnagrams([""]) == [[""]]
    assert s.groupAnagrams(["a"]) == [["a"]]
    print("All tests passed")
