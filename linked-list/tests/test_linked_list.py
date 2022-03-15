import pytest
from linked_list.linked_list import Node, LinkedList, DoublyNode, DoublyLinkedList


#============================================
#===========    Required Tests    ===========
#============================================


def test_empty_list_instatiation():
    assert LinkedList().head is None


def test_inserting_into_linked_list(my_linked_list):
    my_linked_list.Insert(Node("Barham"))
    assert str(my_linked_list) == "Barham -> Mustafa -> Zaid -> Ammar -> NULL"


def test_head_pointer_towards_first_node(my_linked_list):
    assert my_linked_list.head.value == Node("Mustafa").value


def test_inserting_multiple_nodes(my_linked_list):
    [my_linked_list.Insert(Node(i)) for i in ["Barham", "Imad", "Husain"]]
    assert str(my_linked_list) == "Husain -> Imad -> Barham -> Mustafa -> Zaid -> Ammar -> NULL"


def test_serching_for_existed_node(my_linked_list):
    assert my_linked_list.Includes("Zaid") == True


def test_serching_for_not_existed_node(my_linked_list):
    assert my_linked_list.Includes("Maher") == False


def test_returning_all_values_in_linked_list(my_linked_list):
    assert str(my_linked_list) == "Mustafa -> Zaid -> Ammar -> NULL"


#==============================================
#===========    Challenge 06 tests   ==========
#==============================================


def test_appending_to_linked_list(my_linked_list):
    my_linked_list.Append(Node("Barham"))
    assert str(my_linked_list) == "Mustafa -> Zaid -> Ammar -> Barham -> NULL"


def test_providing_not_node_instance_for_append_method(my_linked_list):
    my_linked_list.Append("Barham")
    assert str(my_linked_list) == "Mustafa -> Zaid -> Ammar -> Barham -> NULL"


def test_inserting_a_node_before_a_specific_other_node(my_linked_list):
    my_linked_list.InsertBefore("Barham", "Zaid")
    assert str(my_linked_list) == "Mustafa -> Barham -> Zaid -> Ammar -> NULL"


def test_inserting_a_node_before_the_head(my_linked_list):
    my_linked_list.InsertBefore("Barham", "Mustafa")
    assert str(my_linked_list) == "Barham -> Mustafa -> Zaid -> Ammar -> NULL"


def test_inserting_a_node_after_the_last_node(my_linked_list):
    my_linked_list.InsertAfter("Barham", "Ammar")
    assert str(my_linked_list) == "Mustafa -> Zaid -> Ammar -> Barham -> NULL"


def test_inserting_a_node_after_a_specific_other_node(my_linked_list):
    my_linked_list.InsertAfter("Barham", "Zaid")
    assert str(my_linked_list) == "Mustafa -> Zaid -> Barham -> Ammar -> NULL"


def test_deleting_the_head(my_linked_list):
    my_linked_list.Delete("Mustafa")
    assert str(my_linked_list) == "Zaid -> Ammar -> NULL"


def test_deleting_a_middle_node(my_linked_list):
    my_linked_list.Delete("Zaid")
    assert str(my_linked_list) == "Mustafa -> Ammar -> NULL"


def test_deleting_the_last_node(my_linked_list):
    my_linked_list.Delete("Ammar")
    assert str(my_linked_list) == "Mustafa -> Zaid -> NULL"


#==============================================
#===========    Additional Tests    ===========
#==============================================


def test_providing_not_node_instance_for_insert_method(my_linked_list):
    my_linked_list.Insert("Barham")
    assert str(my_linked_list) == "Barham -> Mustafa -> Zaid -> Ammar -> NULL"


def test_providing_a_node_instance_for_includes_method(my_linked_list):
    assert my_linked_list.Includes(Node("Zaid")) == True


def test_replacing_the_head_with_another_node(my_linked_list):
    my_linked_list.Replace("Mustafa", "Barham")
    assert str(my_linked_list) == "Barham -> Zaid -> Ammar -> NULL"


def test_replacing_a_node_in_the_middle_with_another_node(my_linked_list):
    my_linked_list.Replace("Zaid", "Barham")
    assert str(my_linked_list) == "Mustafa -> Barham -> Ammar -> NULL"


def test_replacing_the_last_node_with_another_node(my_linked_list):
    my_linked_list.Replace("Ammar", "Barham")
    assert str(my_linked_list) == "Mustafa -> Zaid -> Barham -> NULL"


def test_slicing_the_linked_list(my_long_linked_list):
    new_list = my_long_linked_list.Slice(From="Zaid", To="Barham")
    assert str(new_list) == "Zaid -> Ammar -> Barham -> NULL"


def test_slicing_the_linked_list_from_the_head(my_long_linked_list):
    new_list = my_long_linked_list.Slice(From="Mustafa", To="Barham")
    assert str(new_list) == "Mustafa -> Zaid -> Ammar -> Barham -> NULL"


def test_slicing_the_linked_list_to_the_end(my_long_linked_list):
    new_list = my_long_linked_list.Slice(From="Barham", To="Husain")
    assert str(new_list) == "Barham -> Imad -> Husain -> NULL"


def test_reversing_the_linked_list(my_linked_list):
    new_list = my_linked_list.Reverse()
    assert str(new_list) == "Ammar -> Zaid -> Mustafa -> NULL"


#==========================================
#===========    Streach goal    ===========
#==========================================


def test_doubly_linked_list_ToString_meyhod(my_doubly_linked_list):
    my_doubly_linked_list.ToString()
    assert str(my_doubly_linked_list) == "NULL <- Mustafa <-> Zaid <-> Ammar -> NULL"


def test_doubly_linked_list_Insert_meyhod(my_doubly_linked_list):
    my_doubly_linked_list.Insert("Barham")
    assert str(my_doubly_linked_list) == "NULL <- Barham <-> Mustafa <-> Zaid <-> Ammar -> NULL"


def test_doubly_linked_list_Append_meyhod(my_doubly_linked_list):
    my_doubly_linked_list.Append("Barham")
    assert str(my_doubly_linked_list) == "NULL <- Mustafa <-> Zaid <-> Ammar <-> Barham -> NULL"


def test_doubly_linked_list_Includes_meyhod(my_doubly_linked_list):
    assert my_doubly_linked_list.Includes("Zaid") == True


def test_doubly_linked_list_Includes_meyhod(my_doubly_linked_list):
    assert my_doubly_linked_list.Includes("Husain") == False
    

def test_doubly_linked_list_Replace_meyhod(my_doubly_linked_list):
    my_doubly_linked_list.Replace("Zaid", "Barham")
    assert str(my_doubly_linked_list) == "NULL <- Mustafa <-> Barham <-> Ammar -> NULL"


def test_doubly_linked_list_Delete_meyhod(my_doubly_linked_list):
    my_doubly_linked_list.Delete("Zaid")
    assert str(my_doubly_linked_list) == "NULL <- Mustafa <-> Ammar -> NULL"


def test_doubly_linked_list_Slice_meyhod(my_long_doubly_linked_list):
    new_list = my_long_doubly_linked_list.Slice(From="Zaid", To="Barham")
    assert str(new_list) == "NULL <- Zaid <-> Ammar <-> Barham -> NULL"


def test_doubly_linked_list_Reverse_meyhod(my_doubly_linked_list):
    new_list = my_doubly_linked_list.Reverse()
    assert str(new_list) == "NULL <- Ammar <-> Zaid <-> Mustafa -> NULL"


#======================================
#===========    Fixtures    ===========
#======================================


@pytest.fixture
def my_linked_list():
    ll = LinkedList()
    [ll.Append(Node(i)) for i in ["Mustafa", "Zaid", "Ammar"]]
    return ll


@pytest.fixture
def my_long_linked_list():    
    ll = LinkedList()
    [ll.Append(Node(i)) for i in ["Mustafa", "Zaid", "Ammar", "Barham", "Imad", "Husain"]]
    return ll


@pytest.fixture
def my_doubly_linked_list():    
    dll = DoublyLinkedList()
    [dll.Append(DoublyNode(i)) for i in ["Mustafa", "Zaid", "Ammar"]]
    return dll


@pytest.fixture
def my_long_doubly_linked_list():    
    dll = DoublyLinkedList()
    [dll.Append(DoublyNode(i)) for i in ["Mustafa", "Zaid", "Ammar", "Barham", "Imad", "Husain"]]
    return dll

