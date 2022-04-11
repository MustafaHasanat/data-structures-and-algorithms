class TNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        """
        Input: None
        doing: traverse a tree (pre-order --> root-left-right)
        output: print values of the nodes of the tree
        """
        
        output = []
        def _walk(node):
            nonlocal output 
            output.append(node.value)

            if node.left:
                _walk(node.left)

            if node.right:
                _walk(node.right)

        _walk(self.root)
                
        return output
        
        
    def in_order(self):
        """
        Input: None
        doing: traverse a tree (in-order --> left-root-right)
        output: print values of the nodes of the tree
        """
        
        output = []
        def _walk(node):
            nonlocal output 

            if node.left:
                _walk(node.left)

            output.append(node.value)

            if node.right:
                _walk(node.right)
            
        _walk(self.root) 
        
        return list(output)
        
    
    def post_order(self):
        """
        Input: None
        doing: traverse a tree (post-order --> left-right-root)
        output: print values of the nodes of the tree
        """
        
        output = []
        def _walk(node):
            nonlocal output 

            if node.left:
                _walk(node.left)

            if node.right:
                _walk(node.right)
                
            output.append(node.value)
            
        _walk(self.root)
        
        return list(output)

        
        
class BinaryTreeSearch(BinaryTree):
    """
    a binary tree where each left node is less than its root, and each 
    right node is greater than its root 
    """
    
    def add(self, value):
        """
        input: value
        doing: add the value correctly to the tree
        output: None
        """
         
        current = self.root
        
        while True:
            if current.left and value < current.value:
                current = current.left
            elif current.right and value > current.value:
                current = current.right                
            else:
                if value < current.value:
                    current.left = TNode(value)
                else:
                    current.right = TNode(value)
                break         
                
        
    def contains(self, value):
        """        
        input: value
        doing: check if the value is in the tree at least once
        output: boolean 
        """
        
        current = self.root
        
        while True:
            if current.value == value:
                return True
            
            if current.left and value < current.value:
                current = current.left
            elif current.right and value > current.value:
                current = current.right                
            else:
                break
        
        return False
    
    
    def find_max(self):
        """
        input: none
        doing: return the maximum value from the binary tree
        output: number 
        """
        
        if not self.root:
            raise(Exception("Tree is empty !"))
        
        if not self.root.left and not self.root.right:
            return self.root.value

        maximum = self.root.value
        current = self.root
                
        while True:
            if current.right:
                current = current.right                
                maximum = current.value
            else:
                return maximum
    
    


if __name__ == "__main__": 
    pass
    # tree = BinaryTreeSearch()
    # tree.root = TNode(23) 
    # [tree.add(i) for i in [8,4,16,15,22,42,27,85,105]]
    # print(tree.pre_order())
    # print(tree.in_order())
    # print(tree.post_order())

    # nodeA = TNode("A")
    # nodeB = TNode("B")
    # nodeC = TNode("C")
    # nodeD = TNode("D")
    # nodeE = TNode("E")
    # nodeF = TNode("F")
    
    # nodeA.left = nodeB
    # nodeA.right = nodeC
    # nodeB.left = nodeD
    # nodeB.right = nodeE
    # nodeC.left = nodeF
        
    # tree = BinaryTree() 
    # tree.root = nodeA
    
    # print(tree.pre_order())
    # print(tree.in_order())
    # print(tree.post_order())
    
    
    
    