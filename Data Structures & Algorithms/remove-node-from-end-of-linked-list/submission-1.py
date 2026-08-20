# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        listLen = 0
        tmp = head
        while tmp:
            listLen += 1
            tmp = tmp.next

        if listLen == 1:
            return None

        cnt = 0
        start = ListNode(next=head)
        prev = start
        while cnt < listLen-n:
            cnt+=1
            prev = head
            head = head.next
        prev.next = head.next

        return start.next