import collections

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Optimal:
    """
    Two pointer: 1st to get the lenght of two linkedlist, 2nd to find intersection

    Time: O(M+N)
    Space: O(1)
    """
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1, l2 = 0, 0
        curA, curB = headA, headB
        while curA:
            l1 += 1
            curA = curA.next
        while curB:
            l2 += 1
            curB = curB.next
        
        
        s1 = headA
        s2 = headB
        diff = abs(l1-l2)
        if l1 > l2:
            while diff:
                s1 = s1.next
                diff -= 1
        elif l1 < l2:
            while diff:
                s2 = s2.next
                diff -= 1
        
        while s1 and s2:
            if s1 == s2:
                return s1
            s1 = s1.next
            s2 = s2.next
        return None
            

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        cnt = collections.defaultdict(int)
        while headA:
            cnt[headA] += 1
            headA = headA.next
        
        while headB:
            if headB in cnt:
                return headB
            headB = headB.next
        
        return None