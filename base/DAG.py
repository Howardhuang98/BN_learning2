import networkx as nx


class DAG(nx.DiGraph):
    """
    DAG类用来表示有向无环图
    它继承了network的Digraph，同时需要对一些常用的方法进行声明。
    """

    def __init__(self, incoming_graph_data=None, **attr):
        super(DAG, self).__init__(incoming_graph_data, **attr)
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

    def add_edge(self, u_of_edge, v_of_edge, weight=0):
        """
        增加 u->v 的边，默认权重为0
        :param u_of_edge:
        :param v_of_edge:
        :param weight: default=0
        :return:
        """
        super(DAG, self).add_edge(u_of_edge, v_of_edge, weight=weight)

    def add_edges_from(self, ebunch_to_add, weight=0):
        """
        批量增加edges,默认weight=0
        :param ebunch_to_add: list or other hashable item, for example:[('a','b'),('b','c')]
        """
        super(DAG, self).add_edges_from(ebunch_to_add, weight=weight)
