# Quick Sort Blog

## Quick Sort

We sort the array by dividing it into smaller sub arrays repeatedly until we end up with sorted consecutive single elements

## Steps of sorting 

- Input: [8,4,23,42,16,15]

- divide according to (15):
    
        less than 15: 8,4
        the pivot: 15
        more than 15: 23,42,16

- divide (8,4) according to (4):
    
        the pivot: 4
        more than 4: 8

- divide (23,42,16) according to (16):
    
        the pivot: 16
        more than 16: 23, 42

- divide (23,42) according to (42):
    
        less than 42: 23
        the pivot: 42

- all together:
    
        4
        8
        15 
        16
        23
        42


## Efficency


Big-O:

QuickSort: o(log(n)) for time because we have a recursive function with a list that has a decreased length, and o(1) for space  

Partition: o(n) for both time and space

Swap: o(1) for both time and space
