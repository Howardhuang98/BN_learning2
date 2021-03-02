import matplotlib.pyplot as plt
import networkx as nx

def draw(G):
    nx.draw(G,with_labels=True)
    plt.savefig("PIC.png")