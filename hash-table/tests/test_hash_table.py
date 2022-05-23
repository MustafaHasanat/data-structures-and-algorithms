from hash_table.hash_table import HashTable
import pytest


def test_hash_table(hash_table):
    
    assert hash_table.get("name") == [('name', 'python')]
    assert hash_table.get("cloud") == [('cloud', 'AWS'), ('could', 'rainy')]
    assert hash_table.contains("name") == True
    assert hash_table.contains("red") == False
    assert hash_table.keys() == ['name', 'cloud', 'could']
    assert hash_table.hash("cloud") == 949


@pytest.fixture
def hash_table():
    ht = HashTable()
    ht.set('cloud', 'AWS')
    ht.set('could', 'rainy')
    ht.set('name', 'python')
    return ht


