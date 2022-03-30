from stack_and_queue.stack_queue_animal_shelter import AnimalShelter, Cat, Dog, Bird
import pytest


def test_enqueue():
    shelter1 = AnimalShelter()
    shelter1.enqueue(Cat())
    assert shelter1.peek() == "cat"

def test_enqueue_error(shelter1):
    with pytest.raises(Exception): 
        shelter1.enqueue(Bird())

def test_dequeue(shelter1):
    assert str(shelter1.dequeue()) == "dog"

def test_dequeue_2(shelter1):
    assert str(shelter1.dequeue("dog")) == "dog"
    assert str(shelter1.dequeue()) == "cat"

def test_dequeue_error(shelter1):
    with pytest.raises(Exception): 
        shelter1.dequeue("cat")

def test_dequeue_error_2():
    with pytest.raises(Exception): 
        AnimalShelter().dequeue()
        



@pytest.fixture
def shelter1():
    s = AnimalShelter()
    [s.enqueue(i) for i in [Dog(), Cat(), Cat(), Dog(), Cat(), Dog()]]
    return s

