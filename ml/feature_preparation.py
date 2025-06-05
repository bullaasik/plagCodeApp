import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from similarity_metrics.code2vec import code2vec

def prepare_ml_data(results, orig_codes, plag_codes, scaler=None, is_training=False):
    # Базовые метрики
    X = np.array([[r[1], r[2], r[3], r[4], r[5]] for r in results])
    
    # Добавляем векторные представления
    vec1 = code2vec(orig_codes[0])
    vec2 = code2vec(plag_codes[0])
    vec_diff = np.abs(vec1 - vec2).flatten()
    
    X = np.hstack([X, vec_diff])
    
    if is_training:
        scaler = StandardScaler()
        X = scaler.fit_transform(X)
    else:
        X = scaler.transform(X)
    
    # Уменьшение размерности
    pca = PCA(n_components=min(X.shape[0], X.shape[1]))
    X = pca.fit_transform(X)
    
    y = np.array([r[6] for r in results])
    
    return X, y, scaler if is_training else None

def prepare_ml_data(results, orig_codes, plag_codes, scaler=None, is_training=False):
    # Базовые метрики
    X = np.array([[r[1], r[2], r[3], r[4], r[5]] for r in results])
    
    # Добавляем векторные представления
    vec1 = code2vec(orig_codes[0])
    vec2 = code2vec(plag_codes[0])
    vec_diff = np.abs(vec1 - vec2).flatten()
    
    X = np.hstack([X, vec_diff])
    
    if is_training:
        scaler = StandardScaler()
        X = scaler.fit_transform(X)
    else:
        X = scaler.transform(X)
    
    # Уменьшение размерности
    pca = PCA(n_components=min(X.shape[0], X.shape[1]))
    X = pca.fit_transform(X)
    
    y = np.array([r[6] for r in results])
    
    return X, y, scaler if is_training else None