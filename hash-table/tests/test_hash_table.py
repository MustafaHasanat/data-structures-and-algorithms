from hash_table.hash_table import HashTable, repeated_word, word_trimmer
from hash_table.tree_intersection import tree_intersection
import pytest

 
def test_hash_table(hash_table):
    
    assert hash_table.get("name") == [('name', 'python')]
    assert hash_table.get("cloud") == [('cloud', 'AWS'), ('could', 'rainy')]
    assert hash_table.contains("name") == True
    assert hash_table.contains("red") == False
    assert hash_table.keys() == ['name', 'cloud', 'could']
    assert hash_table.hash("cloud") == 949


def test_word_trimmer():
    assert word_trimmer("Hello") == ["hello"]
    assert word_trimmer("Hello, there...") == ["hello", "there"]
    assert word_trimmer("A piece of CODE") == ["a", "piece", "of", "code"]


def test_repeated_word():
    string1 = "Once upon a time, there was a brave princess who..."
    string2 = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    string3 = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    string4 = "there was a brave princess who..."
    assert repeated_word(string1) == "a"
    assert repeated_word(string2) == "it"
    assert repeated_word(string3) == "summer"
    assert repeated_word(string4) == None


def test_tree_intersection():
    from hash_table.hash_table import TNode, BinaryTree
    
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

    assert tree_intersection(tree1, tree2) == [100, 310, 10]
    
    
 
@pytest.fixture
def hash_table():
    ht = HashTable()
    ht.set('cloud', 'AWS')
    ht.set('could', 'rainy')
    ht.set('name', 'python')
    return ht


