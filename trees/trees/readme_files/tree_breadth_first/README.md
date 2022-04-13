# Challenge Summary

> [Back](../../../README.md)

Write a function that traverse the binary tree in a breadth-first manner

## Whiteboard Process

![img](./Problem%20Solving%20Whiteboard%20Template.jpg)

## Approach & Efficiency

define the method breadth_first for the class Binarytree, it takes no arguments and return the items in the breadth-first way
if the tree was empty, raise an exception
define an initial list (output) and a queue (q), enqueue the root of the tree 
while the queue is not empty, keep looping and each time dequeue the front node and add it to the list output
check if the current front node has a left or right nodes, if yes, enqueue each one of them
return the output list

Big-O is o(n) for time because the while loop, and o(n) for space because the queue

## Solution

```
def breadth_first(self):

    if not self.root:
        raise(Exception("Tree is empty !"))

    output = []
    q = Queue()
    q.enqueue(self.root)
    

    while not q.is_empty():
        front = q.dequeue()
        output.append(front.value)
    
        if front.left:
            q.enqueue(front.left)

        if front.right:
            q.enqueue(front.right)
    
    return output
```

## Tests

```
def test_breadth_first(myBinaryTree):
    assert myBinaryTree.breadth_first() == [23, 8, 42, 4, 16, 27, 85, 15, 22, 105]

def test_breadth_first():
    with pytest.raises(Exception):
        BinaryTree().breadth_first()
    
@pytest.fixture
def myBinaryTree():
    tree = BinaryTree()
    tree.root = TNode(23)
    tree.root.left, tree.root.right = TNode(8), TNode(42)
    
    tree.root.left.left, tree.root.left.right = TNode(4), TNode(16)
    tree.root.left.right.left, tree.root.left.right.right = TNode(15), TNode(22)
    
    tree.root.right.left, tree.root.right.right = TNode(27), TNode(85)
    tree.root.right.right.right = TNode(105)
    
    return tree
```