# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        def count(head):
            i = 0
            while head != None:
                head = head.next
                i += 1
            return i
                
        def take(head, n):
            i = 0
            old_head = head
            prev_head = None
            while i < n and head is not None:
                prev_head = head
                head = head.next
                i += 1
            if prev_head is not None:
                prev_head.next = None
            return old_head, head
        
        def reverse(head) -> None:
            prev_head = None
            while head is not None:
                head.next, head, prev_head = prev_head, head.next, head
            return prev_head

 
        def interleave(l1, l2) -> None:
            head = ListNode()
            done = False
            while not done:
                for i in range(1, 3):
                    if l1 is None and l2 is None:
                        done = True
                        break
                    elif l2 is None or i == 1:
                        head.next = l1
                        head = l1
                        l1 = l1.next
                    elif l1 is None or i == 2:
                        head.next = l2
                        head = l2
                        l2 = l2.next
                    else:
                        assert False

        length = count(head)
        first_half_len = length - length // 2
        first_half, second_half = take(head, first_half_len)
        second_half = reverse(second_half)
        interleave(first_half, second_half)
