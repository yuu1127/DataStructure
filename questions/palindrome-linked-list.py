# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return true
        node = head
        vals = []
        while node != None:
            vals.append(node.val)
            node = node.next
        return vals == vals[::-1]
