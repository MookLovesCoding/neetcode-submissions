# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = {} # Node : Index
        curr = head
        i = 0
        while curr is not None and curr.next is not None:
            if curr in seen:
                return True
            seen[curr] = seen.get(curr, i)
            i += 1
            curr = curr.next
        return False