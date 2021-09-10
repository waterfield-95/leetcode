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

    def sample(self, l: List = []):
        ll = LinkedList()
        if not l:
            ll.append(ListNode(0))
            ll.append(ListNode(1))
            ll.append(ListNode(2))
            ll.append(ListNode(3))
        else:
            for val in l:
                ll.append(ListNode(val))
        return ll


if __name__ == '__main__':
    ll = LinkedList().sample([45,67])
    ll.print()

