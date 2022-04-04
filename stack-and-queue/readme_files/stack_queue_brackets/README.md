# Stack Queue Brackets

> [Back to main](../../README.md)

---

# Challenge Summary

Write a function called validate brackets
Arguments: string
Return: boolean
representing whether or not the brackets in the string are balanced
There are 3 types of brackets:
- Round Brackets : ()
- Square Brackets : []
- Curly Brackets : {}

## Pull Request

> [PR](https://github.com/Mustfa1999/data-structures-and-algorithms/pull/12)

## Whiteboard Process

![img](./Problem%20Solving%20Whiteboard%20Template.jpg)

## Approach & Efficiency

define an algorithm validate_brackets(string)
if the input is not a string raise an exception 
define a dictionary that holds the opening brackets as keys, and the closing ones as their values
define a Stack
loop through the string's characters and push every opening bracket to the stack, and if you face a closing one, check if it is on the top of the stack and pop it
if it was not on the top or the stack is empty, return false
only return true if the loop is over and the stack is empty

## Solution

```
@staticmethod
def validate_brackets(string):
    if not type(string) == str: 
        raise Exception("Invalid input !")
    
    pairs = {"(": ")", "[": "]", "{": "}"}
    stack = Stack()
    
    for i in string:
        if i in pairs.keys():
            stack.push(i)
        
        elif i in pairs.values():
            if stack.is_empty():
                return False
            elif i == pairs.get(stack.peek()):
                stack.pop()
            else:
                return False
    
    return True if stack.is_empty() else False
```

## tests

```
def test_validate_brackets():
    assert Stack.validate_brackets("{}") == True
    assert Stack.validate_brackets("{}(){}") == True
    assert Stack.validate_brackets("()[[Extra Characters]]") == True
    assert Stack.validate_brackets("(){}[[]]") == True
    assert Stack.validate_brackets("{}{Code}[Fellows](())") == True
    assert Stack.validate_brackets("[({}]") == False
    assert Stack.validate_brackets("(](") == False
    assert Stack.validate_brackets("{(})") == False	
    assert Stack.validate_brackets("(") == False	
    assert Stack.validate_brackets("}") == False	
    assert Stack.validate_brackets("{(}") == False	
```

