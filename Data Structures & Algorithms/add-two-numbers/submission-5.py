# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        len1 = 0
        getLen1 = l1
        while getLen1:
            len1 += 1
            getLen1 = getLen1.next
        len2 = 0
        getLen2 = l2
        while getLen2:
            len2 += 1
            getLen2 = getLen2.next

        def add(node1: ListNode, node2: ListNode) -> List:
            ansNum = node1.val + node2.val
            carry = 1 if ansNum >= 10 else 0
            return [carry, ListNode(ansNum%10)]

        curr = ListNode()
        ans = curr
        carry = 0

        while l1 and l2:
            l2.val = l2.val + carry
            carry, node = add(l1, l2)
            curr.next = node

            curr = curr.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            carry, node = add(l1, ListNode(carry))
            curr.next = node

            curr = curr.next
            l1 = l1.next

        while l2:
            carry, node = add(l2, ListNode(carry))
            curr.next = node

            curr = curr.next
            l2 = l2.next

        curr.next = ListNode(carry) if carry==1 else None

        return ans.next