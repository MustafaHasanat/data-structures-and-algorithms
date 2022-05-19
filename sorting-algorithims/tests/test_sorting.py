from insertion_sort.insertion_sort import InsertionSort
import pytest

def test_insertion_sort():
    assert [-9, 0, 1, 2, 4, 87] == InsertionSort([2,87,4,-9,0,1])
    assert [-789, 0, 1, 2, 11, 52, 78] == InsertionSort([0,1,78,-789,2,11,52])
    assert [1, 2, 3] == InsertionSort([3,2,1])
    
    
    
    
    