import ast

from astor.tree_walk import TreeWalk


class StripAnnotationsTransformer(TreeWalk):
    def pre_AnnAssign(self):
        node = ast.Assign(
            targets=[self.cur_node.target], value=self.cur_node.value
        )

        self.replace(node)
