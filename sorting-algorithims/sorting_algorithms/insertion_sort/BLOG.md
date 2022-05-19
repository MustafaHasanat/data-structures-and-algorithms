# Insertion Sort Blog

## Insertion Sort

Insertion Sort is a sorting algorithm that traverses the array multiple times as it slowly builds out the sorting sequence. The traversal keeps track of the minimum value and places it in the front of the array which should be incrementally sorted.

## Steps of sorting 

- Trace the Array: 
 
        [8,4,23,42,16,15]

- Step 1: insert 4 in the first because it is the least out of them

        [4,8,23,42,16,15]

- Step 2: don't insert because it is the biggest out of them

        [4,8,23,42,16,15]

- Step 3: don't insert

        [4,8,23,42,16,15]

- Step 4: insert 16 before the 23

        [4,8,16,23,42,15]

- Step 5: insert 15 before the 16

        [4,8,15,16,23,42]


## Efficency

- Time: O(n^2)

The basic operation of this algorithm is comparison. This will happen n * (n-1) number of times…concluding the algorithm to be n squared.

- Space: O(1)

No additional space is being created. This array is being sorted in place…keeping the space at constant O(1).