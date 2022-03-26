from typing import Optional
import collections

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Optimal:
    """
    Using previously eastablished next pointer to populate the next pointer in the next level
    Time: O(n)
    Space: O(1)
    """
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        leftmost = root
        # we need ensure that there are nodes in the next level
        while leftmost.left:
            head = leftmost
            while head:
                #connection 1
                head.left.next = head.right
                #connection 2
                if head.next:
                    head.right.next = head.next.left
                
                head = head.next
            leftmost = leftmost.left
        return root

class Solution:
    """
    level order traversal by using two nested loop
    Time: O(n)
    Space: O(n) -> last level would have n/2 nodes
    """
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        q = collections.deque([root])
        level = 0
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if i == n-1:
                    node.next = None
                else:
                    node.next = q[0]
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return root
            
        
        