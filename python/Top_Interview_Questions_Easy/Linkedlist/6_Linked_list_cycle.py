class TortoiseAndHare:
    """
    Without extra space: O(1) space complexity
    """
    def hasCycle(self, head):
        try:
            slow, fast = head, head.next
            while slow != fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False

    def hasCycle_2(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

if __name__ == '__main__':
    from python.Top_Interview_Questions_Easy.Linkedlist import LinkedList
    ll = LinkedList().sample([1,2])
    ll.print()
    S = TortoiseAndHare()
    print(S.hasCycle_2(ll.head))
