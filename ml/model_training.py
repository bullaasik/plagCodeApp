import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV
from sklearn.metrics import classification_report
import shap
import matplotlib.pyplot as plt
import logging

logger = logging.getLogger(__name__)

def analyze_features(model, X, feature_names):
    try:
        logger.debug("Запуск SHAP-анализа...")
        explainer = shap.TreeExplainer(model.named_steps['clf'])
        shap_values = explainer.shap_values(X)
        
        plt.figure(figsize=(10, 6))
        shap.summary_plot(shap_values, X, feature_names=feature_names, show=False)
        plt.tight_layout()
        plt.savefig('shap_summary.png')
        plt.close()
        logger.info("SHAP summary plot сохранён как 'shap_summary.png'")
        
        shap_importance = np.abs(shap_values[1]).mean(axis=0)
        top_features = sorted(zip(feature_names, shap_importance), key=lambda x: x[1], reverse=True)[:5]
        logger.info("Топ-5 наиболее значимых признаков:")
        for name, importance in top_features:
            logger.info(f"Признак: {name}, SHAP importance: {importance:.4f}")
    except Exception as e:
        logger.error(f"Ошибка при анализе SHAP: {e}", exc_info=True)

def train_model(X, y):
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    reports = []

    param_grid = {
        'clf__n_estimators': [100, 200, 300],
        'clf__max_depth': [10, 20, None],
        'clf__min_samples_split': [2, 5]
    }

    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('clf', RandomForestClassifier(random_state=42, class_weight={0: 2.0, 1: 1.0}))
    ])

    X_train_full, X_test, y_train_full, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    for fold, (train_idx, val_idx) in enumerate(skf.split(X_train_full, y_train_full), 1):
        X_train, X_val = X_train_full[train_idx], X_train_full[val_idx]
        y_train, y_val = y_train_full[train_idx], y_train_full[val_idx]

        grid_search = GridSearchCV(
            pipeline,
            param_grid,
            cv=3,
            scoring='f1_macro',
            n_jobs=-1
        )
        grid_search.fit(X_train, y_train)

        logger.info(f"Fold {fold} - Лучшие параметры: {grid_search.best_params_}")
        y_pred = grid_search.predict(X_val)

        print(f"Fold {fold} classification report:\n")
        report = classification_report(y_val, y_pred, digits=4)
        print(report)
        reports.append(report)

    logger.info("Оценка на тестовом наборе")
    y_pred_test = grid_search.best_estimator_.predict(X_test)
    print("Test set classification report:\n")
    test_report = classification_report(y_test, y_pred_test, digits=4)
    print(test_report)

    feature_names = ['Levenshtein', 'Token', 'AST', 'N-gram', 'AST_Structure'] + \
                    [f'emb_orig_{i}' for i in range(50)] + \
                    [f'emb_plag_{i}' for i in range(50)] + \
                    [f'emb_diff_{i}' for i in range(50)] + \
                    [f'tfidf_orig_{i}' for i in range(200)] + \
                    [f'tfidf_plag_{i}' for i in range(200)] + \
                    [f'tfidf_diff_{i}' for i in range(200)]
    logger.info("Запуск анализа признаков с SHAP...")
    analyze_features(grid_search.best_estimator_, X_test, feature_names)

    return grid_search.best_estimator_