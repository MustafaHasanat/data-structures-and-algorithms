# Challenge Summary

> [Back](../../../README.md)

Write a function that that returns the maximum value from a binary search tree

## Whiteboard Process

![img](./Problem%20Solving%20Whiteboard%20Template.jpg)

## Approach & Efficiency

define an algorithm find_max()
raise an exception if the tree is empty, or return the root value if the tree only have one node (the root)
define (maximum) that holds the value of the root value, and define (current) that holds the root node
keep looping and change the current to be its right and save it in (maximum) until it reaches the None value
return the maximum 

Big-O for time is o(log(n)) because the length of the list is decreasing over each iteration
Big-O for space is o(1) because we only created two variables to hold the current and the maximum values 

## Solution

```
def find_max(self):
    if not self.root:
        raise(Exception("Tree is empty !"))
    
    if not self.root.left and not self.root.right:
        return self.root.value

    maximum = self.root.value
    current = self.root
            
    while True:
        if current.right:
            current = current.right                
            maximum = current.value
        else:
            return maximum
```

## Tests

```
def test_find_maximum_value(myTreeSearch):
    assert myTreeSearch.find_max() == 105

def test_find_maximum_value_on_empty_tree():
    with pytest.raises(Exception):
        BinaryTreeSearch().find_max()
```