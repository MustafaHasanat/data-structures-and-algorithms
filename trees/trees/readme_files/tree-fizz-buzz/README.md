# Challenge Summary

> [Back](../../../README.md)

Write a function called fizz_buzz_tree that applies the Fizz Buzz game on a tree of integers and turn the values to string 


## Whiteboard Process

![img]()

## Approach & Efficiency

define a function (fizz_buzz_tree) that takes a tree as an argument 
if the tree is empty or any of its alues is not integer, raise an error
create new tree 
traverse throught the tree's values as (pre-order) and apply the FizzBuzz game's rules on each node 
change the value of each node accordinally 
return the new tree 

Big-O is o(n) for time because the rucrsive internal function, and o(n) for space because we created a new tree

## Solution

```
def fizz_buzz_tree(tree):
    """
    traversing through the tree and create a new one.
    Set the values of nodes according to the FizzBuzz game
    """
    
    if not tree.root:
        raise(Exception("Tree is empty !"))

    newTree = BinaryTreeSearch()
    newTree.root = tree.root 
        
    def _walk(node):
        
        if node.left:
            _walk(node.left)

        if node.right:
            _walk(node.right)
            
        if not str(node.value).isdigit(): 
            raise Exception("All values must be integers !")
        
        if node.value%3==0 and node.value%5==0:
            node.value = "FizzBuzz"
        elif node.value%5==0:
            node.value = "Buzz"
        elif node.value%3==0:
            node.value = "Fizz"
        else:
            node.value = str(node.value)

    _walk(newTree.root)
            
    return newTree
```

## Tests

```
def test_fizz_buzz_tree():
    tree = BinaryTreeSearch()
    tree.root = TNode(23) 
    [tree.add(i) for i in [8,4,16,15,22,42,27,85,105]]
    assert fizz_buzz_tree(tree).pre_order() == ['23', '8', '4', '16', 'FizzBuzz', '22', 'Fizz', 'Fizz', 'Buzz', 'FizzBuzz'] 


def test_fizz_buzz_tree_empty():
    with pytest.raises(Exception):
        fizz_buzz_tree(BinaryTreeSearch())
```