# Graphs

![img](https://miro.medium.com/max/1066/1*Hqedss67usGXJEx0qH4e1w.jpeg)

## Pull Requests

---

## Challenges

Implement a Graph. The graph should be represented as an adjacency list, and should include the following methods:

add node, add edge, get nodes, get neighbors, size

---

## Approach & Efficiency

I have created a class with initializing attributes 
---

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
