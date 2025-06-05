import numpy as np
from gensim.models import Word2Vec
from gensim.utils import simple_preprocess
import ast
import logging
from collections import defaultdict

logger = logging.getLogger(__name__)

class CodeTokenizer:
    """Токенизация Python-кода с сохранением структуры"""
    def __init__(self):
        self.keywords = {
            'def', 'for', 'while', 'if', 'else', 'return', 
            'import', 'from', 'class', 'try', 'except'
        }

    def tokenize(self, code):
        """Разбивает код на семантические токены"""
        try:
            tree = ast.parse(code)
            tokens = []
            
            for node in ast.walk(tree):
                if isinstance(node, ast.Name):
                    tokens.append(f"VAR_{node.id}")
                elif isinstance(node, ast.FunctionDef):
                    tokens.append(f"FUNC_{node.name}")
                elif isinstance(node, ast.Call):
                    tokens.append(f"CALL_{ast.unparse(node.func)}")
                elif isinstance(node, (ast.Str, ast.Num)):
                    tokens.append("LITERAL")
                elif any(isinstance(node, t) for t in [ast.For, ast.While, ast.If]):
                    tokens.append(type(node).__name__.upper())
            
            return tokens
        except Exception as e:
            logger.warning(f"Tokenization error: {e}")
            return simple_preprocess(code)

word2vec_model = None

def train_word2vec(corpus):
    """Обучение модели на коллекции кодов"""
    global word2vec_model
    tokenizer = CodeTokenizer()
    tokenized_corpus = [tokenizer.tokenize(code) for code in corpus]
    
    word2vec_model = Word2Vec(
        sentences=tokenized_corpus,
        vector_size=100,
        window=5,
        min_count=1,
        workers=4,
        epochs=10
    )
    return word2vec_model

def code2vec(code):
    """Векторизация кода с помощью Word2Vec"""
    global word2vec_model
    if word2vec_model is None:
        raise ValueError("Word2Vec model not trained")
    
    tokenizer = CodeTokenizer()
    tokens = tokenizer.tokenize(code)
    vectors = []
    
    for token in tokens:
        if token in word2vec_model.wv:
            vectors.append(word2vec_model.wv[token])
        else:
            vectors.append(np.zeros(word2vec_model.vector_size))
    
    return np.mean(vectors, axis=0) if vectors else np.zeros(word2vec_model.vector_size)