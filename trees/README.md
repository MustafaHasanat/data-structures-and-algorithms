# Trees

> [Back to main](../README.md)

Node - A Tree node is a component which may contain its own values, and references to other nodes
Root - The root is the node at the beginning of the tree
K - A number that specifies the maximum number of children any node may have in a k-ary tree. In a binary tree, k = 2.
Left - A reference to one child node, in a binary tree
Right - A reference to the other child node, in a binary tree
Edge - The edge in a tree is the link between a parent and child node
Leaf - A leaf is a node that does not have any children
Height - The height of a tree is the number of edges from the root to the furthest leaf

---

## Pull Requests:

> [PR 1: trees](https://github.com/Mustfa1999/data-structures-and-algorithms/pull/13)

> [PR 2: trees max](https://github.com/Mustfa1999/data-structures-and-algorithms/pull/14)

> [PR 3: breadth first]()

---

## Challenges:

> [tree max](./trees/readme_files/trees_max/README.md)

> [ breadth first](./trees/readme_files/tree_breadth_first/README.md)

---

## Challenge

- Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.
Binary Tree

- Create a Binary Tree class, Define a method for each of the depth first traversals: pre order, in order, post order, which returns an array of the values, ordered appropriately.

- Binary Search Tree, Create a Binary Search Tree class, This class should be a sub-class of the Binary Tree Class, with the following additional methods:

    - Add

        Arguments: value
        Return: nothing
        Adds a new node with that value in the correct location in the binary search tree.

    - Contains

        Argument: value
        Returns: boolean indicating whether or not the value is in the tree at least once.

---

## Approach & Efficiency

I used the recursion inner function to traverse each tree and track its values. And inside that recursive function, I implemented the special feature of each individual method.

Big-O for the methods:

- pre_order 
    - o(n) for time because it is a recursive function
    - o(n) for space because it appends items to a new list 

- in_order
    - o(n) for time because it is a recursive function
    - o(n) for space because it appends items to a new list

- post_order
    - o(n) for time because it is a recursive function
    - o(n) for space because it appends items to a new list

- add
    - o(log(n)) for time because the tree size is decreasing over each iteration 
    - o(1) for space because we only created one variable to hold the current value

- contains
    - o(log(n)) for time because the tree size is decreasing over each iteration 
    - o(1) for space because we only created one variable to hold the current value

---

## API

### BinaryTree class

pre_order

    Input: None
    doing: traverse a tree (pre-order --> root-left-right)
    output: print values of the nodes of the tree

in_order

    Input: None
    doing: traverse a tree (in-order --> left-root-right)
    output: print values of the nodes of the tree


post_order

    Input: None
    doing: traverse a tree (post-order --> left-right-root)
    output: print values of the nodes of the tree

### BinaryTreeSearch class

add

    input: value
    doing: add the value correctly to the tree
    output: None

contains
   
    input: value
    doing: check if the value is in the tree at least once
    output: boolean 