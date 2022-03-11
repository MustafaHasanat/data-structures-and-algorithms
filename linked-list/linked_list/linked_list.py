class Node:
    """
    This class is used to create a node that will be
    used in a linked list

    a (Node) instance consists of a (value) that holds 
    the node's value, and a (pointer) that holds the 
    address of the next node
    """

    def __init__(self, value):
        self.value = value
        self.pointer = None


    def __str__(self):
        return self.value


class LinkedList:
    """
    This class is used to create a linked list using nodes,
    and each node is an instance of the class (Node)

    a (LinkedList) instance have only one attribute (head), which
    represents the first node in the linked list
    """


    def __init__(self):
        self.head = None


    def __str__(self):
        return self.ToString()


    def ToString(self):
        """
        This function represents the Linked List as a 
        concatonated string that has all its nodes 
        """
        
        output = ""
        if self.head is None:
            output = "None"
        else:
            current = self.head
            while current:
                output += f"{current.value} -> "
                current = current.pointer
            output += "NULL"
        return output


    def Insert(self, value):
        """
        This function inserts a value (Node instance) at the 
        (beginning) of the linked list
        """
        
        if self.head is None:
            self.head = value
        else:
            value.pointer = self.head
            self.head = value
    

    def Includes(self, value):
        """
        This function checks if the provided value is 
        in the linked list or not and return a Boolean
        """

        if self.head is None:
            return False
        else:
            current = self.head
            while current.value is not None:
                if value == current.value:
                    return True
                current = current.pointer
                if current is None:
                    return False
            return False


    def Append(self, value):
        """
        This function inserts a value (Node instance) at 
        the (end) of the linked list
        """

        if self.head is None:
            self.head = value
        else:
            current = self.head
            while current.pointer is not None:
                current = current.pointer
            current.pointer = value
