

class HashTable(object):
    """
    It is a class that create a hash table and has 
    the following methods:
    - get_hash
    - add
    - contains
    - find
    """
    
    def __init__(self, size=1024):
        self.size = size
        self.map = [None] * size
        self.prime = 19

    
    def get_hash(self, key):
        """        
        """
        sum_of_ascii = 0
        for char in key:
            sum_of_ascii += ord(char)
            
        hashed_key = (sum_of_ascii*self.prime) % self.size
        return hashed_key
        

    def add(self, key, value):
        """
        """
        index = self.get_hash(key)
        if not self.map[index]:
            self.map[index] = [(key, value)]
        else:
            self.map[index].append((key, value))
        


    def contains(self):
        pass
    
    
    def find(self, key):
        return self.map[self.get_hash(key)]




if __name__ == '__main__':
    hash_table = HashTable()
    hash_table.add('cloud', 'AWS')
    hash_table.add('could', 'rainy')
    hash_table.add('name', 'python')
    
    for item in enumerate(hash_table.map):
        if item:
            print(item) 

