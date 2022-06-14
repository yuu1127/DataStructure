# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        node = head
        length = 0
        while node.next != None:
            length += 1
            node = node.next
        if length % 2 == 0:
            stop = length // 2
        else:
            stop = length // 2 + 1
        node = head
        count = 0
        while node != None:
            if count == stop:
                return node
            node = node.next
            count += 1