# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        mid = self.get_mid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)
    
    def merge(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ptr = ListNode(0)
        while head1 and head2:
            if head1.val <= head2.val:
                ptr.next = head1
                head1 = head1.next
            else:
                ptr.next = head2
                head2 = head2.next
            
            ptr = ptr.next
        
        if head1:
            ptr.next = head1
        else:
            ptr.next = head2
        return dummy_head.next
        
    def get_mid(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mid_prev = ListNode()
        mid_prev.next = head
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            mid_prev = mid_prev.next
        mid_prev.next = None
        return slow