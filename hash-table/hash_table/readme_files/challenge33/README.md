# Challenge 33

> [Back](../../../README.md)

## Challenge Summary

Write a function called left join

Arguments: two hash maps
The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.

Return: The returned data structure that holds the results is up to you. It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic

## Whiteboard Process

![img](./Problem%20Solving%20Whiteboard%20Template.jpg)

## Approach & Efficiency

define a list to hold the result
put the items of the first hashmap in the list
check for each item in the second hashmap if it exists in the list, and add it to it if so
if not, add a null value 
return the list 

Big-O :
for time: O(1) because we are looping through the whole hashmap no matter what is the filled items in it 
for space: O(n) because the length of the created list depends on the number of filled items 

## Solution

```
def hashmap_left_join(hashmap1, hashmap2):
    if not isinstance(hashmap1, HashTable) or not isinstance(hashmap2, HashTable):
        raise Exception("inputs must be hashmaps !")
    
    res = []
    
    for item in hashmap1.map:
        if item:
            if hashmap2.get(item[0][0]):
                res.append([item[0][0], item[0][1], hashmap2.get(item[0][0])[0][1]])
            else:
                res.append([item[0][0], item[0][1], None])
                
    return res
```
