# Stacks and Queues

> [Back to main](../README.md)

We want to implement a "stack" and a "queue" data structues using python classes. The Stack is a data structure that has one gate for (in) and (out), and it follows the FILO (first in, last out) and the LIFO (last in, first out) concepts. The Queue is a data structure that has a gate for (in) and one for (out), and it follows the FIFO (first in, first out) and the LILO (last in, last out) concepts.

---

## Pull requests & README

- Challenge 10: Stack and Queue
    
    > [PR](https://github.com/Mustfa1999/data-structures-and-algorithms/pull/9)

- Challenge 11: Stack Queue Psuedo
    
    > [README](./readme_files/stack_queue_psuedo/README.md)

- Challenge 12: Stack Queue Animal Shelter
    
    > [README](./readme_files/stack_queue_animal_shelter/README.md)

---

## Challenge

Build 3 classes:

- Node: creates a node with a (value) and (pointer)

- Stack: creates a stack with a (top)

- Queue: creates a queue with a (front) and (back)

---

## Approach & Efficiency

Big(o) for both time and space in most methods is o(1), since we only deal with one element at a time

---

## API

- Node class : This class creates a Node with a given value and 
    a default pointer of (None)

- Stack class : This class creates a Stack with a default Top of (None)

    - str method : This method return a visual of the stack elements

    - push method : This method append a node value at the top of the stack

    - pop method : This method remove and return the top value of the stack

    - peek method : This method return the Top's value without removing it

    - is_empty method : This method checks if the stack is empty or not

- Queue class : This class creates a Queue with a default Front and Back of (None)s

    - enqueue method : This method put a node value at the back of the queue

    - dequeue method : This method delete the last node from the front of the queue

    - is_empty method : This method checks if the queue is empty or not

    - peek method : This method return the Front's value without removing it



