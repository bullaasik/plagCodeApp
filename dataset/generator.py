import random
import re
from pathlib import Path
import logging
from code_mutations.for_to_while import for_to_while_mutation
from code_mutations.if_to_ternary import if_to_ternary_mutation
from code_mutations.obfuscator import custom_obfuscate_code
from code_mutations.function_splitter import split_function_mutation
from code_mutations.syntax_checker import is_valid_code
from similarity_metrics.code2vec import train_word2vec

logger = logging.getLogger(__name__)

def generate_dataset(num_pairs=500):
    templates = [
        """def factorial(n):
    if n == 0: return 1
    return n * factorial(n-1)
print(factorial(5))""",
        """def binary_search(arr, x):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x: low = mid + 1
        elif arr[mid] > x: high = mid - 1
        else: return mid
    return -1
arr = [1, 3, 5, 7, 9]
print(binary_search(arr, 5))""",
        """def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
print(gcd(60, 48))""",
        """def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print(arr)""",
        """def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
print(fibonacci(10))""",
        """def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr, 0, len(arr)-1)
print(arr)""",
        """def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][capacity]
print(knapsack([60, 100, 120], [10, 20, 30], 50))"""
    ]

    non_plag_templates = [
        """def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False
    return True
print(is_prime(17))""",
        """def reverse_string(s):
    return ''.join(reversed(s))
print(reverse_string("hello"))""",
        """def matrix_multiply(a, b):
    result = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result
a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]
print(matrix_multiply(a, b))""",
        """def dijkstra(graph, start):
    dist = {v: float('inf') for v in graph}
    dist[start] = 0
    visited = set()
    while len(visited) < len(graph):
        min_dist = float('inf')
        min_vertex = None
        for v in graph:
            if v not in visited and dist[v] < min_dist:
                min_dist = dist[v]
                min_vertex = v
        if min_vertex is None: break
        visited.add(min_vertex)
        for neighbor, weight in graph[min_vertex].items():
            if dist[min_vertex] + weight < dist[neighbor]:
                dist[neighbor] = dist[min_vertex] + weight
    return dist
graph = {'A': {'B': 1, 'C': 4}, 'B': {'A': 1, 'C': 2, 'D': 5}, 'C': {'A': 4, 'B': 2, 'D': 1}, 'D': {'B': 5, 'C': 1}}
print(dijkstra(graph, 'A'))"""
    ]

    alt_templates = {
        "factorial": """def factorial_iter(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial_iter(5))""",
        "binary_search": """def binary_search_iter(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x: return mid
        elif arr[mid] < x: left = mid + 1
        else: right = mid - 1
    return -1
arr = [1, 3, 5, 7, 9]
print(binary_search_iter(arr, 5))""",
        "gcd": """def gcd_iter(a, b):
    while b:
        temp = b
        b = a % b
        a = temp
    return a
print(gcd_iter(60, 48))""",
        "bubble_sort": """def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
arr = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(arr)
print(arr)""",
        "fibonacci": """def fibonacci_iter(n):
    if n <= 1: return n
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]
print(fibonacci_iter(10))""",
        "quick_sort": """def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
arr = [10, 7, 8, 9, 1, 5]
merge_sort(arr)
print(arr)""",
        "knapsack": """def knapsack_iter(values, weights, capacity):
    n = len(values)
    dp = [0 for _ in range(capacity + 1)]
    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[capacity]
print(knapsack_iter([60, 100, 120], [10, 20, 30], 50))"""
    }

    mutations = [
        lambda c: re.sub(r"\b(factorial|binary_search|gcd|bubble_sort|fibonacci|quick_sort|knapsack)\b",
                         lambda m: m.group(0) + str(random.randint(1, 5)), c),
        lambda c: re.sub(r"print\((\w+)\((.*?)\)\)",
                         lambda m: f"print({m.group(1)}{random.randint(1, 5)}({m.group(2)}))", c),
        for_to_while_mutation,
        lambda c: c.replace("if", "if" + " " * random.randint(1, 3)),
        lambda c: c + "\n" + "\n".join(random.sample(["import math", "import sys", "import os"], random.randint(1, 2))),
        lambda c: re.sub(r"\b(n|arr|x|low|high|mid|a|b|i|j|values|weights|capacity)\b",
                         lambda m: random.choice(["v" + str(random.randint(1, 10)), m.group(0) + "_"]), c),
        lambda c: c + "\n# Comment " + str(random.randint(1, 100)),
        custom_obfuscate_code,
        if_to_ternary_mutation,
        split_function_mutation
    ]

    orig_dir = Path("dataset/original")
    plag_dir = Path("dataset/plagiarized")
    orig_dir.mkdir(parents=True, exist_ok=True)
    plag_dir.mkdir(parents=True, exist_ok=True)

    all_codes = [] 

    for i in range(num_pairs):
        if i < num_pairs // 2:
            template = random.choice(templates).strip()
            orig_file = orig_dir / f"code_{i+1}_orig.py"
            plag_file = plag_dir / f"code_{i+1}_plag.py"
            
            with open(orig_file, "w", encoding="utf-8") as f:
                f.write(template)
            all_codes.append(template)
            
            mutated = template
            for _ in range(random.randint(3, 6)):
                mut_func = random.choice(mutations)
                new_mutated = mut_func(mutated)
                if new_mutated and is_valid_code(new_mutated):
                    mutated = new_mutated
            
            if is_valid_code(mutated):
                with open(plag_file, "w", encoding="utf-8") as f:
                    f.write(mutated)
                all_codes.append(mutated)
        else: 
            template = random.choice(templates).strip()
            template_key = re.search(r"def (factorial|binary_search|gcd|bubble_sort|fibonacci|quick_sort|knapsack)", template)
            
            if template_key and template_key.group(1) in alt_templates:
                non_plag_template = alt_templates[template_key.group(1)].strip()
            else:
                non_plag_template = random.choice(non_plag_templates).strip()
            
            mutated = non_plag_template
            for _ in range(random.randint(5, 8)):
                mut_func = random.choice(mutations)
                new_mutated = mut_func(mutated)
                if new_mutated and is_valid_code(new_mutated):
                    mutated = new_mutated
            
            orig_file = orig_dir / f"code_{i+1}_orig.py"
            plag_file = plag_dir / f"code_{i+1}_plag.py"
            
            with open(orig_file, "w", encoding="utf-8") as f:
                f.write(template)
            all_codes.append(template)
            
            if is_valid_code(mutated):
                with open(plag_file, "w", encoding="utf-8") as f:
                    f.write(mutated)
                all_codes.append(mutated)

    # Обучение Word2Vec на всем датасете
    logger.info("Обучение Word2Vec на %d примерах кода...", len(all_codes))
    train_word2vec(all_codes)
    
    logger.info(f"{num_pairs} пар файлов успешно сгенерировано. Word2Vec обучен.")