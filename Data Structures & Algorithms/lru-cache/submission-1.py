class ListNode:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = ListNode(0,0)
        self.right = ListNode(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            use = self.cache.get(key)
            self.remove(use)
            self.insert(use)
            return use.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            get = self.cache.get(key)
            self.remove(get)
        put = ListNode(key, value)
        self.cache[key] = put 
        self.insert(put)
        if len(self.cache) > self.capacity:
            out = self.left.next
            self.remove(out)
            del self.cache[out.key]
    
    def remove(self, node):
        prior = node.prev
        prior.next = node.next
        after = node.next
        after.prev = prior
    def insert(self, node):
        placer = self.right.prev 
        placer.next = node
        node.prev = placer
        node.next = self.right
        self.right.prev = node



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)