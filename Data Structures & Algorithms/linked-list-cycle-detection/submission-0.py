# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Two methods:
        # 1. Remember every node we've seen so far in a set
        # 2. Slow pointer that moves by one, fast pointer that moves by 2; if there's a cycly, slow == fast eventually

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
                
        return False