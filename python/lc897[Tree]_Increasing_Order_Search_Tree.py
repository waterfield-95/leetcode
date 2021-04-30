"""
2021.4
idea: in-oder traversal
1. get sorted value list and then recreate the new tree
2. during the in-order traversal, modify the node direction
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTreeFromList:
    def __init__(self, nums) -> None:
        self.nums = nums
        self.root = TreeNode(nums[0])
        self.node_queue = [self.root]

    def create_tree(self):
        front = 0
        index = 1
        while index < len(self.nums):
            node = self.node_queue[front]
            front += 1
            
            left_val = self.nums[index]
            index += 1
            if left_val:
                node.left = TreeNode(left_val)
                self.node_queue.append(node.left)
            else:
                pass

            if index >= len(self.nums):
                break
            
            right_val = self.nums[index]
            index += 1
            if right_val:
                node.right = TreeNode(right_val)
                self.node_queue.append(node.right)
            else:
                pass
        print("Binary search has been created, return root")
        return self.root


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        in_order_list = []
        def in_order_traversal(root):
            if root.left:
                in_order_traversal(root.left)

            in_order_list.append(root.val)
            
            if root.right:
                in_order_traversal(root.right)
        
        in_order_traversal(root)
        new_root = TreeNode(in_order_list[0])
        tmp = new_root
        for val in in_order_list[1:]:
            tmp.right = TreeNode(val)
            tmp = tmp.right
        return new_root

    def official1(self, root):
        def in_order(node, res):
            if node is None:
                return
            in_order(node.left, res)
            res.append(node.val)
            in_order(node.right, res)
        
        res = []
        in_order(root, res)
        dummy_node = TreeNode(-1)
        cur_node = dummy_node
        for val in res:
            cur_node.right = TreeNode(val)
            cur_node = cur_node.right
        return dummy_node.right
    
    def official2(self, root):
        # 递归过程中修改节点指向
        def in_order(node):
            if node is None:
                return
            in_order(node.left)
            self.res_root.right = node
            node.left = None
            self.res_root = node
            in_order(node.right)
        
        dummy_node = TreeNode(-1)
        self.res_root = dummy_node
        in_order(root)
        return dummy_node.right


if __name__ == '__main__':
    nums = [5,3,6,2,4,None,8,1,None,None,None,7,9]
    binary_tree = BinarySearchTreeFromList(nums)
    root = binary_tree.create_tree()
    S = Solution()
    # print(S.increasingBST(root).val)
    print(S.official2(root).val)
