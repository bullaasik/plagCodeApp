import ast
import astor
from difflib import SequenceMatcher
import logging
from code_mutations.syntax_checker import is_valid_code

logger = logging.getLogger(__name__)

def normalize_code(code):
    try:
        tree = ast.parse(code)
        return astor.to_source(tree)
    except Exception as e:
        logger.warning(f"Ошибка нормализации кода: {e}")
        return code

def ast_sim(code1, code2):
    try:
        code1 = normalize_code(code1)
        code2 = normalize_code(code2)
        tree1 = ast.parse(code1)
        tree2 = ast.parse(code2)
        return SequenceMatcher(None, ast.dump(tree1), ast.dump(tree2)).ratio()
    except Exception as e:
        logger.warning(f"Ошибка парсинга AST: {e}")
        return 0

def ast_structure_sim(code1, code2):
    try:
        tree1 = ast.parse(normalize_code(code1))
        tree2 = ast.parse(normalize_code(code2))
        def count_nodes(tree):
            return sum(1 for _ in ast.walk(tree))
        return min(count_nodes(tree1), count_nodes(tree2)) / max(count_nodes(tree1), count_nodes(tree2))
    except Exception as e:
        logger.warning(f"Ошибка в AST structure sim: {e}")
        return 0