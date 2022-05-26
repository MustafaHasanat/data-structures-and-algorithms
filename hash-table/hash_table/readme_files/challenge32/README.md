# Challenge 32

> [Back](../../../README.md)

## Challenge Summary

Write a function called tree_intersection that takes two binary trees as parameters.
Using your Hashmap implementation as a part of your algorithm, return a set of values found in both trees.

## Whiteboard Process

![img](./Problem%20Solving%20Whiteboard%20Template.jpg)

## Approach & Efficiency

create a function called (tree_intersection) that takes two trees as arguments
check if both inputs are binary trees
create an empty hash table
insert all the nodes from the first tree to the hash table
check for each node in the second tree if it exists in the hash table and get the matches
return a list of those matches

Big-O :
for time: o(n), because we used a for-loop and traersed a tree 
for space: o(n), because we created a list with variable size

## Solution

```
def tree_intersection(tree1, tree2):    

    if not isinstance(tree1, BinaryTree) or not isinstance(tree2, BinaryTree):
        raise TypeError("tree1 and tree2 must be BinaryTree")

    hash_table = HashTable()
    for node in tree1.pre_order():
        hash_table.set(str(node), node)
        
    common = [node for node in tree2.pre_order() if hash_table.get(str(node))]

    return common
```
