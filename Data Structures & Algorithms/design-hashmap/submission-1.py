class ListNode:

    def __init__(self, key: int = -1, value: int = -1, next: Optional[ListNode] = None):
        self.key = key
        self.value = value
        self.next = next

class MyHashMap:

    def __init__(self):
        self.arr = [ListNode() for _ in range(10_000)]

    def hash(self, key) -> int:
        return key % 10_000

    def put(self, key: int, value: int) -> None:
        prev = self.arr[self.hash(key)]
        while prev.next:
            if prev.next.key == key:
                prev.next.key = key
                prev.next.value = value
                return
            prev = prev.next
        prev.next = ListNode(key, value)

    def get(self, key: int) -> int:
        prev = self.arr[self.hash(key)]
        while prev.next:
            if prev.next.key == key:
                return prev.next.value
            prev = prev.next
        return -1

    def remove(self, key: int) -> None:
        prev = self.arr[self.hash(key)]
        while prev.next and prev.next.key != key:
            prev = prev.next
        prev.next = prev.next.next if prev.next else None

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)