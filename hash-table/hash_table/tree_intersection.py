from hash_table.hash_table import HashTable
from hash_table.hash_table import BinaryTree
 
 
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
    pass



