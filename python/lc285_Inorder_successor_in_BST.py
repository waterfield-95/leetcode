# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Optimal:
    """
    Time: O(N) -> skewed tree, for balanced binary tree -> O(LogN)
    Space: O(1)
    """
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'Optional[TreeNode]':
        successor = None
        node = root
        while node:
            if p.val >= node.val:
                node = node.right
            else:
                successor = node
                node = node.left
        return successor

class Solution:
    """
    Time: O(N)
    Space: O(N) -> recursion stack
    """
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'Optional[TreeNode]':
        successor = None
        if p.right:
            node = p.right
            # find the in-order successor as node
            while node.left:
                node = node.left
            successor = node
        else:
            # find parent of node p by using binary search
            node = root
            prev = None
            
            def inorder(node, p):
                nonlocal prev, successor
                if not node:
                    return
                
                inorder(node.left, p)
                if prev == p and not successor:
                    successor = node
                    return
                prev = node
                inorder(node.right, p)
                
            inorder(node, p)
        return successor
        
        