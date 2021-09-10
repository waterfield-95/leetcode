from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class CopyToList:
    """
    O(n)
    O(n)
    """
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur = head
        values = []
        while cur:
            values.append(cur.val)
            cur = cur.next
        
        # Python Trick: return values == values[::-1]
        start, end = 0, len(values)-1
        while start < end:
            if values[start] != values[end]:
                return False
            start += 1
            end -= 1
        return True
            
