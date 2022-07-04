# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head = ListNode(-1)
        dummy_head.next = head
        node = dummy_head
        while node.next != None:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
        return dummy_head.next