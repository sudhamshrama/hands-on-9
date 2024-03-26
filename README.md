**Title: Hash Table Implementation in Python with Dynamic Resizing**

**Introduction:**
This project presents an implementation of a hash table data structure in Python. The hash table uses the multiplication and division method for the hash function, resolves collisions by chaining with a doubly linked list, and supports dynamic resizing to accommodate changing load factors.

**Features:**
1. Hash table implementation using multiplication and division method for the hash function.
2. Collision resolution by chaining with a doubly linked list.
3. Dynamic resizing: 
   - Doubles the array size and re-hashes everything when the table is full.
   - Halves the size of the array and re-hashes everything when the table is becoming empty.

**Implementation Details:**
- The hash function is implemented using the multiplication and division method: `(key * 2654435761) % capacity`.
- Collision resolution is achieved by chaining with a doubly linked list. Each bucket in the hash table maintains a linked list of key-value pairs.
- Dynamic resizing is triggered based on the load factor:
  - When the table is full (load factor exceeds 0.75), the array size is doubled and all elements are re-hashed.
  - When the table is becoming empty (load factor drops below 0.25), the array size is halved (minimum capacity of 8) and all elements are re-hashed.

**Usage:**
- Create a new `HashTable` object.
- Use the `insert(key, value)` method to insert key-value pairs into the hash table.
- Use the `remove(key)` method to remove a key-value pair from the hash table.
- Use the `search(key)` method to search for a value associated with a key in the hash table.

**Example:**
```python
hash_table = HashTable()
hash_table.insert(1, 10)
hash_table.insert(2, 20)
hash_table.insert(9, 90)
print(hash_table.search(1))  # Output: 10
print(hash_table.search(2))  # Output: 20
print(hash_table.search(9))  # Output: 90
hash_table.remove(2)
print(hash_table.search(2))  # Output: None
```
