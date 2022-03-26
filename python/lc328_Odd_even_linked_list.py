from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Optimal:
    """
    Intuition: two head and two pointer, visualize linkedlist and consider pointer direction and update
    """
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd = head
        even_head = even = head.next
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        odd.next = even_head
        return head

class Solution:
    """
    Time: O(n)
    Space: O(1)
    """
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        dummy1 = odd = ListNode(0)
        dummy2 = even = ListNode(0)
        cur = head
        flag = 1
        while cur:
            if flag == 1:
                odd.next = cur
                odd = odd.next
            else:
                even.next = cur
                even = even.next
            
            flag = flag * (-1)
            prev = cur
            cur = cur.next
            prev.next = None

        odd.next = dummy2.next
        return dummy1.next
            