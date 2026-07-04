"""
206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/

Pattern: Linked Lists (iterative pointer reversal)
Time: O(n) | Space: O(1)

Approach:
Walk the list once, at each node flipping its `next` pointer to
point back at the previous node instead of forward. Keep track of
`prev` and `curr`, advancing both each iteration until `curr` runs
off the end — `prev` is then the new head.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: ListNode) -> ListNode:
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev


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
    head = from_list([1, 2, 3, 4, 5])
    print(to_list(reverseList(head)))  # [5, 4, 3, 2, 1]
