from similarity_metrics.code2vec import code2vec, train_word2vec
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import logging

logger = logging.getLogger(__name__)

def prepare_ml_data(results, orig_codes, plag_codes, scaler=None, is_training=False):
    # 1. Обучение Word2Vec при первом запуске
    if is_training:
        train_word2vec(orig_codes + plag_codes)
    
    # 2. Базовые метрики
    X = np.array([[r[1], r[2], r[3], r[4], r[5]] for r in results])
    
    # 3. Векторные представления через Word2Vec
    vec_diffs = []
    for orig, plag in zip(orig_codes, plag_codes):
        vec1 = code2vec(orig).reshape(1, -1)
        vec2 = code2vec(plag).reshape(1, -1)
        vec_diff = np.abs(vec1 - vec2).flatten()
        vec_diffs.append(vec_diff)
    
    X = np.hstack([X, np.array(vec_diffs)])
    
    # 4. Масштабирование
    if is_training:
        scaler = StandardScaler()
        X = scaler.fit_transform(X)
    else:
        X = scaler.transform(X)
    
    # 5. Уменьшение размерности
    pca = PCA(n_components=min(X.shape[1], 10))
    X = pca.fit_transform(X) if is_training else pca.transform(X)
    
    y = np.array([r[6] for r in results])
    
    return X, y, scaler