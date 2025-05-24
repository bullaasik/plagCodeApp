def levenshtein(s1, s2):
    """
    Вычисляет нормализованное расстояние Левенштейна между двумя строками.
    Возвращает значение от 0.0 (идентичны) до 1.0 (полностью различны).
    """
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    max_len = max(len(s1), len(s2))
    return previous_row[-1] / max_len if max_len > 0 else 0.0