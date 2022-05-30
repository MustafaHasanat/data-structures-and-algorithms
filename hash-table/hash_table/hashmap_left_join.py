from hash_table.hash_table import HashTable


def hashmap_left_join(hashmap1, hashmap2):
    """
    Arguments: two hash maps
    Return: left-joind two hash maps
    """
    
    if not isinstance(hashmap1, HashTable) or not isinstance(hashmap2, HashTable):
        raise Exception("inputs must be hashmaps !")
    
    res = []
    
    for item in hashmap1.map:
        if item:
            if hashmap2.get(item[0][0]):
                res.append([item[0][0], item[0][1], hashmap2.get(item[0][0])[0][1]])
            else:
                res.append([item[0][0], item[0][1], None])
                
    return res
    
    
if __name__ == '__main__':
    pass
    
    
    