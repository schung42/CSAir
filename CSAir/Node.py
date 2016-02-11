__author__ = 'ShaunChung'
from Edge import *

class Node:

    #Initialize a Node as a constructor
    #@param city - (string ary) city information
    def __init__(self,metro):
        self.code = metro['code']
        self.name = metro['name']
        self.country = metro['country']
        self.continent = metro['continent']
        self.timezone = metro['timezone']
        self.coordinates = metro['coordinates']
        self.population = metro['population']
        self.region = metro['region']
        self.edges = []

    # Add an Edge the array of edges
    # @param code - (string) The city code
    # @param dist - (int) The distance of the flight
    # @return void
    def add_edge(self, code, dist):
        self.edges.append(Edge(code, dist))

    # Get a list of destinations
    #@return list of Destinations
    def get_dest(self):
        destinations = []
        for edge in self.edges:
            destinations.append(edge.dest)
        return destinations

    def edit_node(self, data):
        self.name = data['name']
        self.country = data['country']
        self.continent = data['continent']
        self.timezone = data['timezone']
        self.coordinates = data['coordinates']
        self.population = data['population']
        self.region = data['region']
