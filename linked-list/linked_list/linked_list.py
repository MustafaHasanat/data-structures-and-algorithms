
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

#==============================================
#===========    Required methods    ===========
#==============================================

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
            while current is not None:
                output += f"{current.value} -> "
                current = current.pointer
            output += "NULL"

        return output


    def Insert(self, value, after_node=None):
        """
        This function inserts a value at the (beginning) of the 
        linked list if the argument (after_node) wasn't provided.
        Otherwise, it will insert the (value) after the provided node
        value (after_node) 

        Both (value) and (after_node) can be either (Node) instances or
        any other type, because the method will turn everything to a 
        (Node) instance if it wasn't. 
        """
        
        if value is None:
            raise Exception("The provided values must not be (None) !")

        if not isinstance(value, Node):
            value = Node(value)

        if self.head is None:
            self.head = value
        
        else:
            if after_node is None:
                value.pointer = self.head
                self.head = value
            
            else:
                if not isinstance(after_node, Node):
                    after_node = Node(after_node)
                current = self.head

                while current.pointer is not None:
                    if current.value == after_node.value:
                        value.pointer, current.pointer = current.pointer, value
                        return 0
                    current = current.pointer
                else:            
                    if current.value == after_node.value:
                        value.pointer, current.pointer = current.pointer, value
                        return 0
                
                raise Exception(f"The linked list has no value named \'{after_node}\' !")
                
                
    def Includes(self, value):
        """
        This function checks if the provided value is 
        in the linked list or not and return a Boolean

        The (value) can be either (Node) instances or 
        any other type, because the method will turn 
        everything to a (Node) instance if it wasn't. 
        """

        if value is None:
            raise Exception("The provided value must not be (None) !")
            
        if not isinstance(value, Node):
            value = Node(value)

        if self.head is None:
            return False

        else:
            current = self.head
            while current.pointer is not None:
                if value.value == current.value:
                    return True
                current = current.pointer
            else:
                if value.value == current.value:
                    return True

            return False


#================================================
#===========    Additional methods    ===========
#================================================


    def Append(self, value):
        """
        This function inserts a value (Node instance) at 
        the (end) of the linked list

        The (value) can be either (Node) instances or 
        any other type, because the method will turn 
        everything to a (Node) instance if it wasn't. 
        """

        if value is None:
            raise Exception("The provided value must not be (None) !")

        if not isinstance(value, Node):
            value = Node(value)

        if self.head is None:
            self.head = value
        else:
            current = self.head
            while current.pointer is not None:
                current = current.pointer
            else:
                current.pointer = value


    def Replace(self, value, new):
        """
        This function replaces the (value) from 
        the linked list with the (new) value if 
        it does exist in it.
        Otherwise, it raise an error.

        Both (value) and (new) can be either (Node) instances or
        any other type, because the method will turn everything to a 
        (Node) instance if it wasn't. 
        """

        if (value is None) or (new is None):
            raise Exception("The provided values must not be (None) !")
        
        if not isinstance(value, Node):
            value = Node(value)

        if not isinstance(new, Node):
            new = Node(new)

        if not self.Includes(value.value):
                raise Exception("The provided value isn't existed in the Linked list !")

        if self.head is None:
            raise Exception("The linked list is empty !")
        elif self.head.value == value.value:
            self.head.value = new.value
        else:
            current = self.head
            while current.pointer is not None:
                if current.value == value.value:
                    current.value = new.value
                    return 0
                current = current.pointer
            else:
                if current.value == value.value:
                    current.value = new.value
                    return 0


    def Delete(self, value):
        """
        This function deletes a value from 
        the linked list if it does exist in it.
        Otherwise, it raise an error.

        The (value) can be either (Node) instances or 
        any other type, because the method will turn 
        everything to a (Node) instance if it wasn't. 
        """

        if value is None:
            raise Exception("The provided value must not be (None) !")

        if not isinstance(value, Node):
            value = Node(value)

        if not self.Includes(value.value):
                raise Exception("The provided value isn't existed in the Linked list !")

        if self.head is None:
            raise Exception("The linked list is empty !")
        elif self.head.value == value.value:
            self.head = self.head.pointer
        else:
            current = self.head
            while current.pointer is not None:
                if current.pointer.value == value.value:
                    current.pointer = current.pointer.pointer
                    return 0
                current = current.pointer
            

    def Slice(self, From=None, To=None):
        """
        This function slices the linked list from the node (From) 
        till the node (To) and returns a new linked list that contains 
        the nodes from the (From) node to the (To) node.

        Both (From) and (To) can be either (Node) instances or
        any other type, because the method will turn everything to a 
        (Node) instance if it wasn't. 
        """
        
        if (From is not None) and (To is not None):
            if self.head is None:
                raise Exception("The linked list is empty !")

            if not isinstance(From, Node):
                From = Node(From)
            if not isinstance(To, Node):
                To = Node(To)

            if (not self.Includes(From.value)) or (not self.Includes(To.value)):
                raise Exception("One of the provided values or both isn't existed in the Linked list !")

            sliced = LinkedList()

            current = self.head
            trigger = False
            if current.value == From.value:
                trigger = True
                
            while current.pointer is not None:
                if current.value == From.value:
                    trigger = True
                if trigger:
                    sliced.Append(current.value)   
                if current.value == To.value:
                    break
                current = current.pointer
            else:
                if not sliced.Includes(To.value):
                    sliced.Append(To.value)

            return sliced

        else:
            raise Exception("Both parameters \'From\' and \'To\' must be defined and must not be (None) !")


    def Reverse(self):
        """
        This function reverse the order of the list
        then return a new list.
        """

        reverse = LinkedList()

        if self.head is None:
            return reverse
        
        current = self.head
        while current is not None:
            reverse.Insert(current.value)
            current = current.pointer

        return reverse


#==============================================
#===========    Streach goal    ===============
#==============================================


class DoublyNode:
    """
    This class is used to create a doubly node that 
    will be used in a doubly linked list.

    a (DoublyNode) instance consists of a (value) that holds 
    the node's value, an (n_pointer) that holds the address
    of the next node, and a (p_pointer) that holds the address
    of the previous node.
    """

    def __init__(self, value):
        self.value = value
        self.n_pointer = None
        self.p_pointer = None


    def __str__(self):
        return self.value


class DoublyLinkedList:
    """
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
        
        output = "NULL <- "

        if self.head is None:
            output = "None"
        else:
            current = self.head
            while current:
                output += f"{current.value} <-> "
                current = current.n_pointer
            output = output[:-4] 
            output += "-> NULL"

        return output


    def NodesTable(self):
        current = self.head
        while current is not None:
            print(f"p_pointer: {current.p_pointer}".ljust(25), end=", ")
            print(f"value: {current.value}".ljust(25), end=", ")
            print(f"n_pointer: {current.n_pointer}")
            current = current.n_pointer

    
    def Insert(self, value, after_node=None):
        """
        This function inserts a value at the (beginning) of the 
        linked list if the argument (after_node) wasn't provided.
        Otherwise, it will insert the (value) after the provided node
        value (after_node) 

        Both (value) and (after_node) can be either (Node) instances or
        any other type, because the method will turn everything to a 
        (Node) instance if it wasn't. 
        """
        
        if value is None:
            raise Exception("The provided values must not be (None) !")

        if not isinstance(value, DoublyNode):
            value = DoublyNode(value)

        if self.head is None:
            self.head = value
        
        else:
            if after_node is None:
                value.n_pointer = self.head
                self.head.p_pointer = value
                self.head = value
            
            else:
                if not isinstance(after_node, DoublyNode):
                    after_node = DoublyNode(after_node)
                current = self.head

                while current.n_pointer is not None:
                    if current.value == after_node.value:
                        value.n_pointer, value.p_pointer, current.n_pointer = current.n_pointer, current, value
                        return 0
                    current = current.n_pointer
                else:            
                    if current.value == after_node.value:
                        value.n_pointer, value.p_pointer, current.n_pointer = current.n_pointer, current, value
                        return 0
                
                raise Exception(f"The linked list has no value named \'{after_node}\' !")
                
                
    def Includes(self, value):
        """
        This function checks if the provided value is 
        in the linked list or not and return a Boolean

        The (value) can be either (Node) instances or 
        any other type, because the method will turn 
        everything to a (Node) instance if it wasn't. 
        """

        if value is None:
            raise Exception("The provided value must not be (None) !")
            
        if not isinstance(value, DoublyNode):
            value = DoublyNode(value)

        if self.head is None:
            return False

        else:
            current = self.head
            while current.n_pointer is not None:
                if value.value == current.value:
                    return True
                current = current.n_pointer
            else:
                if value.value == current.value:
                    return True

            return False


    def Append(self, value):
        """
        This function inserts a value (Node instance) at 
        the (end) of the linked list

        The (value) can be either (Node) instances or 
        any other type, because the method will turn 
        everything to a (Node) instance if it wasn't. 
        """

        if value is None:
            raise Exception("The provided value must not be (None) !")

        if not isinstance(value, DoublyNode):
            value = DoublyNode(value)

        if self.head is None:
            self.head = value
        else:
            current = self.head
            while current.n_pointer is not None:
                current = current.n_pointer
            else:
                current.n_pointer, value.p_pointer = value, current


    def Replace(self, value, new):
        """
        This function replaces the (value) from 
        the linked list with the (new) value if 
        it does exist in it.
        Otherwise, it raise an error.

        Both (value) and (new) can be either (Node) instances or
        any other type, because the method will turn everything to a 
        (Node) instance if it wasn't. 
        """

        if (value is None) or (new is None):
            raise Exception("The provided values must not be (None) !")
        
        if not isinstance(value, DoublyNode):
            value = DoublyNode(value)

        if not isinstance(new, DoublyNode):
            new = DoublyNode(new)

        if not self.Includes(value.value):
                raise Exception("The provided value isn't existed in the Linked list !")

        if self.head is None:
            raise Exception("The linked list is empty !")
        elif self.head.value == value.value:
            self.head.value = new.value
        else:
            current = self.head
            while current.n_pointer is not None:
                if current.value == value.value:
                    current.value = new.value
                    return 0
                current = current.n_pointer
            else:
                if current.value == value.value:
                    current.value = new.value
                    return 0


    def Delete(self, value):
        """
        This function deletes a value from 
        the linked list if it does exist in it.
        Otherwise, it raise an error.

        The (value) can be either (Node) instances or 
        any other type, because the method will turn 
        everything to a (Node) instance if it wasn't. 
        """

        if value is None:
            raise Exception("The provided value must not be (None) !")

        if not isinstance(value, DoublyNode):
            value = DoublyNode(value)

        if not self.Includes(value.value):
                raise Exception("The provided value isn't existed in the Linked list !")

        if self.head is None:
            raise Exception("The linked list is empty !")
        elif self.head.value == value.value:
            self.head = self.head.n_pointer
            if self.head is not None:
                self.head.n_pointer.p_pointer = self.head
        else:
            current = self.head
            while current.n_pointer is not None:
                if current.n_pointer.value == value.value:
                    current.n_pointer = current.n_pointer.n_pointer
                    if current.n_pointer is not None:
                        current.n_pointer.p_pointer = current
                    return 0
                current = current.n_pointer
            

    def Slice(self, From=None, To=None):
        """
        This function slices the linked list from the node (From) 
        till the node (To) and returns a new linked list that contains 
        the nodes from the (From) node to the (To) node.

        Both (From) and (To) can be either (Node) instances or
        any other type, because the method will turn everything to a 
        (Node) instance if it wasn't. 
        """
        
        if (From is not None) and (To is not None):
            if self.head is None:
                raise Exception("The linked list is empty !")

            if not isinstance(From, DoublyNode):
                From = DoublyNode(From)
            if not isinstance(To, DoublyNode):
                To = DoublyNode(To)

            if (not self.Includes(From.value)) or (not self.Includes(To.value)):
                raise Exception("One of the provided values or both isn't existed in the Linked list !")

            sliced = DoublyLinkedList()

            current = self.head
            trigger = False
            if current.value == From.value:
                trigger = True
                
            while current.n_pointer is not None:
                if current.value == From.value:
                    trigger = True
                if trigger:
                    sliced.Append(current.value)   
                if current.value == To.value:
                    break
                current = current.n_pointer
            else:
                if not sliced.Includes(To.value):
                    sliced.Append(To.value)

            return sliced

        else:
            raise Exception("Both parameters \'From\' and \'To\' must be defined and must not be (None) !")


    def Reverse(self):
        """
        This function reverse the order of the list
        then return a new list.
        """

        reverse = DoublyLinkedList()

        if self.head is None:
            return reverse
        
        current = self.head
        while current is not None:
            reverse.Insert(current.value)
            current = current.n_pointer

        return reverse



if __name__ == "__main__":
    pass

