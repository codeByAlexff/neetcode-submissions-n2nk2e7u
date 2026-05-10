# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow = head
        fast = head

        if head == None:
            return False

        while fast and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        if slow != fast or fast.next == None:
            return False

        