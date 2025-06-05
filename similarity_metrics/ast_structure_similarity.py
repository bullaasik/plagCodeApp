import ast

def ast_structure_similarity(s1, s2):
    """Сравнивает структуру AST деревьев (без учета имен переменных)"""
    try:
        tree1 = ast.parse(s1)
        tree2 = ast.parse(s2)
        
        class Normalizer(ast.NodeTransformer):
            def visit_Name(self, node):
                return ast.Name(id='x', ctx=node.ctx)
        
        norm1 = Normalizer().visit(tree1)
        norm2 = Normalizer().visit(tree2)
        
        dump1 = ast.dump(norm1)
        dump2 = ast.dump(norm2)
        
        return SequenceMatcher(None, dump1, dump2).ratio()
    except:
        return 0.0