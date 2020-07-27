import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from io import BytesIO

g = nx.MultiDiGraph()

g.add_nodes_from(["a", "b", "c", "g", "d", "e", "f", "h", "i", "j", "k"])
g.add_edges_from([("a", "b"),("b", "g"),("a", "c"),("c", "g"),("a", "g"),("b", "d"),("d", "e"),("e", "g"),("c", "f"),
                  ("f", "h"),("h", "g"),("e", "i"),("h", "j"),("i", "k"),("j", "g"),("j", "i"),("k", "g"),("k", "g"),
                  ("k", "g")])

red_edges = [("a", "c"), ("c", "f"), ("f", "h"), ("h", "j"), ("j", "g"),
             ("k", "g"), ("a", "b"), ("b", "d"), ("d", "e"), ("e", "i")]

#edge_colours = ['black' if not edge in red_edges else 'red' for edge in g.edges()]
black_edges = [edge for edge in g.edges() if edge not in red_edges]
plt.figure().suptitle("Tree Selection")
plt.axis('off')

pos = nx.planar_layout(g)
nx.draw_networkx_nodes(g, pos, cmap=plt.get_cmap('jet'), node_size = 500)
nx.draw_networkx_labels(g, pos)
nx.draw_networkx_edges(g, pos, edgelist=red_edges, edge_color='r', arrows=True)
nx.draw_networkx_edges(g, pos, edgelist=black_edges, arrows=True)
nx.draw_networkx_edge_labels(g,pos,edge_labels={("a", "b"): "2",
                                                ("b", "g"): "4",
                                                ("a", "c"): "3",
                                                ("c", "g"): "5",
                                                ("a", "g"): "1",
                                                ("b", "d"): "6",
                                                ("d", "e"): "7",
                                                ("e", "g"): "10",
                                                ("c", "f"): "11",
                                                ("f", "h"): "9",
                                                ("h", "g"): "12",
                                                ("e", "i"): "13",
                                                ("h", "j"): "14",
                                                ("i", "k"): "15",
                                                ("j", "g"): "16",
                                                ("j", "i"): "17",
                                                ("k", "g"): "18",
                                                ("k", "g"): "19", # WTF r u doing?
                                                ("k", "g"): "20"  # you can't have repeated key in dictionary
                                                }, font_color='k', font_size='6')


plt.figure().suptitle("Pretty Layout")
plt.axis('off')

d=nx.drawing.nx_pydot.to_pydot(g)
plt.imshow(mpimg.imread(BytesIO(
    d.create_png(prog="dot.exe"))))

#nx.draw_planar(g, with_labels=True)
plt.show()
