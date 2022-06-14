# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        slower = head
        faster = head
        while faster.next != None and faster.next.next != None:
            slower = slower.next
            faster = faster.next.next
            if slower == faster:
                return True
        return False