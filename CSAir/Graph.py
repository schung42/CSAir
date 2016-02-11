__author__ = 'ShaunChung'

from Node import Node

class Graph:
    #Dictionary holds nodes and query functions
    def __init__(self):
        self.nodes = dict()

    #Add every node in the data set
    #@param metros - array from jsonfile
    def construct_nodes(self, metros):
        for metro in metros:
            self.nodes[metro['code']] = Node(metro)

    # Add an edge to a Node
    #@param routes - routes array from jsonfile
    #@param srcNode - source index
    #@param destNode - destination index
    def add_node_edge(self, routes, srcNode, destNode):
        node = self.nodes.get(routes['ports'][srcNode])
        node.add_edge(routes['ports'][destNode], routes['distance'])

    # Add all routes to nodes BIDIRECTIONAL
    #@param routes - routes aray from jsonfile
    def construct_edges(self, routes):
        for route in routes:
            self.add_node_edge(route, 0, 1)
            self.add_node_edge(route, 1, 0)

    # Retrieve the city that corresponds to code
    #@param code - (string) city code
    #@return Node (city) that corresponds to code
    def code_lookup_city(self, code):

        return self.nodes.get(code)

    # Remove a city and its routes based on city code
    #@param code = (string) city code to remove
    #@return no return just pop the city code and remove connected edges
    def remove_node(self, code):
        if(self.nodes.get(code)):
            self.nodes.pop(code)
            self.remove_edges_of_node(code)

    # Remove the nodes connected to a node
    #@ param code = (string) city code that edges must be deleted
    def remove_edges_of_node(self, code):
        for key, node in self.nodes.items():
            count = 0
            for edge in node.edges:
                if(edge.dest == code):
                    node.edges.pop(count)
                count  = count +1

    # Remove an edge between cities without deleting any nodes
    #@param src - source city
    #@param dst - destination city
    def remove_route_btwn_cities(self, src, dst):
        node = self.nodes.get(src)
        if node is not None:
            count = 0
            for edge in node.edges:
                if edge.dest == dst:
                    node.edges.pop(count)
                count = count + 1

    # Add a node to the map
    #@param data - dictionary of city information
    def add_node(self, data):
        if(not self.nodes.get(data['code'])):
            self.nodes[data['code']] = Node(data)

    # add a route between a src and destination
    #@param src - src node
    #@param destination - Destination node
    #@param distance - distance of two nodes
    def add_route(self, src, destination, distance):
        node = self.nodes.get(src)
        if node is not Node:
            node.add_edge(destination, distance)

    # Edit selected Node essentially just a wrapper
    #@param data -
    def edit_node(self, data):
        node = self.nodes.get(data['code'])
        if(node is not None):
            node.edit_node(data)















