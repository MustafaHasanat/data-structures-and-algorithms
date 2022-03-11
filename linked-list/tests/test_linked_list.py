import pytest
from linked_list.linked_list import LinkedList, Node


#===========================================
#===========    Reqired Tests    ===========
#===========================================


def test_empty_list_instatiation():
    assert LinkedList().head is None


def test_inserting_into_linked_list(my_inked_list):
    my_inked_list.Insert(Node("Barham"))
    assert str(my_inked_list) == "Barham -> Mustafa -> Zaid -> Ammar -> NULL"


def test_head_pointer_towards_first_node(my_inked_list):
    assert my_inked_list.head.value == Node("Mustafa").value


def test_inserting_multiple_nodes(my_inked_list):
    [my_inked_list.Insert(Node(i)) for i in ["Barham", "Imad", "Husain"]]
    assert str(my_inked_list) == "Husain -> Imad -> Barham -> Mustafa -> Zaid -> Ammar -> NULL"


def test_serching_for_existed_node(my_inked_list):
    assert my_inked_list.Includes("Zaid") == True


def test_serching_for_not_existed_node(my_inked_list):
    assert my_inked_list.Includes("Maher") == False


def test_returning_all_values_in_linked_list(my_inked_list):
    assert str(my_inked_list) == "Mustafa -> Zaid -> Ammar -> NULL"


#==============================================
#===========    Additional Tests    ===========
#==============================================


def test_appending_to_linked_list(my_inked_list):
    my_inked_list.Append(Node("Barham"))
    assert str(my_inked_list) == "Mustafa -> Zaid -> Ammar -> Barham -> NULL"



#======================================
#===========    Fixtures    ===========
#======================================

@pytest.fixture
def my_inked_list():    
    ll = LinkedList()
    [ll.Append(Node(i)) for i in ["Mustafa", "Zaid", "Ammar"]]
    return ll


