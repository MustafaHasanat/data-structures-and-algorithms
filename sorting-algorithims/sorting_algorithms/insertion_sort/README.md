# Challenge Summary

> [Back](../../README.md)

Write a function that sort the input array in the (Insertion Sort) algorithm

## Pull Request:

> [PR](https://github.com/Mustfa1999/data-structures-and-algorithms/pull/17)

## Whiteboard Process

![img](./Problem%20Solving%20Whiteboard%20Template.jpg)

## Approach & Efficiency

define a function (InsertionSort) that takes a list as an argument. if the list's elements are not numeric, raise an error. loop through the list's items and check if it is the greatest one compared with the items before it 
if not, insert it before the greater one. then return the list 

Big-O is o(n2) for time because we have 2 nested loops, and o(n) for space because we created a new list 

## Solution

```
def InsertionSort(my_list):

    for x in my_list:
        if not str(x).isdigit():
            raise(Exception("list has to benumeric"))
    
    for i in range(1, len(my_list)):
        index = i - 1  
        temp = my_list[i]   

        while index >= 0 and temp < my_list[index]:
            my_list[i] = my_list[index]
            index -= 1

        my_list[i] = temp
        
    return my_list 
```

## Tests

```
def test_insertion_sort():
    assert [-9, 0, 1, 2, 4, 87] == InsertionSort([2,87,4,-9,0,1])
    assert [-789, 0, 1, 2, 11, 52, 78] == InsertionSort([0,1,78,-789,2,11,52])
    assert [1, 2, 3] == InsertionSort([3,2,1])
```