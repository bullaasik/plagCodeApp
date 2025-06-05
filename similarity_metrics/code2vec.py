import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import re

def tokenize_code(code):
    tokens = re.findall(r'\b\w+\b', code)
    return ' '.join(tokens)

vectorizer = TfidfVectorizer(max_features=50)

def code2vec(code):
    try:
        tokens = tokenize_code(code)
        vec = vectorizer.fit_transform([tokens])
        return vec.toarray()
    except:
        return np.zeros((1, 50))