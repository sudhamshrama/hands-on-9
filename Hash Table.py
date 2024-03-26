class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, key, value):
        new_node = Node(key, value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove(self, key):
        current = self.head
        while current:
            if current.key == key:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                return
            current = current.next

    def search(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

class HashTable:
    def __init__(self, initial_capacity=8, load_factor=0.75):
        self.capacity = initial_capacity
        self.size = 0
        self.load_factor = load_factor
        self.buckets = [DoublyLinkedList() for _ in range(self.capacity)]

    def hash_function(self, key):
        return (key * 2654435761) % self.capacity

    def resize(self, new_capacity):
        old_buckets = self.buckets
        self.capacity = new_capacity
        self.buckets = [DoublyLinkedList() for _ in range(self.capacity)]
        self.size = 0
        for bucket in old_buckets:
            current = bucket.head
            while current:
                self.insert(current.key, current.value)
                current = current.next

    def insert(self, key, value):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        if bucket.search(key) is None:
            bucket.append(key, value)
            self.size += 1
            if self.size > self.load_factor * self.capacity:
                self.resize(self.capacity * 2)

    def remove(self, key):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        if bucket.search(key) is not None:
            bucket.remove(key)
            self.size -= 1
            if self.size < (1 / 4) * self.capacity:
                self.resize(max(self.capacity // 2, 8))

    def search(self, key):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        return bucket.search(key)

# Example usage:
hash_table = HashTable()
hash_table.insert(1, 10)
hash_table.insert(2, 20)
hash_table.insert(9, 90)
print(hash_table.search(1))  # Output: 10
print(hash_table.search(2))  # Output: 20
print(hash_table.search(9))  # Output: 90
hash_table.remove(2)
print(hash_table.search(2))  # Output: None
