from utils.binary_tree import BinarySearchTreeFromList

class BST:
    def __init__(self, values) -> None:
        self.values = values
        self.root = TreeNode(values[0])
        self._create()
        

    def _create(self):
        index = 1
        queue = [self.root]
        while index < len(self.values):
            node = queue.pop()
            if self.values[index]:
                node.left = TreeNode(self.values[index])
                queue.insert(0, node.left)
            
            index += 1
            if index >= len(self.values):
                break
            if self.values[index]:
                node.right = TreeNode(self.values[index])
                queue.insert(0, node.right)
            index += 1
    
    def dfs(self, node):
        if node is None:
            return
        print(node.val)
        self.dfs(node.left)
        self.dfs(node.right)
            

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool: 
        x_parent, x_depth, x_found = None, None, False
        y_parent, y_depth, y_found = None, None, False
        
        def dfs(node, depth, parent):
            if not node:
                return

            nonlocal x_parent, y_parent, x_depth, y_depth, x_found, y_found

            if node.val == x:
                x_parent, x_depth, x_found = parent, depth, True
            elif node.val == y:
                y_parent, y_depth, y_found = parent, depth, True
                
            if x_found and y_found:
                return
            
            dfs(node.left, depth+1, node)
            
            if x_found and y_found:
                return
            
            dfs(node.right, depth+1, node)
        
        dfs(root, 0, None)
        return x_depth == y_depth and x_parent != y_parent
    
    def isCousins_bfs(self, root, x, y):
        x_parent, x_depth, x_found = None, None, False
        y_parent, y_depth, y_found = None, None, False
        queue = [(root, None, 0)]
        while queue:
            node, parent, depth = queue.pop()

            if node.val == x:
                x_parent, x_depth, x_found = parent, depth, True
            elif node.val == y:
                y_parent, y_depth, y_found = parent, depth, True
            
            if x_found and y_found:
                break
            
            if node.left:
                queue.append((node.left, node, depth+1))
            if node.right:
                queue.append((node.right, node, depth+1))
        
        return x_depth == y_depth and x_parent != y_parent
                

if __name__ == '__main__':
    root_list = [1,2,3,None,4]
    x = 5
    y = 4
    bst = BST(root_list)
    root = bst.root
    S = Solution()
    print(S.isCousins_bfs(root, x, y))


