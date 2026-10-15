"""
56. Merge Intervals
https://leetcode.com/problems/merge-intervals/
Difficulty: Medium | Topics: Array, Sorting

Approach:
    Sort intervals by start. Go through them in order: if an interval
    starts before the last merged one ends, they overlap, so extend the
    end. Otherwise start a new merged interval.

Time: O(n log n)   Space: O(n)
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        for start, end in intervals:
            if merged and start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])
        return merged


if __name__ == "__main__":
    s = Solution()
    assert s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert s.merge([[1, 4], [4, 5]]) == [[1, 5]]
    assert s.merge([[1, 4], [0, 4]]) == [[0, 4]]
    print("All tests passed")
