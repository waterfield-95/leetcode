"""
2021.6.28
idea: traverse a tree in inorder method
    - find the most left one and get its value, and then get upper level node value
    finally get right one value. Notice special condition which is None node.

1. DFS
2. stack

"""

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorder(self, root, res):
        if not root: return
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.inorder(root, res)
        return res

# stack
class Solution2:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        # terminal condition
        while root or stack:
            # deal with left node and current node
            if root:
                stack.append(root)
                root = root.left
            # deal with right one and get result value from stack
            else:
                cur = stack.pop()
                res.append(cur.val)
                root = cur.right
        return res