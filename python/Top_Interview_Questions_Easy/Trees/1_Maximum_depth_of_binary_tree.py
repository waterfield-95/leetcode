from utils.binary_tree import BinarySearchTreeFromList
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BFS:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        queue = deque()
        depth = 0
        if root:
            queue.appendleft(root)
        while queue:
            depth += 1
            n = 0
            length = len(queue)
            while n < length:
                n += 1
                node = queue.pop()
                if node.left:
                    queue.appendleft(node.left)
                if node.right:
                    queue.appendleft(node.right)
        return depth

class DFS:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


if __name__ == '__main__':
    nums = [0,2,4,1,None,3,-1,5,1,None,6,None,8]
    root = BinarySearchTreeFromList(nums).create_tree()
    S = DFS()
    print(S.maxDepth(root))
