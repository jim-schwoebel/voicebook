'''
text_network.py

Use the networkX library to build a network.
'''
import networkx as nx
import matplotlib.pyplot as plt

transcript=open('./data/test.txt').read()
transcript=transcript.split()
uniquewords=list()

G = nx.Graph()
for i in range(len(transcript)):
    if transcript[i] not in uniquewords:
        uniquewords.append(transcript[i])
        G.add_edge(transcript[i], uniquewords[len(uniquewords)-1])

nx.clustering(G)
        
# draw graph 
nx.draw(G)
plt.savefig("network.png")
