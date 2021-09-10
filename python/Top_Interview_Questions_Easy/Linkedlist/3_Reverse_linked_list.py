from python.Top_Interview_Questions_Easy.Linkedlist import LinkedList, ListNode


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Iterative:
    def reverseList(self, head):
        prev = None
        cur = head
        while cur:
            tmp = cur
            cur = cur.next
            tmp.next = prev
            prev = tmp
        return prev

class Recursive:
    def reverseList(self, head):
        return self._reverse(head)

    def _reverse(self, node, prev=None):
        if not node:
            return prev
        next = node.next
        node.next = prev
        return self._reverse(next, prev=node)


if __name__ == '__main__':
    ll = LinkedList().sample()
    ll.print()
    S = Iterative()
    h = S.reverseList(ll.head)
    
    while h:
        print(h.val, '->', end=' ')
        h = h.next


