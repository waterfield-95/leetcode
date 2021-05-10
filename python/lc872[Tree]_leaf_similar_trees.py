"""
2021.5
idea: DFS
    - DFS traverse tree
    - using "yield" and "yield form generator" to generate leaves value without memeory list
"""


from typing import List
from utils.binary_tree import BinarySearchTreeFromList

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar_mod(self, root1, root2):
        def dfs(node):
            if not node:
                yield
            if not node.left and not node.right:
                yield node.val
            if node.left:
                yield from dfs(node.left)
            if node.right:
                yield from dfs(node.right)
        
        leaves1 = list(dfs(root1))
        leaves2 = list(dfs(root2))
        return leaves1 == leaves2

    def leafSimilar_official(self, root1, root2):
        def dfs(node):
            if not node.left and not node.right:
                yield node.val
            else:
                if node.left:
                    yield from dfs(node.left)
                if node.right:
                    yield from dfs(node.right)
        
        seq1 = list(dfs(root1)) if root1 else list()
        seq2 = list(dfs(root2)) if root2 else list()
        return seq1 == seq2

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leaves1 = []
        self.getBinaryTreeLeaf(root1, leaves1)
        leaves2 = []
        self.getBinaryTreeLeaf(root2, leaves2)
        return leaves1 == leaves2

    def getBinaryTreeLeaf(self, root, leaf_list):
        if root == None:
            return
        
        if root.left == None and root.right==None:
            leaf_list.append(root.val)
        self.getBinaryTreeLeaf(root.left, leaf_list)
        self.getBinaryTreeLeaf(root.right, leaf_list)
        

if __name__ == '__main__':
    root1 = [3,5,1,6,2,9,8,None, None,7,4]
    root2 = [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]
    bst = BinarySearchTreeFromList
    r1 = bst(root1).create_tree()
    r2 = bst(root2).create_tree()
    S = Solution()
    leaves = []
    # print(S.getBinaryTreeLeaf(r1, leaves), leaves)
    print(S.leafSimilar_mod(r1, r2))
