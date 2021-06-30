"""
2021.6.29
idea: given a node in a undirect connected graph, clone graph
which means we need to know the structure of the total graph
    - empty graph: return None
    - one node without neightbor: return only one node
    - base case: come across visited node, return cloned node
    - recursive: a new node -> clone node and add its neighbor -> recur neighbor node 
"""

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# DFS
class Solution:
    def __init__(self) -> None:
        self.visited = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        if node in self.visited:
            return self.visited[node]
        
        clone_node = Node(node.val, [])
        self.visited[node] = clone_node
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]
        
        return clone_node

# BFS
from collections import deque
class Solution2:
    def cloneGraph(self, node):
        # special case, node is None or single without neighbors
        if not node:
            return node
        
        visited = {}
        # if the node add to queue, it's regarded as visited
        queue = deque([node])
        visited[node] = Node(node.val, [])
        
        while queue:
            n = queue.popleft()
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                visited[n].neighbors.append(visited[neighbor])
        return visited[node]


if __name__ == '__main__':
    A = Node(1, [])
    B = Node(2, [])
    C = Node(3, [])
    D = Node(4, [])
    A.neighbors = [B, D]
    B.neighbors = [A, C]
    C.neighbors = [B,D]
    D.neighbors = [A,C]
    print([ node.neighbors for node in A.neighbors])