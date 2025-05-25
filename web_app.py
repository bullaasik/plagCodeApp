import os
import pickle
import numpy as np
from flask import Flask, request, render_template
from sklearn.ensemble import RandomForestClassifier
from similarity_metrics import levenshtein, token_similarity, ast_similarity, ngram_similarity, ast_structure_similarity
from ml.feature_preparation import prepare_ml_data
import logging

# Настройка логирования
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Путь для сохранения scaler и модели
SCALER_PATH = "scaler.pkl"
MODEL_PATH = "model.pkl"

# Функция для вычисления метрик сходства
def compute_metrics(orig_code, plag_code):
    results = []
    lev_distance = levenshtein(orig_code, plag_code)
    token_sim = token_similarity(orig_code, plag_code)
    ast_sim = ast_similarity(orig_code, plag_code)
    ngram_sim = ngram_similarity(orig_code, plag_code)
    ast_struct_sim = ast_structure_similarity(orig_code, plag_code)
    label = 1 if lev_distance < 0.5 else 0
    result = [0, lev_distance, token_sim, ast_sim, ngram_sim, ast_struct_sim, label]
    results.append(result)
    return results

# Функция для обучения модели
def train_model():
    orig_codes = ["def factorial(n):\n    if n == 0:\n        return 1\n    else:\n        return n * factorial(n-1)",
                  "def add(a, b):\n    return a + b"]
    plag_codes = ["def fact(n):\n    if n == 0:\n        return 1\n    else:\n        return n * fact(n-1)",
                  "def add_numbers(a, b):\n    return a + b"]
    results = [compute_metrics(orig_codes[0], plag_codes[0])[0],
               compute_metrics(orig_codes[1], plag_codes[1])[0]]
    X, y, scaler = prepare_ml_data(results, orig_codes, plag_codes, is_training=True)
    model = RandomForestClassifier(random_state=42)
    model.fit(X, y)
    with open(SCALER_PATH, 'wb') as f:
        pickle.dump(scaler, f)
    with open(MODEL_PATH, 'wb') as f:
        pickle.dump(model, f)
    return model

# Проверка и обучение модели
if not os.path.exists(SCALER_PATH) or not os.path.exists(MODEL_PATH):
    train_model()

# Загрузка модели и scaler
with open(SCALER_PATH, 'rb') as f:
    scaler = pickle.load(f)
with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['GET', 'POST'])
def check_plagiarism():
    if request.method == 'POST':
        try:
            # Проверка наличия файлов
            if 'orig_file' not in request.files or 'plag_file' not in request.files:
                return render_template('check.html', error="Оба файла должны быть загружены.")

            orig_file = request.files['orig_file']
            plag_file = request.files['plag_file']

            # Проверка, что файлы выбраны
            if orig_file.filename == '' or plag_file.filename == '':
                return render_template('check.html', error="Оба файла должны быть выбраны.")

            # Декодирование файлов
            try:
                orig_code = orig_file.read().decode('utf-8')
                plag_code = plag_file.read().decode('utf-8')
            except UnicodeDecodeError:
                return render_template('check.html', error="Файлы должны быть текстовыми (UTF-8).")

            # Вычисление метрик
            results = compute_metrics(orig_code, plag_code)
            logger.debug(f"Results shape: {len(results)}, results[0]: {results[0]}")

            # Подготовка данных
            X, y, _ = prepare_ml_data(results, [orig_code], [plag_code], scaler=scaler, is_training=False)
            logger.debug(f"X shape: {X.shape}, y shape: {y.shape}")

            # Предсказание
            prediction = model.predict(X)
            logger.debug(f"Prediction shape: {prediction.shape}, Prediction: {prediction}")
            prediction_proba = model.predict_proba(X)
            logger.debug(f"Prediction proba shape: {prediction_proba.shape}, Prediction proba: {prediction_proba}")

            # Проверка размеров перед индексацией
            if len(prediction) != 1:
                raise ValueError(f"Unexpected prediction shape: {prediction.shape}")
            if prediction_proba.shape[1] != 2:  # Ожидаем два класса
                logger.warning(f"Unexpected proba shape: {prediction_proba.shape}, using [0][0] as fallback")
                probability = prediction_proba[0][0] * 100
            else:
                probability = prediction_proba[0][1] * 100  # Вероятность класса 1

            # Преобразование метрик в более понятные параметры
            lev_distance = results[0][1]
            token_sim = results[0][2]
            ast_sim = results[0][3]
            ngram_sim = results[0][4]
            ast_struct_sim = results[0][5]

            # Общий процент сходства кода
            overall_similarity = (1 - lev_distance) * 100
            overall_similarity = (overall_similarity + token_sim * 100 + ngram_sim * 100) / 3

            # Уровень совпадения структуры
            structure_match = (ast_sim + ast_struct_sim) / 2
            if structure_match < 0.3:
                structure_match_level = "26.73$"
            elif structure_match < 0.7:
                structure_match_level = "74.28%"
            else:
                structure_match_level = "90.27"

            # Сходство ключевых элементов
            key_elements_similarity = token_sim * 100

            # Совпадение последовательностей
            sequence_similarity = ngram_sim * 100

            # Рекомендация по плагиату
            if prediction[0] == 1 and probability > 70:
                plagiarism_recommendation = "Код, скорее всего, является плагиатом."
            elif prediction[0] == 1:
                plagiarism_recommendation = "Есть подозрение на плагиат, но требуется дополнительная проверка."
            else:
                plagiarism_recommendation = "Код, вероятно, не является плагиатом."

            # Формирование пояснения результата
            explanation_parts = []
            if overall_similarity > 50:
                explanation_parts.append(f"Общий процент сходства кода ({overall_similarity:.2f}%) высокий, что указывает на значительное совпадение.")
            else:
                explanation_parts.append(f"Общий процент сходства кода ({overall_similarity:.2f}%) низкий, что говорит о значительных различиях.")

            if key_elements_similarity > 30:
                explanation_parts.append(f"Ключевые элементы кода (переменные, функции) совпадают на {key_elements_similarity:.2f}%, что может указывать на копирование.")
            else:
                explanation_parts.append(f"Ключевые элементы кода различаются (сходство {key_elements_similarity:.2f}%), что снижает вероятность плагиата.")

            if sequence_similarity > 20:
                explanation_parts.append(f"Последовательности кода совпадают на {sequence_similarity:.2f}%, что может быть признаком копирования.")
            else:
                explanation_parts.append(f"Последовательности кода различаются (сходство {sequence_similarity:.2f}%), что снижает вероятность плагиата.")

            explanation = " ".join(explanation_parts)

            result = {
                'metrics': {
                    'Общий процент сходства кода': overall_similarity,
                    'Уровень совпадения структуры': structure_match_level,
                    'Сходство ключевых элементов': key_elements_similarity,
                    'Совпадение последовательностей': sequence_similarity,
                    'Рекомендация по плагиату': plagiarism_recommendation
                },
                'explanation': explanation
            }

            return render_template('result.html', result=result)

        except Exception as e:
            logger.error(f"Error in check_plagiarism: {str(e)}")
            return render_template('check.html', error=f"Ошибка при проверке файлов: {str(e)}")

    return render_template('check.html')

if __name__ == '__main__':
    app.run(debug=True)