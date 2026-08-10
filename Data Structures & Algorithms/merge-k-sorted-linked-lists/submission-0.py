# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        elif len(lists) == 2:
            return self.merge(lists[0], lists[1])
        newList = []
        if len(lists) % 2 != 0:
            newList.append(lists.pop())
        for i in range(1, len(lists), 2):
            newList.append(self.merge(lists[i], lists[i - 1]))
        return self.mergeKLists(newList)
    def merge(self, one: Optional[ListNode], two: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        while one and two:
            if one.val <= two.val:
                curr.next = one
                curr = curr.next
                one = one.next
            else:
                curr.next = two
                curr = curr.next
                two = two.next
        if not one and two:
            curr.next = two
        elif not two and one:
            curr.next = one
        return dummy.next