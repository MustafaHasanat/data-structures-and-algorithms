from stack_and_queue.stack_and_queue import Node, Stack


class PseudoQueue:
    """
    Implements a Queue using two Stacks.
    """
    
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        """
        Inserts value into the PseudoQueue, using a first-in, first-out approach.
        """

        self.stack1.push(value)

    def dequeue(self):
        """
        Extracts a value from the PseudoQueue, using a first-in, first-out approach.
        """
        
        if not self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())

        if not self.stack1.is_empty():
            return self.stack1.pop()
        else:
            raise(Exception("Pseudo Queue is empty !"))


    def is_empty(self):
        """
        """

        return True if self.stack1.is_empty() and self.stack2.is_empty() else False

    
    def size(self):
        """
        """
        
        return self.stack1.size() + self.stack2.size()

    def front(self):
        """
        """

        if not self.stack2.is_empty():
            return self.stack2.peek()
        elif not self.stack1.is_empty():
            return self.stack1.reverse().peek()
        else:
            raise(Exception("Pseudo Queue is empty !"))

    



         

