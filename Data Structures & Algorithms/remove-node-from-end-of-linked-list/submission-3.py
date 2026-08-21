# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = ListNode(next=head)
        slow, fast = prev, head
        # init
        cnt = 0
        while fast and cnt < n:
            cnt += 1
            fast = fast.next

        # search
        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return prev.next