from igraph import *
import graph_generator
from k_bap_solver import *
import collections

graph_gen = graph_generator.graph_generator()

gr = graph_gen.generate_graph_two_passes(13, 0.009, 0.01)

gr.vs["label"] = gr.vs["name"]
#color_dict = {"m": "blue", "f": "pink"}
gr.vs["color"] = [k_bap.colorize(name) for name in gr.vs["name"]]
plot(gr)

gr_2 = k_bap.solve_task(gr, 4)
k_bap.print_solved_task_graph(gr_2)

