"""
112. Path Sum
https://leetcode.com/problems/path-sum/

Pattern: Trees (DFS)
Time: O(n) | Space: O(h)  (h = tree height, recursion stack)

Approach:
DFS down from the root, subtracting each node's value from the
target sum as you descend. At a leaf, check if the remaining
target has been reduced to exactly 0 — that means the path from
root to this leaf sums to the original target.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(root: TreeNode, targetSum: int) -> bool:
    if not root:
        return False

    if not root.left and not root.right:
        return targetSum == root.val

    remaining = targetSum - root.val
    return hasPathSum(root.left, remaining) or hasPathSum(root.right, remaining)


if __name__ == "__main__":
    # Tree:        5
    #            /   \
    #           4     8
    #          /     /  \
    #         11    13   4
    #        /  \          \
    #       7    2          1
    root = TreeNode(5,
        TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
        TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))

    print(hasPathSum(root, 22))  # True  (5 -> 4 -> 11 -> 2)
    print(hasPathSum(root, 26))  # True  (5 -> 8 -> 13)
    print(hasPathSum(root, 100)) # False
