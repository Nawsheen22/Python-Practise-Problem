"""
70. Climbing Stairs
https://leetcode.com/problems/climbing-stairs/
Difficulty: Easy | Topics: Math, Dynamic Programming

Approach:
    To reach step n you come from step n-1 or step n-2, so
    ways(n) = ways(n-1) + ways(n-2), the Fibonacci pattern.
    Only the last two values are needed, so keep two variables.

Time: O(n)   Space: O(1)
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        current, previous = 1, 1
        for _ in range(n - 1):
            current, previous = current + previous, current
        return current


if __name__ == "__main__":
    s = Solution()
    assert s.climbStairs(1) == 1
    assert s.climbStairs(2) == 2
    assert s.climbStairs(3) == 3
    assert s.climbStairs(5) == 8
    print("All tests passed")
