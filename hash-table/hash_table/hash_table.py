class HashTable(object):
    """
    It is a class that create a hash table and its required methods
    """
    
    def __init__(self, size=1024):
        self.size = size
        self.map = [None] * size
        self.prime = 19
        
        
    def __getitem__(self, key):
        idx = self.get_hash(key)
        return self.map[idx][0][1]


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
            
            
         


if __name__ == '__main__':
    hash_table = HashTable()
    hash_table.set('cloud', 'AWS')
    hash_table.set('could', 'rainy')
    hash_table.set('name', 'python')
    
    for item in enumerate(hash_table.map):
        if item[1] is not None:
            print(item) 
            
    print(hash_table.get("name"))
    print(hash_table.get("cloud"))
    print(hash_table.contains("name"))
    print(hash_table.contains("red"))
    print(hash_table.keys())
    print(hash_table.hash("cloud"))



