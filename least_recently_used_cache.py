"""
To implement a Least Recently Used (LRU) cache efficiently, I have used a combination of a hash table and a doubly linked list.
The hash table will allow us to quickly look up key-value pairs by key, while the doubly linked list will allow us to efficiently 
track the least recently used item.

Here's an implementation in Python:
"""


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.add(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self.add(node)
        if len(self.cache) > self.capacity:
            node = self.head.next
            self.remove(node)
            del self.cache[node.key]

    def delete(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            del self.cache[key]
            return node.val
        else:
            return -1

    def add(self, node: Node) -> None:
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node: Node) -> None:
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
