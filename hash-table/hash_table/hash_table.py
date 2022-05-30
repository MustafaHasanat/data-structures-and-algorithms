class HashTable(object):
    """
    It is a class that create a hash table and its required methods
    """
    
    def __init__(self, size=1024):
        self.size = size
        self.map = [None] * size
        self.prime = 19
        

    def set(self, key, value):
        """
        Arguments: key, value
        Returns: nothing
        This method should hash the key, and set the key and value 
        pair in the table, handling collisions as needed.
        Should a given key already exist, replace its value from 
        the value argument given to this method.
        """
        
        sum_of_ascii = 0
        for char in key:
            sum_of_ascii += ord(char)
            
        index = (sum_of_ascii*self.prime) % self.size
        
        if not self.map[index]:
            self.map[index] = [(key, value)]
        else:
            self.map[index].append((key, value))
        
        
    def get(self, key):
        """
        Arguments: key
        Returns: Value associated with that key in the table
        """
        return self.map[self.hash(key)]
        
        
    def contains(self, key):
        """
        Arguments: key
        Returns: Boolean, indicating if the key exists in the table already.
        """ 
        return True if self.map[self.hash(key)] else False
        
        
    def keys(self):
        """
        Returns: Collection of keys
        """
        res = []
        for item in self.map:
            if item: [res.append(pair[0]) for pair in item]
                
        return res
            
        
        
    def hash(self, key):
        """
        Arguments: key
        Returns: Index in the collection for that key
        """
        sum_of_ascii = 0
        for char in key:
            sum_of_ascii += ord(char)
            
        return (sum_of_ascii*self.prime) % self.size
       
       
class TNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        """
        Input: None
        doing: traverse a tree (pre-order --> root-left-right)
        output: print values of the nodes of the tree
        """
        
        output = []
        def _walk(node):
            nonlocal output 
            output.append(node.value)

            if node.left:
                _walk(node.left)

            if node.right:
                _walk(node.right)

        _walk(self.root)
                
        return output
     
            

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




if __name__ == '__main__':
    pass
    
