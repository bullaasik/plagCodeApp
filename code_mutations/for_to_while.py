import ast
import astor
import logging
from .syntax_checker import is_valid_code

logger = logging.getLogger(__name__)

def for_to_while_mutation(code):
    if not code.strip():
        logger.warning("Пустой код передан для мутации for-to-while")
        return None
    try:
        tree = ast.parse(code)
        class ForToWhileTransformer(ast.NodeTransformer):
            def visit_For(self, node):
                if not (hasattr(node, 'iter') and isinstance(node.iter, ast.Call) and getattr(node.iter.func, 'id', None) == 'range'):
                    return node
                
                start = ast.Constant(value=0)
                step = ast.Constant(value=1)
                args = node.iter.args
                if len(args) == 1:
                    end = args[0]
                elif len(args) >= 2:
                    start = args[0]
                    end = args[1]
                    if len(args) == 3:
                        step = args[2]
                
                var = node.target.id if isinstance(node.target, ast.Name) else None
                if not var:
                    return node
                
                new_nodes = [
                    ast.Assign(
                        targets=[ast.Name(id=var, ctx=ast.Store())],
                        value=start
                    ),
                    ast.While(
                        test=ast.Compare(
                            left=ast.Name(id=var, ctx=ast.Load()),
                            ops=[ast.Lt()],
                            comparators=[end]
                        ),
                        body=node.body + [ast.AugAssign(
                            target=ast.Name(id=var, ctx=ast.Store()),
                            op=ast.Add(),
                            value=step
                        )],
                        orelse=node.orelse
                    )
                ]
                
                return new_nodes
        
        transformer = ForToWhileTransformer()
        new_tree = transformer.visit(tree)
        ast.fix_missing_locations(new_tree)
        new_code = astor.to_source(new_tree)
        
        if is_valid_code(new_code):
            return new_code
        else:
            logger.warning("Некорректный синтаксис после мутации for-to-while")
            return None
    except Exception as e:
        logger.warning(f"Ошибка в мутации for-to-while: {e}")
        return None