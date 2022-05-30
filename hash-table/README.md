# Hashtables

Hashtable is a list of lists. Each sub list contains pairs of items, the hashed key and its value. The hashed key is generated based on the ASCII values of the key, so we can have multiple pairs linked with the same index of the table. 

## Pull Requests

> [PR](https://github.com/Mustfa1999/data-structures-and-algorithms/pull/24)

---

## Challenges

Implement a Hashtable lass with the methods: set, get, contains, keys, hash

> [challenge 31](./hash_table/readme_files/challenge31/README.md)

> [challenge 32](./hash_table/readme_files/challenge32/README.md)

> [challenge 33](./hash_table/readme_files/challenge33/README.md)

---

## Approach & Efficiency

I have created a class with initializing 3 attributes for it. First one is the size of the hash table (defalt as 1024). Second one is the map, which is a list of None values with the same number of the (size) attribute. the last one is the prime number we will use to hash values across the class.

---

## API

The class (HashTable) has the following methods:

- set

    Arguments: key, value
    
    Returns: nothing
    
    Doing: This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
    Should a given key already exist, replace its value from the value argument given to this method.

- get

    Arguments: key

    Returns: Value associated with that key in the table

- contains

    Arguments: key
    
    Returns: Boolean, indicating if the key exists in the table already.

- keys
  
    Returns: Collection of keys

- hash
  
    Arguments: key
  
    Returns: Index in the collection for that key

