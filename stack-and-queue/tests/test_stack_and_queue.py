import pytest
from stack_and_queue.stack_and_queue import Node, Stack, Queue


# ==============================================
# ====== tests the node and stack classes ======
# ==============================================

def test_node_creation():
    assert Node("Mustafa").value == "Mustafa"

def test_empty_stack():
    assert Stack().top == None

def test_push(my_stack):
    my_stack.push("Imad")
    assert my_stack.top.value == "Imad"
    
def test_pop(my_stack):
    assert my_stack.pop() == "Ammar"
    assert my_stack.top.value == "Zaid"
    
def test_is_empty_stack(my_stack):
    assert Stack().is_empty() == True
    assert my_stack.is_empty() == False

def test_peek_stack(my_stack):
    assert my_stack.peek() == "Ammar"
    
def test_multiple_pushes():
    s = Stack()
    [s.push(i) for i in ["Mustafa", "Barham", "Zaid", "Ammar"]]
    assert s.top.value == "Ammar"

def test_multiple_pops_untill_empty(my_stack):
    [my_stack.pop() for _ in range(4)]
    assert my_stack.is_empty() == True

def test_pop_on_empty_stack():
    with pytest.raises(Exception):
        Stack().pop()

def test_peek_on_empty_stack():
    with pytest.raises(Exception):
        Stack().peek()

def test_size_stack(my_stack):
    assert my_stack.size() == 4

def test_reverse_stack(my_stack):
    assert my_stack.reverse().peek() == "Mustafa"

# =====================================
# ====== tests the queue classe =======
# =====================================

def test_empty_queue():
    assert Queue().front == None
    assert Queue().back == None

def test_enqueue(my_queue):
    my_queue.enqueue("Imad")
    assert my_queue.front.value == "Mustafa"
    assert my_queue.back.value == "Imad"

def test_multiple_enqueue():
    q = Queue()
    [q.enqueue(i) for i in ["Mustafa", "Barham", "Zaid", "Ammar"]]
    assert q.front.value == "Mustafa"
    assert q.back.value == "Ammar"

def test_dequeue(my_queue):
    assert my_queue.dequeue() == "Mustafa"
    assert my_queue.front.value == "Barham"
    assert my_queue.back.value == "Ammar"

def test_multiple_dequeues_untill_empty(my_queue):
    [my_queue.dequeue() for _ in range(4)]
    assert my_queue.is_empty() == True

def test_is_empty_queue(my_queue):
    assert Queue().is_empty() == True
    assert my_queue.is_empty() == False

def test_peek_queue(my_queue):
    assert my_queue.peek() == "Mustafa"
  
def test_dequeue_on_empty_queue():
    with pytest.raises(Exception):
        Queue().dequeue()

def test_peek_on_empty_queue():
    with pytest.raises(Exception):
        Queue().peek()

  
# =======================
# ====== fixtures =======
# =======================

@pytest.fixture
def my_stack():
    s = Stack()
    [s.push(i) for i in ["Mustafa", "Barham", "Zaid", "Ammar"]]
    return s

@pytest.fixture
def my_queue():
    q = Queue()
    [q.enqueue(i) for i in ["Mustafa", "Barham", "Zaid", "Ammar"]]
    return q


