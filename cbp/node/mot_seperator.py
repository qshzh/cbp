from .mot_node import MOTNode
import cbp.utils.np_utils as npu


class MOTSeperator(MOTNode):
    def make_message(self, recipient_node):
        product_out = self.prod2node(recipient_node)
        multi_idx = self.idx_dims(recipient_node)
        return npu.nd_multiexpand(
            product_out,
            recipient_node.potential.shape,
            multi_idx)

    def plot(self, graph):
        graph.add_node(
            self.name,
            color='blue',
            style='bold',
            shape='box',
            label=self.mot_name)
