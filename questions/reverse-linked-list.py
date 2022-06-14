# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        new_node = ListNode(head.val)
        node = head.next
        while node != None:
            tmp_node = ListNode(node.val)
            tmp_node.next = new_node
            new_node = tmp_node
            node = node.next
        return new_node