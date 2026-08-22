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
        newPrev = Node(-1)
        new = None
        ans = newPrev

        head_to_new = {}
        while head:
            rand = head_to_new.get(head.random) if (head.random == None or head_to_new.get(head.random)) else Node(head.random.val, None, None)
            head_to_new[head.random] = rand

            new = head_to_new.get(head) if head_to_new.get(head) != None else Node(head.val, None, rand)
            head_to_new[head] = new
            new.random = head_to_new[head.random]

            newPrev.next = new
            randr = new.random if not new.random else new.random.val

            newPrev = new
            new = new.next
            head = head.next
        return ans.next
