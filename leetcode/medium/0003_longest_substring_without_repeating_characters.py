"""
3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/
Difficulty: Medium | Topics: Hash Table, String, Sliding Window

Approach:
    Sliding window. Remember the last index of each character. When a
    character repeats inside the window, move the window's left edge to
    just after its previous position.

Time: O(n)   Space: O(k), k = number of distinct characters
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        best = 0
        for right, ch in enumerate(s):
            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1
            last_seen[ch] = right
            best = max(best, right - left + 1)
        return best


if __name__ == "__main__":
    s = Solution()
    assert s.lengthOfLongestSubstring("abcabcbb") == 3
    assert s.lengthOfLongestSubstring("bbbbb") == 1
    assert s.lengthOfLongestSubstring("pwwkew") == 3
    assert s.lengthOfLongestSubstring("") == 0
    assert s.lengthOfLongestSubstring("abba") == 2
    print("All tests passed")
