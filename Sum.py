def sum(n):
    a = 5  # Перший член прогресії
    d = 5  # Різниця прогресії
    sum_n = (n / 2) * (2 * a + (n - 1) * d)
    return sum_n

# Приклад виклику функції
n = 10  # Наприклад, обчислити суму перших 10 членів
result = sum(n)
print(f"Сума перших {n} членів прогресії: {result}")
