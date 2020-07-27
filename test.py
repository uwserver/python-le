import networkx as nx
import matplotlib.pyplot as plt

g = nx.DiGraph()

g.add_nodes_from(["a", "b", "c", "g", "d", "e", "f", "h", "i", "j", "k"])
g.add_edges_from([("a", "b"),("b", "g"),("a", "c"),("c", "g"),("a", "g"),("b", "d"),("d", "e"),("e", "g"),("c", "f"),
                  ("f", "h"),("h", "g"),("e", "i"),("h", "j"),("i", "g"),("i", "k"),("j", "g"),("j", "i"),("k", "g"),
                  ("k", "g")])

red_edges = [("a", "c"), ("c", "f"), ("f", "h"), ("h", "j"), ("j", "g"), ("k", "g"), ("a", "b"), ("b", "d"), ("d", "e"), ("e", "i")]

edge_colours = ['black' if not edge in red_edges else 'red' for edge in g.edges()]
black_edges = [edge for edge in g.edges() if edge not in red_edges]

pos = nx.planar_layout(g)
nx.draw_networkx_nodes(g, pos, cmap=plt.get_cmap('jet'), node_size = 500)
nx.draw_networkx_labels(g, pos)
nx.draw_networkx_edges(g, pos, edgelist=red_edges, edge_color='r', arrows=True)
nx.draw_networkx_edges(g, pos, edgelist=black_edges, arrows=True)
nx.draw_networkx_edge_labels(g,pos,edge_labels={("a", "b"): "AB",
                                                ("b", "g"): "AB",
                                                ("a", "c"): "AB",
                                                ("c", "g"): "AB",
                                                ("a", "g"): "AB",
                                                ("b", "d"): "AB",
                                                ("d", "e"): "AB",
                                                ("e", "g"): "AB",
                                                ("c", "f"): "AB",
                                                ("f", "h"): "AB",
                                                ("h", "g"): "AB",
                                                ("e", "i"): "AB",
                                                ("h", "j"): "AB",
                                                ("i", "g"): "AB",
                                                ("i", "k"): "AB",
                                                ("j", "g"): "AB",
                                                ("j", "i"): "AB",
                                                ("k", "g"): "AB",
                                                ("k", "g"): "AB"}, font_color='k', font_size='6')

plt.figure().suptitle("Planar Layout")
plt.axis('off')
nx.draw_planar(g, with_labels=True)
plt.show()
