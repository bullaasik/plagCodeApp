import os
import pickle
import numpy as np
from flask import Flask, request, render_template, redirect, url_for, flash
from sklearn.ensemble import RandomForestClassifier
from similarity_metrics import levenshtein, token_similarity, ast_similarity, ngram_similarity, ast_structure_similarity
from ml.feature_preparation import prepare_ml_data
import logging

# Настройка логирования
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Необходимо для flash-сообщений

# Пути для сохранения scaler и модели
SCALER_PATH = "scaler.pkl"
MODEL_PATH = "model.pkl"

def compute_metrics(orig_code, plag_code):
    """Вычисление всех метрик сходства между двумя фрагментами кода"""
    results = []
    lev_distance = levenshtein(orig_code, plag_code)
    token_sim = token_similarity(orig_code, plag_code)
    ast_sim = ast_similarity(orig_code, plag_code)
    ngram_sim = ngram_similarity(orig_code, plag_code)
    ast_struct_sim = ast_structure_similarity(orig_code, plag_code)
    
    # Комбинированная метрика (статическая часть)
    static_score = 0.3*(1 - lev_distance) + 0.2*token_sim + 0.25*ast_sim + 0.15*ngram_sim + 0.1*ast_struct_sim
    label = 1 if static_score > 0.7 else 0
    
    result = [static_score, lev_distance, token_sim, ast_sim, ngram_sim, ast_struct_sim, label]
    results.append(result)
    return results

def train_model():
    """Обучение модели с использованием сгенерированного датасета"""
    from dataset.generator import generate_dataset
    generate_dataset(1000)
    
    orig_dir = "dataset/original"
    plag_dir = "dataset/plagiarized"
    
    results = []
    orig_codes = []
    plag_codes = []
    
    for filename in os.listdir(orig_dir):
        if filename.endswith(".py"):
            orig_path = os.path.join(orig_dir, filename)
            plag_path = os.path.join(plag_dir, filename.replace("_orig", "_plag"))
            
            with open(orig_path, 'r', encoding='utf-8') as f:
                orig_code = f.read()
            with open(plag_path, 'r', encoding='utf-8') as f:
                plag_code = f.read()
                
            orig_codes.append(orig_code)
            plag_codes.append(plag_code)
            results.extend(compute_metrics(orig_code, plag_code))
    
    X, y, scaler = prepare_ml_data(results, orig_codes, plag_codes, is_training=True)
    
    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=20,
        min_samples_split=5,
        random_state=42,
        class_weight={0: 1.5, 1: 1}
    )
    model.fit(X, y)
    
    with open(SCALER_PATH, 'wb') as f:
        pickle.dump(scaler, f)
    with open(MODEL_PATH, 'wb') as f:
        pickle.dump(model, f)
    
    return model

# Инициализация модели при запуске приложения
if not os.path.exists(SCALER_PATH) or not os.path.exists(MODEL_PATH):
    logger.info("Модель не найдена, начинаем обучение...")
    train_model()

# Загрузка модели и scaler
with open(SCALER_PATH, 'rb') as f:
    scaler = pickle.load(f)
with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def index():
    """Главная страница"""
    return render_template('index.html')

@app.route('/check', methods=['GET', 'POST'])
def check_plagiarism():
    """Обработка проверки на плагиат"""
    if request.method == 'POST':
        try:
            # Проверка наличия файлов
            if 'orig_file' not in request.files or 'plag_file' not in request.files:
                flash('Оба файла должны быть загружены', 'error')
                return redirect(url_for('check_plagiarism'))
            
            orig_file = request.files['orig_file']
            plag_file = request.files['plag_file']
            
            # Проверка, что файлы выбраны
            if orig_file.filename == '' or plag_file.filename == '':
                flash('Выберите файлы для сравнения', 'error')
                return redirect(url_for('check_plagiarism'))
            
            # Чтение и декодирование файлов
            try:
                orig_code = orig_file.read().decode('utf-8')
                plag_code = plag_file.read().decode('utf-8')
            except UnicodeDecodeError:
                flash('Файлы должны быть текстовыми (UTF-8)', 'error')
                return redirect(url_for('check_plagiarism'))
            
            # Вычисление метрик
            results = compute_metrics(orig_code, plag_code)
            logger.debug(f"Вычисленные метрики: {results[0]}")
            
            # Подготовка данных для ML модели
            X, _, _ = prepare_ml_data(results, [orig_code], [plag_code], scaler=scaler)
            
            # Предсказание модели
            ml_prob = model.predict_proba(X)[0][1]
            static_score = results[0][0]
            
            # Комбинированный результат (гибридный подход)
            final_score = 0.6*ml_prob + 0.4*static_score
            
            # Формирование детализированного результата
            result = {
                'static_metrics': {
                    'levenshtein': results[0][1],
                    'token_similarity': results[0][2],
                    'ast_similarity': results[0][3],
                    'ngram_similarity': results[0][4],
                    'ast_structure_similarity': results[0][5],
                    'static_score': static_score * 100,
                },
                'ml_score': ml_prob * 100,
                'final_score': final_score * 100,
                'is_plagiarism': final_score > 0.65,
                'explanation': get_explanation(final_score, results[0])
            }
            
            return render_template('result.html', result=result)
        
        except Exception as e:
            logger.error(f"Ошибка при проверке: {str(e)}")
            flash(f'Произошла ошибка: {str(e)}', 'error')
            return redirect(url_for('check_plagiarism'))
    
    return render_template('check.html')

def get_explanation(final_score, metrics):
    """Генерация пояснительного текста на основе результатов"""
    explanations = []
    
    if final_score > 0.75:
        explanations.append("Высокий уровень сходства кода.")
    elif final_score > 0.5:
        explanations.append("Умеренный уровень сходства кода.")
    else:
        explanations.append("Низкий уровень сходства кода.")
    
    if metrics[1] < 0.3:
        explanations.append("Код имеет значительное текстовое сходство.")
    elif metrics[1] < 0.6:
        explanations.append("Код имеет умеренное текстовое сходство.")
    else:
        explanations.append("Код имеет низкое текстовое сходство.")
    
    if metrics[3] > 0.7: 
        explanations.append("Структура кода очень похожа.")
    elif metrics[3] > 0.4:
        explanations.append("Структура кода имеет некоторое сходство.")
    else:
        explanations.append("Структура кода отличается.")
    
    return " ".join(explanations)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)