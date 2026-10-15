"""
104. Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/
Difficulty: Easy | Topics: Tree, Depth-First Search, Recursion

Approach:
    The depth of a tree is 1 (the root) plus the deeper of its two
    subtrees. An empty tree has depth 0.

Time: O(n)   Space: O(h), where h is the height of the tree
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


if __name__ == "__main__":
    s = Solution()
    #     3
    #    / \
    #   9  20
    #      / \
    #     15  7
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert s.maxDepth(root) == 3
    assert s.maxDepth(TreeNode(1, None, TreeNode(2))) == 2
    assert s.maxDepth(None) == 0
    print("All tests passed")
