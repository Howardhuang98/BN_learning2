from base.DAG import *
from base.visualization import *

g = DAG()
g.add_edge('a','b',weight=0.1)
g.add_edges_from([('b','c')])
print(g['a']['b'])
print(g['b']['c'])
draw(g)
