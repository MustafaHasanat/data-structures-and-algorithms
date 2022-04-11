class Node:
    """
    This class creates a Node with a given value and 
    a default pointer of (None)
    """
    
    def __init__(self, value):
        self.value = value
        self.pointer = None


class Stack:
    """
    This class creates a Stack with a default Top of (None)
    """
    
    def __init__(self):
        self.top = None

    def __str__(self):
        """
        This method return a visual of the stack elements
        """
        
        output = []
        current = self.top
        while current is not None:
            output.append(str(current.value))
            current = current.pointer
        return "Top -> " + " -> ".join(output)

    def push(self, value):
        """
        This method append a node value at the top of the stack
        """

        if not isinstance(value, Node):
            value = Node(value)
        value.pointer = self.top
        self.top = value

    def pop(self):
        """
        This method remove and return the top value of the stack
        """

        if self.is_empty():
            raise Exception("Stack is empty")
        temp = self.top
        self.top = self.top.pointer
        temp.pointer = None
        return temp.value 

    def peek(self):
        """
        This method return the Top's value without removing it
        """
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.top.value

    def is_empty(self):
        """
        This method checks if the stack is empty or not
        """
        
        return self.top is None

    def size(self):
        """
        This method return the size of the stack 
        """
        
        size = 0
        while not self.is_empty():
            size += 1
            self.pop()

        return size

    def reverse(self):
        rev = Stack()
        if self.is_empty: rev 

        while not self.is_empty():
            rev.push(self.pop())

        return rev
    
    @staticmethod
    def validate_brackets(string):
        if not type(string) == str: 
            raise Exception("Invalid input !")
        
        pairs = {"(": ")", "[": "]", "{": "}"}
        stack = Stack()
        
        for i in string:
            if i in pairs.keys():
                stack.push(i)
            
            elif i in pairs.values():
                if stack.is_empty():
                    return False
                elif i == pairs.get(stack.peek()):
                    stack.pop()
                    continue
                else:
                    return False
        
        return True if stack.is_empty() else False


class Queue:
    """
    This class creates a Queue with a default Front and Back of (None)s
    """
    
    def __init__(self):
        self.front = None
        self.back = None

    def __str__(self):
        """
        This method return a visual of the queue elements
        """
        
        output = []
        current = self.front
        while current is not None:
            output.append(str(current.value))
            current = current.pointer
        return "Front -> " + " -> ".join(output) + " <- Back"

    def enqueue(self, value):
        """
        This method put a node value at the back of the queue
        """

        if not isinstance(value, Node):
            value = Node(value)

        if self.is_empty():
            self.front, self.back = value, value
        else:
            self.back.pointer = value
            self.back = value

    def dequeue(self):
        """
        This method delete the last node from the front of the queue
        """
        
        if self.is_empty():
            raise Exception("Queue is empty")
        if self.front.value == self.back.value:
            value = self.front.value
            self.front, self.back = None, None
            return value

        temp = self.front
        self.front = self.front.pointer
        temp.pointer = None
        return temp.value 

    def is_empty(self):
        """
        This method checks if the queue is empty or not
        """
        
        return self.front is None and self.back is None

    def peek(self):
        """
        This method return the Front's value without removing it
        """

        if self.is_empty():
            raise Exception("Queue is empty")
        return f"{self.front.value}"
    

    @staticmethod
    def DuckDuckGoose(strings: list, k: int):
        if (type(strings) != list) or (type(k) != int):
            raise Exception("Invalid input !")
        
        q = Queue()
        [q.enqueue(i) for i in strings]

        for _ in range(len(strings)-1):
            [q.enqueue(q.dequeue()) for _ in range(k-1)]
            q.dequeue() 

        return q.front.value





if __name__ == "__main__":
    print(Queue.DuckDuckGoose(["A", "B", "C", "D", "E"], 3))
 