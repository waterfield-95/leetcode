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

            # left node
            left_val = self.nums[index]
            index += 1
            if left_val:
                node.left = TreeNode(left_val)
                self.node_queue.append(node.left)
            else:
                pass
            if index >= len(self.nums):
                break
            
            # right one
            right_val = self.nums[index]
            index += 1
            if right_val:
                node.right = TreeNode(right_val)
                self.node_queue.append(node.right)
            else:
                pass
        print("Binary search has been created, return root")
        return self.root


if __name__ == '__main__':
    # 列表是先序遍历结果，即根节点->left->right
    nums = [5,3,6,2,4,None,8,1,None,None,None,7,9]
    binary_tree = BinarySearchTreeFromList(nums)
    root = binary_tree.create_tree()
    print(root.val)