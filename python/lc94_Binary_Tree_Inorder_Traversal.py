from typing import Optional

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

class Stack:    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        node = root
        # terminal condition
        while node or stack:
            # deal with left node and current node
            if node:
                stack.append(node)
                node = node.left
            # deal with right one and get result value from stack
            else:
                node = stack.pop()
                res.append(node.val)
                node = node.right
        return res

class DFS:
    """
    Time: O(n)
    Space: O(n)
    """
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        if not root:
            return self.res
        
        self.in_order(root)
        return self.res
        
    def in_order(self, node):
        if not node:
            return
        
        self.in_order(node.left)
        self.res.append(node.val)
        self.in_order(node.right)
            
