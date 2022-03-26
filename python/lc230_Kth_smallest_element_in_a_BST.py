from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Optimal:
    """
    Stack
    Time: O(H+k): height of tree = logN, k is the k-th smallest
    Space: O(H)
    """
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        node = root
        stack = []
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            
            # when the node don't have left child, it's the smallest one
            node = stack.pop()
            k -= 1
            if not k:
                return node.val
            node = node.right


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def inorder(node):
            nonlocal sort_list
            if not node:
                return
            inorder(node.left)
            sort_list.append(node.val)
            inorder(node.right)
        
        sort_list = []        
        inorder(root)
        return sort_list[k-1]
