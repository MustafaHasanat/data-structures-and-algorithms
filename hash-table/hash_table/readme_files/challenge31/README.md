# Challenge 31

> [Back](../../../README.md)

## Challenge Summary

Write a function called repeated word that finds the first word to occur more than once in a string
Arguments: string
Return: the first repeated word

## Whiteboard Process

![img](./Problem%20Solving%20Whiteboard%20Template.jpg)

## Approach & Efficiency

I created a function called (word_trimmer) that is used to delete all non alphanumeric characters from the string and return a list of all the words that are separated with whitespaces.

I used that function to git rid of the non alphanumeric characters from the input of the (repeated_word) main function. Then I kept inserting the words in a hash table untill I get a match for one of them, which means that this is the first repeated word. If the loop couldn't find any match, it will return None. 

Big-O for (repeated_word):

time: o(n), because we used a for-loop twice overall
for space: o(1), because the size of the hash table is the same no matter what is the size of the input text (until we have more than 1024 unique words)

Big-O for (word_trimmer):

for time: o(n), because we used a for-loop twice overall
for space: o(n), because the size of the list will vary according to the input string

## Solution

```
def word_trimmer(string):
    """
    Input: a string
    Doing: delete any non alphanumeric characters in each word 
    Output: trimmed list of words
    """

    list_words = "".join([char for char in string if ord(char) in [32, *list(range(65,91)), *list(range(97, 123)), *list(range(48,58))]])
    
    return list_words.lower().split()
    

def repeated_word(string):
    """
    Input: the input text
    Doing: finds the first word to occur more than once in a string
    Output: the first repeated word
    """
    
    trimmed_words = word_trimmer(string) 
    
    hash_table = HashTable()
    
    for word in trimmed_words:
        if hash_table.get(word):
            return word
        hash_table.set(word, len(word))
        
    return None
```
