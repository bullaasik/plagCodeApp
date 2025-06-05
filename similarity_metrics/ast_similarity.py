import ast
from difflib import SequenceMatcher

def ast_similarity(s1, s2):
    """Вычисляет сходство AST деревьев двух фрагментов кода"""
    try:
        tree1 = ast.parse(s1)
        tree2 = ast.parse(s2)
        
        # Сравнение структуры AST
        dump1 = ast.dump(tree1)
        dump2 = ast.dump(tree2)
        
        # Используем SequenceMatcher для сравнения
        similarity = SequenceMatcher(None, dump1, dump2).ratio()
        
        return similarity
    except:
        return 0.0