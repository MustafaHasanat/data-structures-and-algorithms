from stack_and_queue.stack_and_queue import Queue


class Cat:
    def __str__(self):
        return "cat"    
class Dog:
    def __str__(self):
        return "dog"
class Bird:
    def __str__(self):
        return "bird"

class AnimalShelter:
    """
    Create a virtual shelter that takes cats and dogs objects and 
    enqueue or dequeue them as demand
    """
    
    def __init__(self):
        self.shelter = Queue()

    
    def __str__(self):
        return f"{self.shelter}"


    def enqueue(self, animal):
        """
        push an animal into the queue
        """
        if (not isinstance(animal, Cat)) and (not isinstance(animal, Dog)):
            raise Exception("The animal must be either a Cat or a Dog objects !")

        self.shelter.enqueue(animal)


    def dequeue(self, pref="bird"):
        """
        pop out the first animal in the queue as demand
        """
        if (pref != "dog") and (pref != "cat"):
            if self.shelter.is_empty():
                raise Exception("The shelter is empty !")
            return self.shelter.dequeue()
        elif self.shelter.is_empty():
            raise Exception("The shelter is empty !")
        elif ((pref == "dog") and (self.shelter.peek() == "dog")) or ((pref == "cat") and (self.shelter.peek() == "cat")):
            return self.shelter.dequeue()
        else:
            raise Exception(f"The animal in the queue is not {pref} !")

    def peek(self):
        return self.shelter.peek()
           

if __name__ == "__main__":
    # from stack_and_queue import Queue
    shelter = AnimalShelter()

    shelter.enqueue(Cat())
    print(shelter.peek())

    # [shelter.enqueue(i) for i in [Dog(), Cat(), Cat(), Dog(), Cat(), Dog()]]

    # print(shelter)
    # print(shelter.dequeue())
    # print(shelter.dequeue("cat"))

    # print(shelter.dequeue("cat"))

    # print(shelter)





