from stack_and_queue.stack_queue_pseudo import PseudoQueue
import pytest

def test_enqueue():
    pseudoQ = PseudoQueue()
    [pseudoQ.enqueue(i) for i in ["Mustafa", "Zaid", "Barham"]]
    assert pseudoQ.front() == "Mustafa"

def test_dequeue(my_pseudo_queue):
    assert my_pseudo_queue.dequeue() == "Barham"

def test_dequeue_empty():
    with pytest.raises(Exception):
        PseudoQueue().dequeue()





# =============================================
# =============================================
# =============================================

@pytest.fixture
def my_pseudo_queue():
    q = PseudoQueue()
    [q.enqueue(i) for i in ["Mustafa", "Zaid", "Barham"]]
    return q
