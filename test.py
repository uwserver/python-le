import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from io import BytesIO

g = nx.MultiDiGraph()

g.add_nodes_from(["a", "b", "c", "g", "d", "e", "f", "h", "i", "j", "k"])
g.add_edges_from([("a", "b"),("b", "g"),("a", "c"),("c", "g"),("a", "g"),("b", "d"),("d", "e"),("e", "g"),("c", "f"),
                  ("f", "h"),("h", "g"),("e", "i"),("h", "j"),("i", "k"),("j", "g"),("j", "i"),("k", "g"),("k", "g"),
                  ("k", "g")])

edge_labels={
    ("a", "b"): ["2"],
    ("b", "g"): ["4"],
    ("a", "c"): ["3"],
    ("c", "g"): ["5"],
    ("a", "g"): ["1"],
    ("b", "d"): ["6"],
    ("d", "e"): ["7"],
    ("e", "g"): ["10"],
    ("c", "f"): ["11"],
    ("f", "h"): ["9"],
    ("h", "g"): ["12"],
    ("e", "i"): ["13"],
    ("h", "j"): ["14"],
    ("i", "k"): ["15"],
    ("j", "g"): ["16"],
    ("j", "i"): ["17"],
    ("k", "g"): ["18","19", "20"]}

tree={1,6,7,9,10,11,12,15,17,18}

plt.figure().suptitle("Pretty Layout")
plt.axis('off')

d=nx.drawing.nx_pydot.to_pydot(g)
for e in d.get_edges():
    e.set_label(edge_labels[(e.get_source(), e.get_destination())].pop())
    if int(e.get_label()) in tree:
        e.set_color('red')

# preview
plt.imshow(mpimg.imread(BytesIO(
    d.create_png(prog="dot.exe"))), interpolation='none')

# download image for full resolution
d.write_png("test2.png", prog="dot.exe")
plt.show()
