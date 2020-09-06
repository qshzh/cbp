from .msg_graph import MsgGraph
from .base_graph import BaseGraph


class MOTGraph(MsgGraph):
    def __init__(self):
        """
        * ``varnode2mot` map: while cluster should be used to calculate maring of varnode
        """
        self.varnode2mot = {}
        super().__init__()

    def add_cluster(self, node):
        node_name = self.add_factornode(node)
        if node.isconstrained:
            self.constrained_names.append(node_name)
        self.register_var(node)
        return node_name

    def add_seperator(self, node):
        return BaseGraph.add_varnode(self, node)

    def register_var(self, mot_node):
        for var_name in mot_node.list_varname:
            if var_name not in self.varnode2mot:
                self.varnode2mot[var_name] = mot_node
            else:
                if mot_node.rv_dim < self.varnode2mot[var_name].rv_dim:
                    self.varnode2mot[var_name] = mot_node

    def delete_node(self):
        pass

    def export_node_marginal(self):
        return {
            name: node.margin_vars([name]) for name,
            node in self.varnode2mot.items()}