from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, node: ListNode):
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def print(self):
        if not self.head:
            print('None')
        else:
            cur = self.head
            while cur:
                if cur.next:
                    print(cur.val, '->', end=' ')
                else:
                    print(cur.val)
                cur = cur.next

    def sample(self):
        ll = LinkedList()
        ll.append(ListNode(0))
        ll.append(ListNode(1))
        ll.append(ListNode(2))
        ll.append(ListNode(3))
        return ll
        
        

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        
if __name__ == '__main__':
    ll = LinkedList()
    ll.append(ListNode(0))
    ll.append(ListNode(1))
    ll.append(ListNode(2))
    ll.append(ListNode(3))
    ll.print()

    S = Solution()
    n = ll.head.next.next
    S.deleteNode(n)
    ll.print()