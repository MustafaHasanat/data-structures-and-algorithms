from hash_table.hash_table import HashTable, repeated_word, word_trimmer
import pytest


def test_hash_table(hash_table):
    
    assert hash_table.get("name") == [('name', 'python')]
    assert hash_table.get("cloud") == [('cloud', 'AWS'), ('could', 'rainy')]
    assert hash_table.contains("name") == True
    assert hash_table.contains("red") == False
    assert hash_table.keys() == ['name', 'cloud', 'could']
    assert hash_table.hash("cloud") == 949


def test_word_trimmer():
    assert word_trimmer("Hello") == ["hello"]
    assert word_trimmer("Hello, there...") == ["hello", "there"]
    assert word_trimmer("A piece of CODE") == ["a", "piece", "of", "code"]


def test_repeated_word():
    string1 = "Once upon a time, there was a brave princess who..."
    string2 = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    string3 = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    string4 = "there was a brave princess who..."
    assert repeated_word(string1) == "a"
    assert repeated_word(string2) == "it"
    assert repeated_word(string3) == "summer"
    assert repeated_word(string4) == None
 
 
@pytest.fixture
def hash_table():
    ht = HashTable()
    ht.set('cloud', 'AWS')
    ht.set('could', 'rainy')
    ht.set('name', 'python')
    return ht


