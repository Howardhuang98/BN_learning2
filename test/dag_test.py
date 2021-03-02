from base.DAG import *

g = DAG()
g.add_edge('a','b',weight=0.1)
print(g['a']['b'])
