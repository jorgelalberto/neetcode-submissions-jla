# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        secondHalfStart = slow.next
        slow.next = None

        # reverse second half
        secondHalfStartPrev = None
        head2 = None
        while secondHalfStart:
            currNxt = secondHalfStart.next # None
            secondHalfStart.next = secondHalfStartPrev # LN(8).next = LN(6)
            secondHalfStartPrev = secondHalfStart
            secondHalfStart = currNxt
        head2 = secondHalfStartPrev

        # merge first (head) and second (head2) halves
        while head and head2:
            tmpHeadNxt = head.next
            tmpHead2Nxt = head2.next
            head.next = head2
            head2.next = tmpHeadNxt
            head = tmpHeadNxt
            head2 = tmpHead2Nxt

        return None
