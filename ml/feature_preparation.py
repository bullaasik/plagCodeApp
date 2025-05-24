import numpy as np
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import StandardScaler
from similarity_metrics.code2vec import code2vec

def prepare_ml_data(results, orig_codes, plag_codes, scaler=None, is_training=False):
    # Проверка входных данных
    if not results or len(results) == 0:
        raise ValueError("Results is empty")

    # Извлечение метрик
    X = np.array([[r[1], r[2], r[3], r[4], r[5]] for r in results])  # Levenshtein, Token, AST, N-gram, AST Structure
    y = np.array([r[6] for r in results])  # Labels

    # Добавление векторных представлений через code2vec
    vec1 = code2vec(orig_codes[0])
    vec2 = code2vec(plag_codes[0])
    if vec1 is not None and vec2 is not None:
        vec1_mean = np.mean(vec1, axis=0) if vec1.shape[0] > 0 else np.zeros(vec1.shape[1])
        vec2_mean = np.mean(vec2, axis=0) if vec2.shape[0] > 0 else np.zeros(vec2.shape[1])
        vec_diff = vec1_mean - vec2_mean
        X = np.hstack((X, vec_diff.reshape(1, -1)))

    # Масштабирование признаков
    if is_training:
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
    else:
        if scaler is None:
            raise ValueError("Scaler must be provided for inference mode")
        X_scaled = scaler.transform(X)

    # Динамическое определение n_components для SVD
    n_samples, n_features = X_scaled.shape
    n_components = min(n_features, n_samples) - 1 if min(n_features, n_samples) > 1 else 1

    if n_components > 1:
        svd = TruncatedSVD(n_components=n_components, random_state=42)
        X_reduced = svd.fit_transform(X_scaled)
    else:
        X_reduced = X_scaled

    return X_reduced, y, scaler if is_training else None