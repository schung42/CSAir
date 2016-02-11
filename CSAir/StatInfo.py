__author__ = 'ShaunChung'
import json
from cmath import sqrt

class StatInfo:
    def __init__(self):
        return

    # Returns the longest single flight in the network
    #@return a list of source city, destination and distance
    def longest_single_flight(self, graph):
        longest_distance = 0

        for key, node in graph.nodes.items():
            for entry in node.edges:
                distance = entry.dist
                if distance > longest_distance:
                    longest_distance = distance
                    srcNode = node.code
                    endNode = entry.dest
        return (srcNode, endNode, longest_distance)

        # Returns the shortest single flight in the network
        #@return a list of source city, destination and distance
    def shortest_single_flight(self, graph):
        shortest_distance = 1000000000
        for key, node in graph.nodes.items():
            for entry in node.edges:
                distance = entry.dist
                if distance < shortest_distance:
                    shortest_distance = distance
                    srcNode = node.code
                    endNode = entry.dest
        return (srcNode, endNode, shortest_distance)


    # Returns the average distance of all flights in network
    #@return a float avg distance
    def average_network_distance(self, graph):
        num_flights = 0
        sum = 0
        avg_dist = 0;
        for key, node in graph.nodes.items():
            for entry in node.edges:
                num_flights = num_flights + 1
                sum = sum + entry.dist
        avg_dist = sum / num_flights
        return avg_dist


    # Returns the largest population of all cities in network
    #@return a list of largest city code and population
    def largest_population(self, graph):
        largest_pop = 0
        largest_city_code = ''
        for key, node in graph.nodes.items():
            if largest_pop < node.population:
                largest_pop = node.population
                largest_city_code = node.code
        return(largest_city_code, largest_pop)


    # Returns the smallest population of all cities in network
    #@return a list of smallest city code and population
    def smallest_population(self, graph):
        smallest_pop = 1000000000
        smallest_city_code = ''
        for key, node in graph.nodes.items():
            if smallest_pop > node.population:
                smallest_pop = node.population
                smallest_city_code = node.code
        return(smallest_city_code, smallest_pop)

    # Returns the average of all populations in the network
    #@return a float avg population
    def average_network_population(self, graph):
        num_cities = 0
        sum = 0
        avg_pop = 0
        for key, node in graph.nodes.items():
            num_cities = num_cities + 1
            sum = sum + node.population
        avg_pop = sum / num_cities
        return avg_pop


    # Returns a list of city codes that are hub cities
    #@return list with multiple node.code these are hubs
    def get_hub(self, graph):
        city_codes = []
        max = 0
        for key, node in graph.nodes.items():
            if(len(node.edges) > max):
                city_codes = [node.code]
                max = len(node.edges)
            elif(len(node.edges) == max):
                city_codes.append(node.code)
        return city_codes


    # Returns a list of cities TO BE USED IN CONJUNCTION WITH GET ALL
    #@return list of node's codes and names
    def get_all_cities(self, graph):
        cities = []
        for key, node in graph.nodes.items():
            cities.append((node.code, node.name))
        return cities

    def get_map_string_all_cities(self, graph):
        map_string = ''
        for key, node in graph.nodes.iteritems():
            for entry in node.edges:
                if (map_string == ''):
                    map_string += node.code + '-' + entry.dest
                else:
                    map_string += ',+' + node.code + '-' + entry.dest
        return map_string

    # Saves the current network to the disk
    #@param - graph - the graph network you wish to save to 'save_data.json'
    def save_network_to_disk(self, graph):
        data = dict()
        data['metros'] = []
        data['routes'] = []
        for key, node in graph.nodes.items():
            data['metros'].append\
            (
                {'code': node.code,
                 'name': node.name,
                 'country': node.country,
                 'continent': node.continent,
                 'timezone': node.timezone,
                 'coordinates': node.coordinates,
                 'population': node.population,
                 'region': node.region}
            )
            for edge in node.edges:
                data['routes'].append({'ports': [node.code, edge.dest], 'distance': edge.dist})

        save_data = json.dumps(data)
        _file_ = open('save_data.json', 'w')
        _file_.write(save_data)
        return

    # Calculate the distance through a path of cities
    #@param graph - the graph you are taking in
    #@param cities - a list of cities (nodes)
    def multi_route_distance(self, graph, cities):
        length = len(cities)
        count = 0
        distance = []
        while count < length-1:
            node = graph.nodes.get(cities[count])
            if node is None:
                return
            for edge in node.edges:
                if cities[count+1]==edge.dest:
                    distance.append(edge.dist)
                    break
            count = count + 1
        return distance

    # Calculate the cost of a multi city trip based on pricing algorithm
    #@param graph - graph we are looking at
    #@param cities - cities that we are linking together
    #@param distance - distance between cities
    def multi_route_cost(self, graph, cities, distance):
        if distance is None:
            return
        first_leg = 0.35
        total_cost = 0
        total_distance = list(distance)
        while total_distance:
            first_leg = first_leg - 0.05
            if(first_leg <= 0):
                first_leg = 0
            leg = total_distance.pop(0)
            leg_cost = first_leg * leg
            total_cost = total_cost + leg_cost
        return total_cost

  # finds info on a route
  # @param graph
  # @param list of city codes
  # @return dictionary of info
    def route_info(self, graph, cities):
        info = {}
        info['distance'] = self.multi_route_distance(graph, cities)
        info['cost'] = self.multi_route_cost(graph, cities, info['distance'])
        return info























