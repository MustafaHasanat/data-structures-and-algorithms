# Challenge Summary

> [Back](../../README.md)

Write a function to implement the quick sort technique

## Whiteboard Process

![img](./Problem%20Solving%20Whiteboard%20Template.jpg)

## Approach & Efficiency

define the pivot of the array as the last element
divide the array according to the pivot into two where the first has elements bigger than pivotm, and the second has elements smaller than pivot
for each part, create an array tp hold its elements 
do the process again for each part (left and right)

Big-O:

QuickSort: o(log(n)) for time because we have a recursive function with a list that has a decreased length, and o(1) for space  

Partition: o(n) for both time and space

Swap: o(1) for both time and space

---

## Solution

```
def QuickSort(arr, left, right):
    if left < right:
        position = Partition(arr, left, right)
        QuickSort(arr, left, position - 1)
        QuickSort(arr, position + 1, right)

    return arr


def Partition(arr, left, right):
    pivot = arr[right]
    low = left - 1
    for i in range(left, right):
        if arr[i] <= pivot:
            low += 1
            Swap(arr, i, low)

    Swap(arr, right, low + 1)
    return low + 1

def Swap(arr, i, low):
    temp =  arr[i]
    arr[i] = arr[low]
    arr[low] = temp
```

## Tests

```
def test_quick_sort():
    assert [-9, 0, 1, 2, 4, 87] == QuickSort([2,87,4,-9,0,1], 0, 5)
    assert [-789, 0, 1, 2, 11, 52, 78] == QuickSort([0,1,78,-789,2,11,52], 0, 6)
    assert [1, 2, 3] == QuickSort([3,2,1], 0, 2)
```
