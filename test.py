import networkx as nx
import matplotlib.pyplot as plt

#g = nx.PlanarEmbedding()
g = nx.DiGraph()
g.add_nodes_from([1,2,3,4,5,6,7,8,9,10,11])
g.add_edge(1,2)
g.add_edge(2,4)
g.add_edge(1,3)
g.add_edge(3,4)
g.add_edge(1,4)
g.add_edge(2,5)
g.add_edge(5,6)
g.add_edge(6,4)
g.add_edge(3,7)
g.add_edge(7,8)
g.add_edge(8,4)
g.add_edge(6,9)
g.add_edge(8,10)
g.add_edge(9,4)
g.add_edge(9,11)
g.add_edge(11,4)
g.add_edge(11,4)

nx.draw(g,with_labels=True)
plt.draw()
plt.show()

