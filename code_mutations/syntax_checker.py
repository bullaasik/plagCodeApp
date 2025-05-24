import ast
import logging

logger = logging.getLogger(__name__)

def is_valid_code(code):
    if not code.strip():
        logger.warning("Пустой код передан для проверки синтаксиса")
        return False
    try:
        ast.parse(code)
        return True
    except SyntaxError as e:
        logger.warning(f"Некорректный синтаксис: {e}")
        return False