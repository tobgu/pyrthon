import ast


class PyrsistentTransformer(ast.NodeTransformer):
    def visit_Module(self, node):
        node = self.generic_visit(node)
        import_node = ast.ImportFrom(module='pyrsistent', names=[ast.alias(name='pvector'), ast.alias(name='pmap'), ast.alias(name='pset')], level=0)
        node.body.insert(0, import_node)
        return node

    def _visit_collection(self, node, pname):
        node = self.generic_visit(node)
        name_node = ast.Name(id=pname, ctx=ast.Load())
        new_node = ast.Call(func=name_node, args=[node], keywords=[])
        return new_node

    @staticmethod
    def _is_empty_set_call(node):
        return isinstance(node.func, ast.Name) and node.func.id == 'set' and not node.args

    def visit_Call(self, node):
        if self._is_empty_set_call(node):
            name_node = ast.Name(id='pset', ctx=ast.Load())
            return ast.Call(func=name_node, args=[], keywords=[])

        return self.generic_visit(node)

    def visit_Dict(self, node):
        return self._visit_collection(node, 'pmap')

    def visit_DictComp(self, node):
        return self._visit_collection(node, 'pmap')

    def visit_List(self, node):
        return self._visit_collection(node, 'pvector')

    def visit_ListComp(self, node):
        return self._visit_collection(node, 'pvector')

    def visit_Set(self, node):
        return self._visit_collection(node, 'pset')

    def visit_SetComp(self, node):
        return self._visit_collection(node, 'pset')


def transform(src):
    """ Transforms the given source to use pvectors, pmaps and psets to replace built in structures """
    tree = ast.parse(src)
    transformer = PyrsistentTransformer()
    new_tree = transformer.visit(tree)
    ast.fix_missing_locations(new_tree)
    return new_tree