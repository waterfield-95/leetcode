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
    DFS
    Time: O(n)
    Space: O(n)
    """
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        def dfs(node, level):
            if len(result) <= level: # can use "==" for the first time
                result.append(collections.deque())
            
            if level % 2 == 0:
                result[level].append(node.val)
            else:
                result[level].appendleft(node.val)
            
            for child in [node.left, node.right]:
                if child:
                    dfs(child, level+1)

        dfs(root, 0)
        return result

class BFS2:
    """
    Single loop with two deque for node and current level
    """
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        level = collections.deque()
        dq = collections.deque([root, None])    # delimiter for current level
        is_left_order = True
        while dq:
            node = dq.popleft()
            if node:
                if is_left_order:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
                
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            else:
                # complete current level traversal
                res.append(level)
                level = collections.deque()
                # if not terminate, add a new delimiter
                if dq:
                    dq.append(None)
                
                # change flag of traversal order
                is_left_order = not is_left_order
        
        return res
                

class BFS1:
    """
    Time: O(n)
    Space: O(n)
    """
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        q = collections.deque([root])
        
        while q:
            level = []
            length = len(q)
            for i in range(length):
                node = q.popleft()
                level.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            res.append(level)
            
        print(res)
        for i in range(len(res)):
            if i % 2 == 1:
                res[i].reverse()
        
        return res
        