# Singly and Doubly Linked Lists

> [Back to main](../README.md)

A singly and doubly linked lists project that can create linked lists and nodes.
It also can append, insert, delete, reverse, slice, and print nodes from a linked list. 

---

## Pull Requests

> [Singly Linked List PR](https://github.com/Mustfa1999/data-structures-and-algorithms/pull/4)

> [Doubly & Singly Linked Lists PR](https://github.com/Mustfa1999/data-structures-and-algorithms/pull/5)

> [Kth element](https://github.com/Mustfa1999/data-structures-and-algorithms/pull/7)

---

## Challenge 06 Summary

> [Challenge 06](./Challenge6/README.md)

---

## Challenge 07 Summary

> [Challenge 07](./Challenge7/README.md)

---

## Challenge

Create two classes for creating singly linked lists and nodes.
Add functions that can append, insert, and print nodes from a linked list. 

---

## Approach & Efficiency

I created (Node) class which takes a value of any type as an argument and have a pointer of (None) type as default.
I also created (LinkedList) class which takes no arguments and create an empty linked list. 

Then I created (DoublyNode) class which takes a value of any type as an argument and have a pointer of (DoublyNone) type as default.
I also created (DoublyLinkedList) class which takes no arguments and create an empty doubly linked list. 

---

## Streatch Goal

Implement a doubly linked list (completely separate from your singly linked list).

---

## API

### Classes (LinkedList) and (DoublyLinkedList) each one has these methods:

- **ToString(self)**:

    This function represents the Linked List as a concatonated string that has all its nodes 

- **Insert(self, value)**:

    This function inserts a value at the (beginning) of the linked list

- **InsertBefore(self, new_value, value)**:

    This function inserts the (new value) before the (value) of the linked list if it does exist

- **InsertAfter(self, new_value, value)**:
    
    This function inserts the (new value) after the (value) of the linked list if it does exist

- **Includes(self, value)**:

    This function checks if the provided value is in the linked list or not and return a Boolean 
    The (value) can be either (Node) instances or any other type, because the method will turn everything to a (Node) instance if it wasn't.

- **Append(self, value)**:

    This function inserts a value (Node instance) at the (end) of the linked list
    The (value) can be either (Node) instances or any other type, because the method will turn everything to a (Node) instance if it wasn't. 

- **Replace(self, value, new)**:

    This function replaces the (value) from the linked list with the (new) value if it does exist in it. Otherwise, it raise an error.
    Both (value) and (new) can be either (Node) instances or any other type, because the method will turn everything to a (Node) instance if it wasn't. 

- **Delete(self, value)**:

    This function deletes a value from the linked list if it does exist in it. Otherwise, it raise an error.
    The (value) can be either (Node) instances or any other type, because the method will turn everything to a (Node) instance if it wasn't. 

- **Slice(self, From=None, To=None)**:

    This function slices the linked list from the node (From) till the node (To) and returns a new linked list that contains the nodes from the (From) node to the (To) node.
    Both (From) and (To) can be either (Node) instances or any other type, because the method will turn everything to a (Node) instance if it wasn't. 

- **Reverse(self)**:

    This function reverse the order of the list then return a new list.

---
