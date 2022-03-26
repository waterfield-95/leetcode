from typing import Optional, List
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Time: O(n) traverse each node once
    Space: O(n) -> deque and keep the output structure which both contains N node values
    """
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        dq = collections.deque([root])    # dq.popleft(), dq.append()
        
        while dq:
            level = []
            level_num = len(dq)
            for i in range(level_num):
                node = dq.popleft()
                level.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            res.append(level)
        
        return res

class DFS:
    """
    Recursion
    Time: O(n)
    Space: O(n)
    """
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        levels = []
        
        def helper(node, level):
            nonlocal levels
            if len(levels) == level:
                levels.append([])
            
            levels[level].append(node.val)
            
            if node.left:
                helper(node.left, level+1)
            if node.right:
                helper(node.right, level+1)
        
        helper(root, 0)
        return levels
        
        