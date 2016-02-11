__author__ = 'ShaunChung'
import Node
import StatInfo
import webbrowser


class TextUI:
    def __init__(self):
        return

    def print_menu(self):
        print("Welcome to CSAir!")
        print("----------------------------")
        print("Please Select a Choice or 'x' to quit")
        print("Enter 'Menu' to Redisplay Menu")
        print("1 - City Information")
        print("2 - Longest Flight")
        print("3 - Shortest Flight")
        print("4 - Average Flight Distance")
        print("5 - Biggest Population")
        print("6 - Smallest Population")
        print("7 - Average Population")
        print("8 - Hub Cities")
        print("9 - All Cities")
        print("10 - See Route Map")
        print("11 - Add City")
        print("12 - Add Route")
        print("13 - Remove City")
        print("14 - Remove Route")
        print("15 - Edit City")
        print("16 - Save Network to Disk")
        print("17 - Route Information")



    # Helper for the UI_city_info function
    # UI_city_info is function that deals with user
    # This is backend
    def print_city_info(self, graph, code):
        node = graph.code_lookup_city(code)
        if(node is None):
            print("Invalid city")
        else:
            print('Code: ' + node.code)
            print('Name: ' + node.name)
            print('Country: ' + node.country)
            print('Continent: ' + node.continent)
            print('Timezone: ' + str(node.timezone))
            print('Coordinates: ' + str(node.coordinates))
            print('Population: ' + str(node.population))
            print('Region: ' + str(node.region))
            routes_to_other_nodes = node.edges
            for item in routes_to_other_nodes:
                print("Destination: " + item.dest + " Distance: " + str(item.dist))

    # Get Information about city
    def UI_city_info(self, graph):
        print("Enter a city code for data about it: ")
        code = raw_input()
        self.print_city_info(graph, code)

    # Print flight information
    # From: CityCode To: CityCode Distance: Num
    def print_flight(self, flight):
        print('From:' + flight[0] + ' To:' + flight[1] + ' Distance:' + str(flight[2]))

    # Prints the average distance of every edge in the network
    def print_average_distance(self, average_network_distance):
        print('Average flight distance: ' + str(average_network_distance))

    # Prints the population
    def print_population(self, population):
        print('Population: ' + str(population))

    # Prints cities
    def print_cities(self, cities):
        for entry in cities:
            print( entry[1] + ', Code: ' + entry[0])

    # open up a URL with all cities
    def display_map_all(self, map_string):
        url = 'http://www.gcmap.com/mapui?P=' + map_string
        webbrowser.open(url, new=2)

    # Display Menu for Adding a city
    def add_city_menu(self):
        data = dict()
        print("Enter City Code: ")
        data['code'] = raw_input()
        print("Enter City Name: ")
        data['name'] = raw_input()
        print("Enter Country: ")
        data['country'] = raw_input()
        print("Enter Continent: ")
        data['continent'] = raw_input()
        print("Enter Timezone: ")
        data['timezone'] = raw_input()
        print("Enter Coordinates: ")
        data['coordinates'] = raw_input()
        print("Enter Population: ")
        data['population'] = raw_input()
        print("Enter Region: ")
        data['region'] = raw_input()
        return data

    # Display the Menu for adding a route
    def add_route_menu(self):
        data = dict()
        print("Enter Source City: ")
        data['src'] = raw_input()
        print("Enter Destination City: ")
        data['dest'] = raw_input()
        print("Enter Distance: ")
        data['dist'] = raw_input()
        return data

    # Display the menu for removing a node
    def remove_node_menu(self):
        print("Please Enter City Code to Remove: ")
        cityCode = raw_input()
        return cityCode

    # Display menu for removing a route
    def remove_route_menu(self):
        print("Please Enter Source City: ")
        srcCity = raw_input()
        print("Please Enter Destination City: ")
        destCity = raw_input()
        print("Route between " + srcCity + " And " + destCity + " Removed")
        return {'src': srcCity, 'dest': destCity}

    # Display Meny for editing a city
    def edit_city_menu(self):
        data = dict()
        print("Enter City Code to Change: ")
        data['code'] = raw_input()
        print("Enter New City Name: ")
        data['name'] = raw_input()
        print("Enter New Country: ")
        data['country'] = raw_input()
        print("Enter New Continent: ")
        data['continent'] = raw_input()
        print("Enter New Timezone: ")
        data['timezone'] = raw_input()
        print("Enter New Coordinates: ")
        data['coordinates'] = raw_input()
        print("Enter New Population: ")
        data['population'] = raw_input()
        print("Enter New Region: ")
        data['region'] = raw_input()
        return data

    # Parse user input for route_info calculation
    def route_menu(self):
        print("Enter the city codes separated by ',': \n")
        nodes = raw_input()
        return nodes.split(',')

    # Print computed values from StatInfo
    def print_multi_route_info(self, total_route):
        print("Total Distance: " + str(sum(total_route['distance'])))
        print("Total Cost: " + str(total_route['cost']))





















