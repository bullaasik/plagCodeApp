import os
import random
import numpy as np
import pandas as pd
import logging
from dataset.generator import generate_dataset
from similarity_metrics.text_metrics import levenshtein_sim, token_based_sim, ngram_sim
from similarity_metrics.ast_metrics import ast_sim, ast_structure_sim
from ml.feature_preparation import prepare_ml_data
from ml.model_training import train_model

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

random.seed(42)
np.random.seed(42)

def run_experiment():
    NUM_PAIRS = 1000
    generate_dataset(NUM_PAIRS)

    results = []
    orig_codes = []
    plag_codes = []

    for i in range(NUM_PAIRS):
        orig_path = f"dataset/original/code_{i+1}_orig.py"
        plag_path = f"dataset/plagiarized/code_{i+1}_plag.py"

        try:
            with open(orig_path, encoding="utf-8") as f1, open(plag_path, encoding="utf-8") as f2:
                code1 = f1.read()
                code2 = f2.read()

                label = 1 if i < NUM_PAIRS // 2 else 0

                result = (
                    i + 1,
                    levenshtein_sim(code1, code2),
                    token_based_sim(code1, code2),
                    ast_sim(code1, code2),
                    ngram_sim(code1, code2, n=3),
                    ast_structure_sim(code1, code2),
                    label
                )
                results.append(result)
                orig_codes.append(code1)
                plag_codes.append(code2)
        except Exception as e:
            logger.error(f"Ошибка при обработке пары {i+1}: {e}")
            continue

    df = pd.DataFrame(results, columns=["Pair", "Levenshtein", "Token", "AST", "N-gram", "AST_Structure", "Label"])
    print("\nПервые 5 строк датафрейма результатов:")
    print(df.head())

    X, y = prepare_ml_data(results, orig_codes, plag_codes)
    print(f"\nПодготовлено признаков: {X.shape[1]}, объектов: {X.shape[0]}")

    model = train_model(X, y)
    print("Обучение завершено.")

if __name__ == "__main__":
    print("Запуск эксперимента...")
    run_experiment()
    print("Эксперимент завершён.")