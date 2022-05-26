# Merge Sort Blog

## Merge Sort

It is a technique to sort an array where we divide it from the middle continuously until we end up with pairs or single elements

## Steps of sorting 

- Input: [2,8,5,25,11]

- divide from the middle for (2,8,5,25,11):
    
        left: 2,8
        right: 5,25,11

- divide from the middle for (2,8):
    
        left: 2
        right: 8
        sorted ==> 2, 8

- divide from the middle for (5,25,11):
    
        left: 5,
        right: 25,11

- divide from the middle for (25,11):
    
        left: 25
        right: 11
        sorted ==> 11, 25
        
- merge all together:

        2
        5
        8
        11
        25

## Efficency

Big-O is o(log(n)) for time because we have a recursive function with a list that has a decreased length, and o(n) for space because we created multiple lists 

