import ast
import astor
import random
import re
import logging
from .syntax_checker import is_valid_code

logger = logging.getLogger(__name__)

def custom_obfuscate_code(code):
    if not code.strip():
        logger.warning("Пустой код передан для обфускации")
        return None
    try:
        tree = ast.parse(code)
        new_names = {}
        reserved = {'True', 'False', 'None', 'print', 'range', 'len', 'int', 'str', 'float'}
        for node in ast.walk(tree):
            if isinstance(node, ast.Name) and node.id not in new_names and node.id not in reserved:
                new_names[node.id] = f"var_{random.randint(1000, 9999)}"
        
        def transform_condition(node):
            if isinstance(node, ast.Compare) and len(node.ops) == 1:
                op = node.ops[0]
                if isinstance(op, (ast.Gt, ast.Lt, ast.GtE, ast.LtE)):
                    left, right = node.left, node.comparators[0]
                    inverse_ops = {ast.Gt: ast.LtE, ast.Lt: ast.GtE, ast.GtE: ast.Lt, ast.LtE: ast.Gt}
                    new_op = inverse_ops.get(type(op), op)
                    return ast.UnaryOp(
                        op=ast.Not(),
                        operand=ast.Compare(left=left, ops=[new_op()], comparators=[right])
                    )
            return node
        
        class ConditionTransformer(ast.NodeTransformer):
            def visit_If(self, node):
                node.test = transform_condition(node.test)
                self.generic_visit(node)
                return node
        
        tree = ConditionTransformer().visit(tree)
        
        def replace_names(code, name_map):
            for old_name, new_name in sorted(name_map.items(), key=lambda x: len(x[0]), reverse=True):
                code = re.sub(r"\b" + re.escape(old_name) + r"\b", new_name, code)
            return code
        
        obfuscated = replace_names(astor.to_source(tree), new_names)
        if is_valid_code(obfuscated):
            return obfuscated
        return None
    except Exception as e:
        logger.warning(f"Ошибка в пользовательской обфускации: {e}")
        return None