class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyHashSet:

    def __init__(self):
        self.arr = [ListNode(-1, ListNode(-1)) for _ in range(10_000)]

    def hash(self, key:int) -> int:
        return key % 10_000

    def add(self, key: int) -> None:
        prev = self.arr[self.hash(key)]
        duplicate = False
        while prev.next.val != -1:
            prev = prev.next
            duplicate = True if prev.val == key else False
            if duplicate:
                return
        prev.next = ListNode(key, prev.next)

    def remove(self, key: int) -> None:
        prev = self.arr[self.hash(key)]
        while prev.next.val != -1 and prev.next.val != key:
            prev = prev.next
        if prev.next.val == -1:
            return
        temp = prev.next
        prev.next = prev.next.next
        del temp

    def contains(self, key: int) -> bool:
        prev = self.arr[self.hash(key)]
        while prev.next.val != -1:
            if prev.next.val == key:
                return True
            prev = prev.next
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)