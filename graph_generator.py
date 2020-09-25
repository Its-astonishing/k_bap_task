from igraph import *
import random

class graph_generator:
    def __init__(self, allow_loops = False):
        self.allow_loops = allow_loops
        self.directed = True

    # Generates graph with in two passes
    #
    # The first pass: add new vertex, add new edge randomly
    # from new vertex to already existing vertex (probability
    # that edge starts from recently added vertex is higher)
    #
    # The second pass: go through all vertices, add random edge
    def generate_graph_two_passes(self, num_v, edge_factor, second_pass_factor):
        result_graph = Graph(directed = self.directed)  # Create result graph
        result_graph.add_vertex("r")  # Add root vertex

        v_left_to_add = num_v - 1
        current_prob = random.random()
        current_bound = edge_factor

        while v_left_to_add > 0:
            for current_v in range(0, len(result_graph.vs.indices)):
                if current_prob < current_bound:
                    result_graph.add_vertex(len(result_graph.vs.indices))
                    last_v_index = len(result_graph.vs.indices) - 1
                    result_graph.add_edges([(current_v, last_v_index)])
                    v_left_to_add -= 1
                    current_prob = random.random()
                    current_bound = edge_factor
                    break
                current_bound *= 1.1

        for first_v in range(0, len(result_graph.vs.indices)):
            for second_v in range(0, len(result_graph.vs.indices)):

                if first_v == second_v and self.allow_loops is False:
                    continue

                new_edge_creates_loop = graph_generator.common_member(result_graph.incident(first_v),
                                                                      result_graph.incident(second_v, mode=IN))

                if self.allow_loops is False and new_edge_creates_loop is True:
                    continue

                if random.random() < second_pass_factor :
                    result_graph.add_edges([(first_v, second_v)])

        return result_graph

    @staticmethod
    def common_member(a, b):
        a_set = set(a)
        b_set = set(b)

        if len(a_set.intersection(b_set)) > 0:
            return True

        return False
