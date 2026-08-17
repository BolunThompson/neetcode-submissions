"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        memo_table = {}
        start_new_head = new_head = Node(-1)
        while head is not None:
            p = memo_table.setdefault(id(head), Node(head.val))
            new_head.next = p
            new_head = p

            if head.random is not None:
                if id(head.random) in memo_table:
                    new_head.random = memo_table[id(head.random)]
                else:
                    memo_table[id(head.random)] = new_head.random = Node(head.random.val)

            head = head.next

                        
        return start_new_head.next
        