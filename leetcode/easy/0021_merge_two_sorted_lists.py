"""
21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/
Difficulty: Easy | Topics: Linked List, Recursion

Approach:
    Use a dummy head node. Compare the fronts of both lists and attach
    the smaller node each time. When one list runs out, attach the rest
    of the other list.

Time: O(n + m)   Space: O(1)
"""
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = tail = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next, list1 = list1, list1.next
            else:
                tail.next, list2 = list2, list2.next
            tail = tail.next
        tail.next = list1 or list2
        return dummy.next


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
    assert to_list(s.mergeTwoLists(build([1, 2, 4]), build([1, 3, 4]))) == [1, 1, 2, 3, 4, 4]
    assert to_list(s.mergeTwoLists(build([]), build([]))) == []
    assert to_list(s.mergeTwoLists(build([]), build([0]))) == [0]
    print("All tests passed")
