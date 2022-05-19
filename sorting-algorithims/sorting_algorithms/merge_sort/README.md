# Challenge Summary

> [Back](../../README.md)

Write a function that sort the input array in the (Merge Sort) algorithm

## Pull Request:

> [PR](https://github.com/Mustfa1999/data-structures-and-algorithms/pull/18)

## Whiteboard Process

![img](./Problem%20Solving%20Whiteboard%20Template.jpg)

## Approach & Efficiency

define a function (Mergesort) that takes a list as an argument 
if the length of the list is bigger than 1, split the lists into two parts (left, right) from the middle
call the function again recursively for each part of the list
define 3 counters
in a while loop that ends when both counters are less than the length of the left and right lists:
compare the nth element between two lists and assign that element to the original list based on that
if the first counter equals the length of the left list, assign the remaining elements of the right side of the right list to the original list, and vice versia for the else. 

Big-O is o(log(n)) for time because we have a recursive function with a list that has a decreased length, and o(n) for space because we created multiple lists 

## Solution

```
def Mergesort(arr):
    n = len(arr)

    if n > 1:
      mid = n//2  
      left = arr[:mid]  
      right = arr[mid:] 
      
      Mergesort(left)
      Mergesort(right)
      Merge(left, right, arr)
      
      return arr


def Merge(left, right, arr): 
    i, j, k = 0, 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else: 
            arr[k] = right[j]
            j += 1

        k += 1
        
    if i == len(left): 
        for element in right[j:]:
            arr[k] = element
            k += 1
    else:
        for element in left[i:]: 
            arr[k] = element
            k += 1

```

## Tests

```
def test_merge_sort():
    assert [-5, 0, 1, 4, 8] == Mergesort([0, -5, 1, 8, 4])
    assert [-789, 0, 1, 2, 11, 52, 78] == Mergesort([0,1,78,-789,2,11,52])
```