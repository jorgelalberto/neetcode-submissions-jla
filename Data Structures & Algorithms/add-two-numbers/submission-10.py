# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def add(node1: ListNode, node2: ListNode) -> List:
            node1 = node1 if node1 else ListNode(val=0)
            node2 = node2 if node2 else ListNode(val=0)
            ansNum = node1.val + node2.val
            carry = 1 if ansNum >= 10 else 0
            return [carry, ListNode(ansNum%10)]

        curr = ListNode()
        ans = curr
        finalCarry = 0

        while l1 or l2:
            carry, node = add(l1, l2)

            curr.next = node

            if carry == 1:
                if l1 and l1.next:
                    l1.next.val += carry
                elif l2 and l2.next:
                    l2.next.val += carry
                else:
                    finalCarry += 1
            curr = curr.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2



        curr.next = ListNode(finalCarry) if finalCarry else None

        return ans.next
