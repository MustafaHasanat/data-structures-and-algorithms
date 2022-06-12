# Graphs

![img](https://miro.medium.com/max/1066/1*Hqedss67usGXJEx0qH4e1w.jpeg)

## Pull Requests

> [PR 1](https://github.com/Mustfa1999/data-structures-and-algorithms/pull/31)

---

## Challenges

Implement a Graph. The graph should be represented as an adjacency list, and should include the following methods:

add node, add edge, get nodes, get neighbors, size

---

## Approach & Efficiency

I have created a 3 class for creating the Node, Edge, and Graph.
Each one has a special initialized attributes to implement it:

Node Class:

- It creates a Graph Node and its object takes only one argument (value) and assign it as the value of the node

Edge Class: 

- It creates a Graph Edge and its object takes two arguments. The (Value) which is the node itself, and the (Weight) which is the wieght of that edge

Graph Class: 

- It creates a Graph by initializing an adjacency list that represent the whole graph. 

- The Adjacency list is a list of pairs that mentions all connections (edges) between nodes. Here, it is represented by a dictionary where the key of the pair is a Node, and the value is a list that has all edges that are connecting this Node with others (this list is initialized as an empty list)

## API

The class (Graph) has the following methods:

- add node

Arguments: value
Returns: The added node
Add a node to the graph

- add edge

Arguments: 2 nodes to be connected by the edge, weight (optional)
Returns: nothing
Adds a new edge between two nodes in the graph
If specified, assign a weight to the edge
Both nodes should already be in the Graph

- get nodes

Arguments: none
Returns all of the nodes in the graph as a collection (set, list, or similar)

- get neighbors

Arguments: node
Returns a collection of edges connected to the given node
Include the weight of the connection in the returned collection

- size

Arguments: none
Returns the total number of nodes in the graph
