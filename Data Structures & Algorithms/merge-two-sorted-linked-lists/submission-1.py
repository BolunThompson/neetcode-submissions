# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        original_head = head = ListNode(0, None)
        while head != None:
            if l1 is not None and (l2 is None or l1.val <= l2.val):
                head.next = head = l1
                l1 = l1.next
            elif l2 is not None and (l1 is None or l2.val < l1.val):
                head.next = head = l2
                l2 = l2.next
            else:
                break


        return original_head.next

