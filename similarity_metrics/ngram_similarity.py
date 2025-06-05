def ngram_similarity(s1, s2, n=3):

    def get_ngrams(text, n):
        words = text.split()
        ngrams = [tuple(words[i:i + n]) for i in range(len(words) - n + 1)]
        return set(ngrams) if ngrams else set()

    ngrams1 = get_ngrams(s1, n)
    ngrams2 = get_ngrams(s2, n)
    intersection = len(ngrams1.intersection(ngrams2))
    union = len(ngrams1.union(ngrams2))
    return intersection / union if union > 0 else 0.0