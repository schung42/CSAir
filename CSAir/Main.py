__author__ = 'ShaunChung'
import json
from Graph import Graph
from StatInfo import StatInfo
from TextUI import TextUI
import webbrowser


class Main:
    def __init__ (self):
        return

    def parse_file(self, graphs, files):
        for file in files:
            f = open(file, 'r')
            parsed_JSON = json.loads(f.read())
            graphs.construct_nodes(parsed_JSON['metros'])
            graphs.construct_edges(parsed_JSON['routes'])

    def main(self):
        UI = TextUI()
        files = ['data.json', 'CU_data.json']
        g = Graph()
        self.parse_file(g ,files)
        stats = StatInfo()
        UI.print_menu()
        while(True):
            code = raw_input()
            if(code == 'x'):
                exit(0)
            elif(code == '1'):
                UI.UI_city_info(g)
            elif(code == '2'):
                longest_flight = stats.longest_single_flight(g)
                UI.print_flight(longest_flight)
            elif(code == '3'):
                shortest_flight = stats.shortest_single_flight(g)
                UI.print_flight(shortest_flight)
            elif(code == '4'):
                average_flight = stats.average_network_distance(g)
                UI.print_average_distance(average_flight)
            elif(code == '5'):
                largest_pop = stats.largest_population(g)
                UI.print_population(largest_pop)
            elif(code == '6'):
                smallest_pop = stats.smallest_population(g)
                UI.print_population(smallest_pop)
            elif(code == '7'):
                average_pop = stats.average_network_population(g)
                UI.print_population(average_pop)
            elif(code == '8'):
                hub_cities = stats.get_hub(g)
                print(hub_cities)
            elif(code == '9'):
                cities = stats.get_all_cities(g)
                UI.print_cities(cities)
            elif(code == '10'):
                print("Enter City Codes Separated by '-', Enter 'See All' to see all cities")
                input_var = raw_input()
                if input_var == "See All":
                    map_string = stats.get_map_string_all_cities(g)
                    UI.display_map_all(map_string)
                else:
                    URL = 'http://www.gcmap.com/mapui?P='
                    ret_URL = URL + input_var
                    webbrowser.open(ret_URL, new=2)
            elif(code == '11'):
                data = UI.add_city_menu()
                g.add_node(data)
                print(data['code'] + " Added")
            elif(code == '12'):
                data = UI.add_route_menu()
                g.add_route(data['src'], data['dest'], data['dist'])
                print("Route Added from: " + data['src'] + " To: " + data['dest'])
            elif(code == '13'):
                cityCode = UI.remove_node_menu()
                g.remove_node(cityCode)
                print(cityCode + " Removed")
            elif(code == '14'):
                data = UI.remove_route_menu()
                g.remove_route_btwn_cities(data['src'], data['dest'])
            elif(code == '15'):
                data = UI.edit_city_menu()
                g.edit_node(data)
                print(data['code'] + " Changed")
            elif(code == '16'):
                stats.save_network_to_disk(g)
                print("Network Saved to save_data.json")
            elif(code == '17'):
                cities = UI.route_menu()
                total_route = stats.route_info(g, cities)
                UI.print_multi_route_info(total_route)
            elif(code == 'Menu'):
                UI.print_menu()










