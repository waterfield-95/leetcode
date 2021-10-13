from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class SelfSolution:
    """
    Time: O(n)
    """
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        while queue:
            layer = []
            # add current layer value
            for node in queue:
                if node:
                    layer.append(node.val)
                else:
                    layer.append(None)
            # judge if the elements in this layer are symmetric
            n = len(layer)
            if layer[:n//2] != list(reversed(layer[(n//2+n%2):])):
                return False
            # add next layer node to queue
            m = len(queue)
            for i in range(m):
                node = queue.popleft()
                if not node:
                    continue
                if node.left:
                    queue.append(node.left)
                else:
                    queue.append(None)
                queue.append(node.right) if node.right else queue.append(None)
        return True


class Recursive:
    """
    TC: O(n)
    SC: O(n) recursive depth is less than n
    """
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        
        if left.val != right.val:
            return False
        else:
            return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)

class RecursiveByStack:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            else:
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
        return True

            
if __name__ == '__main__':
    from utils.binary_tree import BinarySearchTreeFromList
    nums = [1,2,2,None,3,None,3]
    root = BinarySearchTreeFromList(nums).create_tree()
    S = SelfSolution()
    print(S.isSymmetric(root))
