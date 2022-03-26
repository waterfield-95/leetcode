from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Digitwise:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode(0)
        
        h1, h2 = l1, l2
        carry = 0
        while h1 or h2:
            v1 = h1.val if h1 else 0
            v2 = h2.val if h2 else 0
            s = v1 + v2 + carry
            carry = s // 10
            cur.next = ListNode(s % 10)
            cur = cur.next
            h1 = h1.next if h1 else None
            h2 = h2.next if h2 else None
        
        if carry:
            cur.next = ListNode(carry)
            
        return dummy.next
        


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = 0, 0
        
        i = 0
        h1 = l1
        while h1:
            num1 += h1.val * pow(10, i)
            h1 = h1.next
            i += 1
        
        i = 0
        h2 = l2
        while h2:
            num2 += h2.val * pow(10, i)
            h2 = h2.next
            i += 1
            
        res = num1 + num2

        res, val = divmod(res, 10)
        l3 = cur = ListNode(val)    # we can also use dummy head
        while res != 0:
            res, val = divmod(res, 10)
            cur.next = ListNode(val)
            cur = cur.next
        return l3