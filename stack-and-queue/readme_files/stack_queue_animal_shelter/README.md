# Stack Queue Animal Shelter

> [Back to main](../../README.md)

---

# Challenge Summary

Create a class that makes a virtual shelter that takes cats and dogs objects and enqueue or dequeue them as demand

## Pull Request

> [PR](https://github.com/Mustfa1999/data-structures-and-algorithms/pull/11)

## Whiteboard Process

![img](./Problem%20Solving%20Whiteboard%20Template.jpg)

## Approach & Efficiency

create a function (enqueue) inside the class (AnimalShelter)
it takes one argument (animal)
check if the input is an instance of Cat or Dog classes, if not raise an error
enqueue the input to the queue

create a function (dequeue) inside the class (AnimalShelter)
it takes one argument: the preferred animal 
check if the input is at the front of the queue and dequeue it and return it, if not raise an error
if the preferred is not a cat or a dog, or didn't specified, return the first on the queue
if the queue is empty, raise an error 

## Solution

```
class AnimalShelter:
    def __init__(self):
        self.shelter = Queue()

    
    def __str__(self):
        return f"{self.shelter}"


    def enqueue(self, animal):
        if (not isinstance(animal, Cat)) and (not isinstance(animal, Dog)):
            raise Exception("The animal must be either a Cat or a Dog objects !")

        self.shelter.enqueue(animal)


    def dequeue(self, pref="bird"):

        if (pref != "dog") and (pref != "cat"):
            if self.shelter.is_empty():
                raise Exception("The shelter is empty !")
            
            return self.shelter.dequeue()

        elif self.shelter.is_empty():
            raise Exception("The shelter is empty !")

        elif (pref == "dog") and (self.shelter.peek() == "dog"):
            return self.shelter.dequeue()
        
        elif (pref == "cat") and (self.shelter.peek() == "cat"):
            return self.shelter.dequeue()
        
        else:
            raise Exception(f"The animal in the queue is not {pref} !")

    def peek(self):
        return self.shelter.peek()
```

## tests

```
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
```

