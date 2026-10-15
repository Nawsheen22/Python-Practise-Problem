"""
206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/
Difficulty: Easy | Topics: Linked List

Approach:
    Walk the list and flip each node's next pointer to point backward.
    Keep a `prev` pointer; at the end it is the new head.

Time: O(n)   Space: O(1)
"""
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev


def build(values: List[int]) -> Optional[ListNode]:
    head = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head


def to_list(node: Optional[ListNode]) -> List[int]:
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out


if __name__ == "__main__":
    s = Solution()
    assert to_list(s.reverseList(build([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
    assert to_list(s.reverseList(build([1, 2]))) == [2, 1]
    assert to_list(s.reverseList(build([]))) == []
    print("All tests passed")
