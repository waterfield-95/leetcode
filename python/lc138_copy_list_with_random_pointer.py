"""
2021.7
LinkedList:
    - dummy_head
    - termination condition: node is None

idea: Copy LinkedList with random pointer
"""

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    """
    - backtracing through two pointer: node.next, node.random, return copy node
    - hashtable to record original node and copy node
    - Time: O(n)
    - Space: O(n)
    """
    node_cache = {}
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return
        
        if head not in self.node_cache:
            copy_head = Node(head.val)
            self.node_cache[head] = copy_head
            copy_head.next = self.copyRandomList(head.next)
            copy_head.random = self.copyRandomList(head.random)
        return self.copyRandomList(head)    

class Solution1:
    """
    - traverse through continuous copied node in space
        - copy node
        - copy random pointer
        - divide two linked list
    - Space: O(1)
    """      
    def copyRandomList(self, head):
        ptr = head
        # copy node
        while ptr:
            copy_node = Node(ptr.val)
            tmp = ptr.next
            ptr.next = copy_node
            copy_node.next = tmp
            ptr = tmp
        
        # copy random pointer
        ptr = head
        while ptr:
            copy_node = ptr.next
            copy_node.random = ptr.random.next if ptr.random is not None else None
            ptr = ptr.next.next
        
        # divide original linkedlist and the copyed
        ptr = head
        dummy_head = Node(0)
        last_node = dummy_head
        while ptr:
            copy_node = ptr.next
            last_node.next = copy_node
            last_node = copy_node
            ptr = ptr.next.next
        return dummy_head.next
            

        
            
            



def listToLinkedlist(list_):
    dummy_head = Node(0)
    ptr = dummy_head

    nodes = []
    for val, _ in list_:
        ptr.next = Node(val)
        nodes.append(ptr.next)
        ptr = ptr.next
    
    for i, (_, random_) in enumerate(list_):
        if random_ is not None:
            nodes[i].random = nodes[random_]
        else:
            nodes[i].random = None

    return dummy_head.next

def copyLinkedList(head_):
    node = head_
    dummy_head = Node(0)
    copy_node = dummy_head
    while node.next:
        copy_node.next = Node(node.val, random=node.random)
        copy_node = copy_node.next
        node = node.next
    return dummy_head.next

def dfs(node):
    if not node:
        return
    print(node.val)
    dfs(node.next)        


if __name__ == '__main__':
    head = [[7, None], [13, 0], [11, 4], [10,2], [1,0]]
    head_ = listToLinkedlist(head)
    print(head_.val)
    # S = Solution()
    # h = S.copyRandomList(head_)
    # print(h.val)