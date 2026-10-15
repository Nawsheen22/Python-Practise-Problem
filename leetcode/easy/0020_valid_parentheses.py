"""
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/
Difficulty: Easy | Topics: String, Stack

Approach:
    Push every opening bracket onto a stack. When a closing bracket
    appears, the top of the stack must be its matching opener.
    The string is valid only if the stack is empty at the end.

Time: O(n)   Space: O(n)
"""


class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []
        for ch in s:
            if ch in pairs:
                if not stack or stack.pop() != pairs[ch]:
                    return False
            else:
                stack.append(ch)
        return not stack


if __name__ == "__main__":
    s = Solution()
    assert s.isValid("()") is True
    assert s.isValid("()[]{}") is True
    assert s.isValid("(]") is False
    assert s.isValid("([)]") is False
    assert s.isValid("{[]}") is True
    print("All tests passed")
