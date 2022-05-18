# Challenge Summary

> [Back](../README.md)


## Pull Request:

> [PR]()

## Whiteboard Process

![img]()

## Approach & Efficiency

Big-O is o(n2) for time because we have 2 nested loops, and o(n) for space because we created a new list 

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