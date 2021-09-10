from typing import Optional
from math import inf
from utils.binary_tree import BinarySearchTreeFromList

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Recursive:
    """
    For each node, setting the maximum and minimum
    Time: O(n)
    Space: O(n)
    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        max_, min_ = float(inf), float(-inf)
        return self.dfs(root, max_, min_)
    
    def dfs(self, node, max_, min_):
        if not node:
            return True
        
        if node.val < max_ and node.val > min_:
            # Note: node.val < max_
            return self.dfs(node.left, node.val, min_) and self.dfs(node.right, max_, node.val)
        else:
            return False


class Stack:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        # push the tesing node
        stack = [(root, inf, -inf)]
        while stack:
            node, upper, lower = stack.pop()
            
            # current node satisfy the condition
            if node.val >= upper or node.val <= lower:
                return False
            
            if node.left:
                stack.append((node.left, node.val, lower))
            if node.right:
                stack.append((node.right, upper, node.val))
        return True
                
class InOrderRecursive:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.previous = -inf
        return self.in_order(root)

    def in_order(self, node):
        if not node:
            return True
        if not self.in_order(node.left):
            return False
        if node.val <= self.previous:
            return False
        else:
            self.previous = node.val
        if not self.in_order(node.right):
            return False
        return True

class InOrderIterative:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack, prev = [], -inf
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if node.val <= prev:
                return False
            else:
                prev = node.val
                node = node.right
        return True
        

if __name__ == '__main__':
    nums = [2,1,3]
    root = BinarySearchTreeFromList(nums).create_tree()
    S = InOrderIterative()
    print(S.isValidBST(root))