# Challenge Summary

> [Back](../../../README.md)

Write a function that that returns the maximum value from a binary search tree

## Whiteboard Process

![img](./Problem%20Solving%20Whiteboard%20Template.jpg)

## Approach & Efficiency

define an algorithm find_max()
raise an exception if the tree is empty
return the root value if the tree only have one node (the root)
define (maximum) that holds the value of the root value
define a recursive loop by a function that will traverse through the tree
in each recursion, check if the current value is bigger than the current max and modify it accordingly 
return the maximum 

Big-O is o(n) for time because the rucrsive internal function, and o(1) for space because we only created one variable to hold the max value

## Solution

```
def find_max(self):
        if not self.root:
            raise(Exception("Tree is empty !"))
        
        if not self.root.left and not self.root.right:
            return self.root.value

        maximum = self.root.value
                
        def _walk(node):
            nonlocal maximum 

            if node.value > maximum:
                maximum = node.value
            
            if node.left:
                _walk(node.left)

            if node.right:
                _walk(node.right)
                
        _walk(self.root)
        
        return maximum
```

## Tests

```
def test_find_maximum_value(myBinaryTree):
    assert myBinaryTree.find_max() == 105

def test_find_maximum_value_on_empty_tree():
    with pytest.raises(Exception):
        BinaryTree().find_max()

@pytest.fixture
def myBinaryTree():
    tree = BinaryTree()
    tree.root = TNode(23)
    tree.root.left, tree.root.right = TNode(27), TNode(42)
    
    tree.root.left.left, tree.root.left.right = TNode(4), TNode(16)
    tree.root.left.right.left, tree.root.left.right.right = TNode(105), TNode(22)
    
    tree.root.right.left, tree.root.right.right = TNode(8), TNode(85)
    tree.root.right.right.right = TNode(15)
    
    return tree
```