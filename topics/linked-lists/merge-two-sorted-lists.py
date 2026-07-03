"""
21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/

Pattern: Linked Lists (dummy node)
Time: O(n + m) | Space: O(1) excluding output

Approach:
Use a dummy head to avoid special-casing the first node. Walk both
lists simultaneously, always attaching the smaller current node,
then attach whatever remains of the non-exhausted list.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    tail.next = list1 if list1 else list2
    return dummy.next


def to_list(node):
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out


def from_list(values):
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


if __name__ == "__main__":
    l1 = from_list([1, 2, 4])
    l2 = from_list([1, 3, 4])
    print(to_list(mergeTwoLists(l1, l2)))  # [1, 1, 2, 3, 4, 4]
