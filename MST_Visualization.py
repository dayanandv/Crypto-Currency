import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms.centrality.degree_alg import degree_centrality
from numpy import abs, max
from scipy.sparse import data

edges_to_be_removed = []

G = nx.read_gexf('coins_copy.gexf')
for u,v,weight in G.edges(data=True):
    weight = weight['weight']
    if weight < 0.5:
        print(u,v)
        edges_to_be_removed.append((u,v))
    else:
        if weight>0:
            weight = 1/weight
            if(weight=='NaN'):
                print(u, v, weight)
                break

for edge in edges_to_be_removed:
    G.remove_edge(edge[0],edge[1])

MST = nx.minimum_spanning_tree(G,ignore_nan=True)

degs = nx.degree(MST)
pos=nx.spectral_layout(MST)
nx.draw(MST, pos, node_size=[i * 100 for (v,i) in degs], with_labels=True)
labels = nx.get_edge_attributes(MST, 'weight')
# nx.draw_networkx_edge_labels(MST, pos, edge_labels=labels)
plt.show()


largest = max([val for (node, val) in MST.degree()])
print(largest)