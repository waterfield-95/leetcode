"""
2021.4
idea: BFS, DFS
  - based on the characteristic of BST
"""


from Leetcode.tools.bst import BinarySearchTreeFromList, TreeNode
from Leetcode.tools.timer import func_timer
from collections import deque


class Solution:
    @func_timer
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def in_order(node, low, high):
            if node is None:
                return
            in_order(node.left, low, high)
            if node.val >= low and node.val <= high:
                self.sum_ += node.val
            in_order(node.right, low, high)
            
        self.sum_ = 0
        in_order(root, low, high)
        return self.sum_

    @func_timer
    def rangeSumBST_BFS(self, root, low, high):
        node_queue = deque([root])
        sum_ =0
        while node_queue:
            cur = node_queue.popleft()
            if cur is None:
                continue
            if cur.val > high:
                node_queue.append(cur.left)
            elif cur.val < low:
                node_queue.append(cur.right)
            else:
                sum_ += cur.val
                node_queue.append(cur.left)
                node_queue.append(cur.right)
        return sum_

    def rangeSumBST_DFS(self, root, low, high):
        if root is None:
            return 0
        elif root.val > high:
            return self.rangeSumBST_DFS(root.left, low, high)
        elif root.val < low:
            return self.rangeSumBST_DFS(root.right, low, high)
        else:
            result = sum([
                self.rangeSumBST_DFS(root.left, low, high),
                root.val,
                self.rangeSumBST_DFS(root.right, low, high)
            ])
            return result


if __name__ == '__main__':
    nums = [10,5,15,3,7,13,18,1,None,6] #output: 23
    low, high = 6, 10
    bst = BinarySearchTreeFromList(nums)
    root = bst.create_tree()
    S = Solution()
    print(S.rangeSumBST(root, low, high))
    print(S.rangeSumBST_BFS(root, low, high))
    import time
    t0 = time.time()
    print(S.rangeSumBST_DFS(root, low, high))
    print(time.time() - t0)
