from trees.trees import TNode, BinaryTree, BinaryTreeSearch
import pytest


def test_pre_order(myTree):
    assert myTree.pre_order() == ['A', 'B', 'D', 'E', 'C', 'F']
    
def test_in_order(myTree):
    assert myTree.in_order() == ['D', 'B', 'E', 'A', 'F', 'C']
    
def test_post_order(myTree):
    assert myTree.post_order() == ['D', 'E', 'B', 'F', 'C', 'A']

def test_add_binary_tree_search(myTreeSearch):
    assert myTreeSearch.pre_order() == [23, 8, 4, 16, 15, 22, 42, 27, 85, 105]
    assert myTreeSearch.in_order() == [4, 8, 15, 16, 22, 23, 27, 42, 85, 105]
    assert myTreeSearch.post_order() == [4, 15, 22, 16, 8, 27, 105, 85, 42, 23]

def test_contains_binary_tree_search(myTreeSearch):
    assert myTreeSearch.contains(23) == True
    assert myTreeSearch.contains(42) == True
    assert myTreeSearch.contains(105) == True
    assert myTreeSearch.contains(0) == False
    assert myTreeSearch.contains(100) == False


@pytest.fixture
def myTree():
    nodeA = TNode("A")
    nodeB = TNode("B")
    nodeC = TNode("C")
    nodeD = TNode("D")
    nodeE = TNode("E")
    nodeF = TNode("F")
    
    nodeA.left = nodeB
    nodeA.right = nodeC
    nodeB.left = nodeD
    nodeB.right = nodeE
    nodeC.left = nodeF
        
    tree = BinaryTree()
    tree.root = nodeA
    
    return tree


@pytest.fixture
def myTreeSearch():
    tree = BinaryTreeSearch()
    tree.root = TNode(23)
    [tree.add(i) for i in [8,4,16,15,22,42,27,85,105]]
    return tree


