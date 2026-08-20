# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        listLen = 0

        # get list length
        temp = head
        while temp.next:
            listLen += 1
            temp = temp.next
        listLen += 1
        # get start of second half of list
        secondHalfStart = head
        cnt = 0
        while cnt < (listLen // 2):
            cnt += 1
            secondHalfStart = secondHalfStart.next
        tmpNxt = secondHalfStart.next
        secondHalfStart.next = None
        secondHalfStart = tmpNxt

        # reverse second half
        secondHalfStartPrev = None
        head2 = None
        while secondHalfStart:
            prevNxt = secondHalfStart # LN(8)
            currNxt = secondHalfStart.next # None

            secondHalfStart.next = secondHalfStartPrev # LN(8).next = LN(6)

            secondHalfStartPrev = prevNxt
            secondHalfStart = currNxt
        head2 = secondHalfStartPrev

        # merge first (head) and second (head2) halves
        ans = head
        while head2 and head:
            tmpHeadNxt = head.next
            tmpHead2Nxt = head2.next
            head.next = head2
            head2.next = tmpHeadNxt
            head = tmpHeadNxt
            head2 = tmpHead2Nxt

        return None
