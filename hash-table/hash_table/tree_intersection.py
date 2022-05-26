from hash_table.hash_table import HashTable
 
 
def tree_intersection(tree1, tree2):
    """ returns a list of the values in both trees
    
    Args:
        tree1 (BinaryTree)
        tree2 (BinaryTree)

    Returns:
        common (list)
    """
    
    if not isinstance(tree1, BinaryTree) or not isinstance(tree2, BinaryTree):
        raise TypeError("tree1 and tree2 must be BinaryTree")
    
    hash_table = HashTable()
    for node in tree1.pre_order():
        hash_table.set(str(node), node)
        
    common = [node for node in tree2.pre_order() if hash_table.get(str(node))]

    return common



if __name__ == '__main__':
    from hash_table import BinaryTree, TNode
        
    nodeA = TNode(100)
    nodeB = TNode(70)
    nodeC = TNode(30)
    nodeD = TNode(250)
    nodeE = TNode(310)
    nodeF = TNode(10)
    
    nodeA.left = nodeB
    nodeA.right = nodeC
    nodeB.left = nodeD
    nodeB.right = nodeE
    nodeC.left = nodeF
    
    tree1 = BinaryTree() 
    tree1.root = nodeA

    nodeA2 = TNode(100)
    nodeB2 = TNode(45)
    nodeC2 = TNode(36)
    nodeD2 = TNode(20)
    nodeE2 = TNode(310)
    nodeF2 = TNode(10)
    
    nodeA2.left = nodeB2
    nodeA2.right = nodeC2
    nodeB2.left = nodeD2
    nodeB2.right = nodeE2
    nodeC2.left = nodeF2
    
    tree2 = BinaryTree() 
    tree2.root = nodeA2
        
    print(tree_intersection(tree1, tree2))
    
    