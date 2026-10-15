"""
200. Number of Islands
https://leetcode.com/problems/number-of-islands/
Difficulty: Medium | Topics: Array, Depth-First Search, Matrix

Approach:
    Scan every cell. When we find land ("1"), count a new island and
    flood-fill it: mark all connected land as visited ("0") using DFS
    with an explicit stack, so the same island is not counted twice.

Time: O(rows * cols)   Space: O(rows * cols) in the worst case
"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != "1":
                    continue
                islands += 1
                stack = [(r, c)]
                grid[r][c] = "0"
                while stack:
                    i, j = stack.pop()
                    for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                        if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == "1":
                            grid[ni][nj] = "0"
                            stack.append((ni, nj))
        return islands


if __name__ == "__main__":
    s = Solution()
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    assert s.numIslands(grid1) == 1
    assert s.numIslands(grid2) == 3
    print("All tests passed")
