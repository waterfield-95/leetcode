from typing import List, Optional
from python.Top_Interview_Questions_Easy.Linkedlist import LinkedList

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        dummy_head.next = head
        l = []
        cur = dummy_head
        while cur:
            l.append(cur)
            cur = cur.next
        
        remove_node = l[-n]
        if remove_node.next:
            remove_node.val = remove_node.next.val
            remove_node.next = remove_node.next.next
        else:
            last_node = l[-n-1]
            last_node.next = None
        return dummy_head.next


class DoublePointer:
    def removeNthFromEnd(self, head, n: int):
        # remove one node, you need to find the previous node of target node
        dummy_head = ListNode(0)
        dummy_head.next = head
        left, right = dummy_head, dummy_head
        count = 0
        while right.next:
            if count != n:
                right = right.next
                count += 1
            else:
                left = left.next
                right = right.next
        left.next = left.next.next
        return dummy_head.next
    
    def removeNthFromEnd_concise(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        dummy_head.next = head
        left, right = dummy_head, dummy_head
        
        for _ in range(n):
            right = right.next
        
        while right.next:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return dummy_head.next


if __name__ == '__main__':
    l = [1,2]
    n = 2
    ll = LinkedList().sample(l)
    S = DoublePointer()
    head = S.removeNthFromEnd(ll.head, n)
    
    cur = head
    while cur:
        print(cur.val, '->', end=' ')
        cur = cur.next
