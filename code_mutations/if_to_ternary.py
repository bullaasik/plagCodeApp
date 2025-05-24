import ast
import astor
import logging
from .syntax_checker import is_valid_code

logger = logging.getLogger(__name__)

def if_to_ternary_mutation(code):
    if not code.strip():
        logger.warning("Пустой код передан для мутации if-to-ternary")
        return None
    try:
        tree = ast.parse(code)
        class IfToTernaryTransformer(ast.NodeTransformer):
            def visit_If(self, node):
                self.generic_visit(node)
                if len(node.body) == 1 and len(node.orelse) == 1:
                    if (isinstance(node.body[0], ast.Assign) and
                        isinstance(node.orelse[0], ast.Assign) and
                        len(node.body[0].targets) == 1 and
                        len(node.orelse[0].targets) == 1 and
                        isinstance(node.body[0].targets[0], ast.Name) and
                        isinstance(node.orelse[0].targets[0], ast.Name) and
                        node.body[0].targets[0].id == node.orelse[0].targets[0].id):
                        var = node.body[0].targets[0].id
                        true_val = node.body[0].value
                        false_val = node.orelse[0].value
                        ternary = ast.Assign(
                            targets=[ast.Name(id=var, ctx=ast.Store())],
                            value=ast.IfExp(test=node.test, body=true_val, orelse=false_val)
                        )
                        ast.fix_missing_locations(ternary)
                        return ternary
                return node
        
        transformer = IfToTernaryTransformer()
        new_tree = transformer.visit(tree)
        ast.fix_missing_locations(new_tree)
        new_code = astor.to_source(new_tree)
        if is_valid_code(new_code):
            return new_code
        else:
            logger.warning("Некорректный синтаксис после мутации if-to-ternary")
            return None
    except Exception as e:
        logger.warning(f"Ошибка в мутации if-to-ternary: {e}")
        return None