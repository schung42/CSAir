__author__ = 'ShaunChung'
from unittest import TestCase
import Graph
import StatInfo

import json

class TestFlightGraph(TestCase):

    def init_tests(self):
        f = open('data.json', 'r')
        parsed_JSON = json.loads(f.read())
        self.graphs = Graph()
        self.graphs.construct_nodes(parsed_JSON['metros'])
        self.graphs.contstruct_edges(parsed_JSON['routes'])
        self.stats = StatInfo()

    def test_init(self):
        assert (self.graphs.nodes.get('SFO').name == 'San Francisco')

    def test_longest_flight(self):
        assert (self.stats.longest_single_flight(self.graphs) == ('SYD', 'LAX', 12051))

    def test_shortest_flight(self):
        assert(self.stats.shortest_single_flight(self.graphs) == ('NYC', 'WAS', 334))

    def test_average_dist(self):
        assert (self.stats.average_network_distance(self.graphs) == 2300)

    def test_largest_pop(self):
        assert self.stats.largest_population(self.graphs) == ('TYO', 34000000)

    def test_smallest_pop(self):
        assert self.stats.smallest_population(self.graphs) == ('ESS', 589900)

    def test_average_network_pop(self):
        assert self.stats.average_network_population(self.graphs) == 11796143








