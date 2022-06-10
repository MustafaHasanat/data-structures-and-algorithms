class Node:
    """
    This class is used to create a node in the graph.
    """

    def __init__(self, value):
        """a node has a value and a list of neighbors

        Args:
            value (any)
        """
        
        self.value = value

    def __str__(self):
        return self.value
    
    
class Edge:
    """
    This class is used to represent an edge in the graph. 
    """
    
    def __init__(self, node, weight=0):
        """_summary_

        Args:
            node (Node): a node 
            weight (int, optional): a weight for the edge. Defaults to 0.
        """
        
        self.node = node
        self.weight = weight
        
        
    def __str__(self):
        return str(self.node)


class Graph:
    """
    This class creates the adjacency list to represent a graph
    """

    def __init__(self):
        self.adjacency_list = {}
        

    def add_node(self, value): 
        """ 
        
        Arguments: value
        Returns: The added node
        Doing: Add a node to the graph        
        """     

        node = Node(value)
        self.adjacency_list[node] = []
        
        return node


    def add_edge(self, node1, node2, weight=0):
        """             
        Arguments: 2 nodes to be connected by the edge, weight (optional)
        Returns: nothing
        Adds a new edge between two nodes in the graph
        If specified, assign a weight to the edge
        Both nodes should already be in the Graph
        """
        
        if not node1 in self.adjacency_list.keys() or not node2 in self.adjacency_list.keys():
            raise Exception("One or more of the nodes doesn't exist in the graph")
        
        else:
            edge = Edge(node2, weight=weight)
            self.adjacency_list[node1].append(edge)


    def get_node(self):
        """ 
        Returns all nodes in graph as a collection (set, list, or similar)
        """
        
        nodes = []
        
        for node in self.adjacency_list.keys():
            nodes.append(node.value)
        
        return nodes


    def get_neighbors(self, node):
        """              
        Arguments: node
        Returns a collection of edges connected to the given node
        Include the weight of connection in returned collection           
        """
        
        if not node in self.adjacency_list.keys():
            raise Exception("The node doesn't exist in the graph")
        
        else:
        
            edges=[]
            
            for edge in self.adjacency_list[node]:
                edges.append([edge.node.value, edge.weight])
            
            return edges
       

    def size(self):
        """         
        Arguments: none
        Returns the total number of nodes in the graph
        """
        
        return len(self.adjacency_list)


    def __str__(self):
        """ """
        
        output = ""
        
        for node in self.adjacency_list.keys():
            output += f"{node.value} -> "

            for edge in self.adjacency_list[node]:
                output += f" {edge.node.value} ->"
            
            output += " Null\n"
        
        return output
        

if __name__ == '__main__':
    
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
     
    
    print(graph.get_neighbors(a))

        
