import networkx as nx


class DAG(nx.DiGraph):
    """
    DAG类用来表示有向无环图
    它继承了network的Digraph，同时需要对一些常用的方法进行声明。
    """

    def __init__(self, incoming_graph_data=None, **attr):
        super(DAG, self).__init__(incoming_graph_data,**attr)
        cycles = []
        try:
            cycles = list(nx.find_cycle(self))
        except nx.NetworkXNoCycle:
            pass
        else:
            out_str = "Cycles are not allowed in a DAG."
            out_str += "\nEdges indicating the path taken for a loop: "
            out_str += "".join([f"({u},{v}) " for (u, v) in cycles])
            raise ValueError(out_str)

    def add_edge(self, u_of_edge, v_of_edge, weight= 0):
