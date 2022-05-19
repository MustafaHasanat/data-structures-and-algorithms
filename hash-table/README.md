# Hashtables

Hashtable is a 

## Pull Requests



## Challenge

Implement a Hashtable Class with the following methods:



## Approach & Efficiency

I have created a class with initializing 3 attributes for it. First one is the size of the hash table (defalt as 1024). Second one is the map, which is a list of None values with the same number of the (size) attribute. the last one is the prime number we will use to hash values across the class.

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

