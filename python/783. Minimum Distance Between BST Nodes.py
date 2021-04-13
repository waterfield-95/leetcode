"""
2021.4
idea: 
1. in-order traverse to get sorted list
  - find minimum from the list of difference between neighbor elements from the sorted list
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def list2tree(lst):
    root = TreeNode(lst[0])
    node_queue = [root]
    front = 0
    index = 1
    while index < len(lst):
        node = node_queue[front]
        front += 1
        item = lst[index]
        index += 1
        if item != 'null':
            left_number = item
            node.left = TreeNode(item)
            node_queue.append(node.left)
        
        if index >= len(lst):
            break

        item = lst[index]
        index += 1
        if item != 'null':
            right_number = item
            node.right = TreeNode(right_number)
            node_queue.append(node.right)
    return root

# 中序遍历打印
def print_tree(root):
    if root.left:
        print_tree(root.left)
    
    print(root.val)
    
    if root.right:
        print_tree(root.right)
    

class Solution:
    def __init__(self) -> None:
        self.res = []

    def inOrder(self, root):
        if root.left:
            self.inOrder(root.left)
        
        self.res.append(root.val)

        if root.right:
            self.inOrder(root.right)
        
    def minDiffInBST(self, root: TreeNode) -> int:
        self.inOrder(root)
        diff = [self.res[i] - self.res[i-1] for i in range(1, len(self.res))]
        return min(diff)


if __name__ == '__main__':
    root_list = [1,0,48,'null','null',12,49]
    root = list2tree(root_list)
    # print_tree(root)

    S = Solution()
    print(S.minDiffInBST(root))
