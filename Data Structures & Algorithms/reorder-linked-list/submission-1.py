# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # get to middle of list
        left, right = head, head.next
        while right and right.next:
            right = right.next.next
            left = left.next
        # reverse second half of list
        second = left.next
        prev = left.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        # merge two lists together
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2