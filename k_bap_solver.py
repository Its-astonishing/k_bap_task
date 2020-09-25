import copy
from igraph import *

class k_bap:

    #Calculate g function value
    @staticmethod
    def calculate_g(list_of_distances):
        sum_of_distances = 0

        for distance in list_of_distances:
            sum_of_distances += distance

        return sum_of_distances

    @staticmethod
    def single_iter(graph, previous_g):
        result_g = previous_g
        result_edge = 0

        for current_v in range(1, len(graph.vs.indices)):
            graph_copy = copy.deepcopy(graph)
            graph_copy.add_edges([(0, current_v)])
            new_g = k_bap.calculate_g(graph_copy.shortest_paths_dijkstra(graph_copy.vs[0])[0])

            if new_g < result_g:
                result_g = new_g
                result_edge = current_v

        return (result_g, result_edge)

    @staticmethod
    def solve_task(graph, num_of_bookmarks_to_add):
        # Calculate g for the input graph
        current_g = k_bap.calculate_g(graph.shortest_paths_dijkstra(graph.vs[0])[0])

        graph_copy = copy.deepcopy(graph)

        graph_copy.es["is_new"] = [False] * len(graph_copy.es)
        last_edge_id = len(graph_copy.es) - 1

        for i in range(num_of_bookmarks_to_add):
            new_value_edge = k_bap.single_iter(graph_copy, current_g)
            current_g = new_value_edge[0]
            new_edge = new_value_edge[1]
            graph_copy.add_edges([(0, new_edge)])
            last_edge_id += 1
            graph_copy.es[last_edge_id]["is_new"] = True
            k_bap.print_solved_task_graph(graph_copy)

        return graph_copy

    @staticmethod
    def print_solved_task_graph(graph):
        visual_style = {}
        visual_style["edge_width"] = [1 + 2 * int(is_new) for is_new in graph.es["is_new"]]
        graph.vs["label"] = graph.vs["name"]
        color_dict = {"m": "blue", "f": "pink"}
        graph.vs["color"] = [k_bap.colorize(name) for name in graph.vs["name"]]

        plot(graph, **visual_style)

    @staticmethod
    def colorize(vertex_name):
        if vertex_name == "r":
            return "blue"
        else:
            return "red"