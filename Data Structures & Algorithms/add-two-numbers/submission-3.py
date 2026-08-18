# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        old_head = head = ListNode()
        carry = 0
        while l1 is not None or l2 is not None or carry != 0:
            if l1 is None:
                l1 = ListNode()
            if l2 is None:
                l2 = ListNode()
            val = l1.val + l2.val + carry;
            p = ListNode(val % 10)
            carry = val // 10
            head.next, head = (p, p)
            l1 = l1.next
            l2 = l2.next
        return old_head.next       
        