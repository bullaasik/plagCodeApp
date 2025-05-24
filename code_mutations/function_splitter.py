import ast
import astor
import random
import logging
from .syntax_checker import is_valid_code

logger = logging.getLogger(__name__)

def split_function_mutation(code):
    if not code.strip():
        logger.warning("Пустой код передан для мутации split-function")
        return None
    try:
        tree = ast.parse(code)
        class FunctionSplitter(ast.NodeTransformer):
            def visit_FunctionDef(self, node):
                if len(node.body) < 2:
                    return node
                split_idx = random.randint(1, len(node.body) - 1)
                sub_body = node.body[split_idx:]
                node.body = node.body[:split_idx]
                
                sub_func_name = f"sub_{node.name}_{random.randint(1000, 9999)}"
                sub_func = ast.FunctionDef(
                    name=sub_func_name,
                    args=node.args,
                    body=sub_body,
                    decorator_list=[],
                    returns=None
                )
                ast.fix_missing_locations(sub_func)
                
                call = ast.Expr(ast.Call(
                    func=ast.Name(id=sub_func_name, ctx=ast.Load()),
                    args=[ast.Name(id=arg.arg, ctx=ast.Load()) for arg in node.args.args],
                    keywords=[]
                ))
                node.body.append(call)
                
                return [node, sub_func]
        
        transformer = FunctionSplitter()
        new_tree = transformer.visit(tree)
        ast.fix_missing_locations(new_tree)
        new_code = astor.to_source(new_tree)
        if is_valid_code(new_code):
            return new_code
        else:
            logger.warning("Некорректный синтаксис после мутации split-function")
            return None
    except Exception as e:
        logger.warning(f"Ошибка в мутации split-function: {e}")
        return None