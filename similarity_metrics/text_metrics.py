from difflib import SequenceMatcher
import re

def levenshtein_sim(a, b):
    if not a or not b:
        return 0.0
    return SequenceMatcher(None, a, b).ratio()

def token_based_sim(code1, code2):
    tokens1 = set(re.findall(r'\b\w+\b', code1))
    tokens2 = set(re.findall(r'\b\w+\b', code2))
    union = tokens1 | tokens2
    return len(tokens1 & tokens2) / len(union) if union else 0

def ngram_sim(code1, code2, n=3):
    tokens1 = re.findall(r'\b\w+\b', code1)
    tokens2 = re.findall(r'\b\w+\b', code2)
    
    def get_ngrams(tokens, n):
        return set(tuple(tokens[i:i+n]) for i in range(len(tokens)-n+1))
    
    ngrams1 = get_ngrams(tokens1, n)
    ngrams2 = get_ngrams(tokens2, n)
    union = ngrams1 | ngrams2
    return len(ngrams1 & ngrams2) / len(union) if union else 0