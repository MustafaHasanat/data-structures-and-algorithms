from trees.trees import fizz_buzz_tree, BinaryTreeSearch, TNode
import pytest


def test_fizz_buzz_tree():
    tree = BinaryTreeSearch()
    tree.root = TNode(23) 
    [tree.add(i) for i in [8,4,16,15,22,42,27,85,105]]
    assert fizz_buzz_tree(tree).pre_order() == ['23', '8', '4', '16', 'FizzBuzz', '22', 'Fizz', 'Fizz', 'Buzz', 'FizzBuzz'] 


def test_fizz_buzz_tree_empty():
    with pytest.raises(Exception):
        fizz_buzz_tree(BinaryTreeSearch())


# @pytest.fixture



