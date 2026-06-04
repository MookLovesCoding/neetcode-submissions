# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()
        a, b = list1, list2
        while a and b:
            if a.val < b.val:
                node.next = a
                node = node.next
                a = a.next
            else:
                node.next = b
                node = node.next
                b = b.next
        node.next = a or b
        return dummy.next