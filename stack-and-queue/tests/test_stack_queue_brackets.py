from stack_and_queue.stack_and_queue import Stack


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


