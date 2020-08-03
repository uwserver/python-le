import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from io import BytesIO

g = nx.MultiDiGraph()

g.add_nodes_from(["a", "b", "c", "g", "d", "e", "f", "h", "i", "j", "k"])
g.add_edges_from([("a", "b"),("b", "g"),("a", "c"),("c", "g"),("a", "g"),
                  ("b", "d"),("d", "e"),("e", "g"),("c", "f"),
                  ("f", "h"),("h", "g"),("e", "i"),("d","f"),("h", "j"),
                  ("i", "k"),("j", "g"),("j", "i"),("k", "g"),("k", "g"),
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
    ("d", "f"): ["8"],
    ("h", "g"): ["12"],
    ("e", "i"): ["13"],
    ("h", "j"): ["14"],
    ("i", "k"): ["15"],
    ("j", "g"): ["16"],
    ("j", "i"): ["17"],
    ("k", "g"): ["18","19", "20"]}

edges_ = set(range(1,21))
tree={1,6,7,9,10,11,12,15,17,18}
cotree = edges_-tree

adjacency_list = dict()
for u,v in g.edges():
    adjacency_list.setdefault(u, dict())[v] = 1
    adjacency_list.setdefault(v, dict())[u] = -1

label_map = dict()
for e in edge_labels:
    for i in edge_labels[e]:
        label_map[int(i)] = e

# find f-cutset
def fcutset(t):
    """t is in integer representing an edge in tree
    return the cutset list corresponding to t
    since every edge in the tree is a bridge, removing the bridge
    gives exactly two components from the tree.
    We then find the cut induced by the component.
    
    The implementation is extremely messy. But given the shitty data
    structures I had to work with, cleaning up this would be a chore.
    So don't bother.
    """
    u,v = label_map[t]
    component = [ u ]

    pos = u
    prev = v
    more = True
    
    while more:
        more=False
        for n in adjacency_list[pos]:
            if n == prev:
                continue
            labels = []
            if (pos,n) in edge_labels:
                labels.extend(edge_labels[(pos,n)])
            elif (n,pos) in edge_labels:
                labels.extend(edge_labels[(n,pos)])
            bb = False
            for label in labels:
                if int(label) in tree:
                    component.append(n)
                    prev = pos
                    pos = n
                    more = True
                    bb = True
                    break
            if bb:
                break
    # return component for debugging
    
    collect_cot = []
    for x in component:
        for y in adjacency_list[x]:
            labels = []
            labels.extend(edge_labels.get((x,y), []))
            labels.extend(edge_labels.get((y,x), []))
            for label in labels:
                if int(label) not in tree:
                    collect_cot.append(int(label))
    return component, collect_cot

m = []
tree_sorted= sorted(tree)
cotree_sorted= sorted(cotree)
print("f-cutset matrix")
print(sorted(tree), sorted(cotree))
for e in sorted(list(tree)):
    tpart=[0]*len(tree_sorted)
    tpart[tree_sorted.index(e)] = 1

    cotpart=[0]*len(cotree_sorted)
    component, cutset = fcutset(e)
    if e == 10:
        print(component, cutset)
    
    # find direction multiplier
    mult = 1
    u, v = label_map[e]
    if v in component:
        mult = -1
    
    for x in cutset:
        y,z = label_map[x]
        weight = 1 if y in component else -1
        cotpart[cotree_sorted.index(x)]=mult*weight
    m.append(tpart+cotpart)


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


