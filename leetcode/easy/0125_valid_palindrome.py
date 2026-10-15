"""
125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/
Difficulty: Easy | Topics: Two Pointers, String

Approach:
    Two pointers start at both ends and move inward, skipping anything
    that is not a letter or digit. Compare characters case-insensitively.

Time: O(n)   Space: O(1)
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True


if __name__ == "__main__":
    s = Solution()
    assert s.isPalindrome("A man, a plan, a canal: Panama") is True
    assert s.isPalindrome("race a car") is False
    assert s.isPalindrome(" ") is True
    print("All tests passed")
