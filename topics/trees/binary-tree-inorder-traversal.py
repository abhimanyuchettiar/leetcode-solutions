"""
94. Binary Tree Inorder Traversal
https://leetcode.com/problems/binary-tree-inorder-traversal/

Pattern: Trees (DFS)
Time: O(n) | Space: O(h)  (h = tree height, recursion stack)

Approach:
Inorder = left subtree, then node, then right subtree. Straightforward
recursive DFS; an iterative version with an explicit stack is the
natural follow-up if asked to avoid recursion.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: TreeNode) -> list[int]:
    result = []

    def dfs(node):
        if not node:
            return
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)

    dfs(root)
    return result


if __name__ == "__main__":
    # Tree:   1
    #          \
    #           2
    #          /
    #         3
    root = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
    print(inorderTraversal(root))  # [1, 3, 2]
