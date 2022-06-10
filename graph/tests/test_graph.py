import pytest
from graph.graph import Node, Edge, Graph


def test_add_node_and_add_edge_methods(graph):
    correct_edges = [("A", "B"), ("A", "C"),("B", "C"),("B", "E"),("B", "D"),("C", "E"),("D", "E"),("D", "F"),("E", "F")]    
    
    counter = 0
    for i in graph.adjacency_list.items():
        for j in i[1]:
            assert (i[0].value, j.node.value) == correct_edges[counter]
            counter += 1
            

def test_get_node(graph):
    assert graph.get_node() == ['A', 'B', 'C', 'D', 'E', 'F']


def test_size_method(graph):
    assert graph.size() == 6


def test_all_neighbors_method_with_weights():
    correct_neighbors = [('A', ['B', 'C']), ('B', ['C', 'E', 'D']), ('C', ['E']), ('D', ['E', 'F']), ('E', ['F'])]
    
    graph = Graph()
    
    a=graph.add_node('A')
    b=graph.add_node('B')
    c=graph.add_node('C')
    d=graph.add_node('D')
    e=graph.add_node('E')
    f=graph.add_node('F')
    
    all_nodes = [a, b, c, d, e, f]
    
    graph.add_edge(a, b)
    graph.add_edge(a, c)

    graph.add_edge(b, c)
    graph.add_edge(b, e)
    graph.add_edge(b, d)
    
    graph.add_edge(c, e)
    
    graph.add_edge(d, e)
    graph.add_edge(d, f)
    
    graph.add_edge(e, f)

    for i in range(5):
        n = graph.get_neighbors(all_nodes[i])
        for j in range(len(n)):
            assert n[j][0] == correct_neighbors[i][1][j]
            assert n[j][1] == 0


def test_graph_with_one_node():
    graph = Graph()
    a=graph.add_node('A')
    graph.add_edge(a, b)
    
    
def test_empty_graph():
    graph = Graph()

    
    
@pytest.fixture
def graph():
    graph = Graph()
    
    a=graph.add_node('A')
    b=graph.add_node('B')
    c=graph.add_node('C')
    d=graph.add_node('D')
    e=graph.add_node('E')
    f=graph.add_node('F')
    
    graph.add_edge(a, b)
    graph.add_edge(a, c)

    graph.add_edge(b, c)
    graph.add_edge(b, e)
    graph.add_edge(b, d)
    
    graph.add_edge(c, e)
    
    graph.add_edge(d, e)
    graph.add_edge(d, f)
    
    graph.add_edge(e, f)
    
    return graph
