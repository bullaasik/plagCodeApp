def token_similarity(s1, s2):
    """
    Вычисляет сходство токенов между двумя строками с использованием коэффициента Жаккара.
    Возвращает значение от 0.0 (нет сходства) до 1.0 (полное сходство).
    """
    tokens1 = set(s1.split())
    tokens2 = set(s2.split())
    intersection = len(tokens1.intersection(tokens2))
    union = len(tokens1.union(tokens2))
    return intersection / union if union > 0 else 0.0