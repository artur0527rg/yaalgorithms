"""
ПРИНЦИП РАБОТЫ
    Подробное описание алгоритма - https://ru.wikipedia.org/wiki/Задача_разбиения_множества_чисел

ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ
    Доказательство алгоритма - https://ru.wikipedia.org/wiki/Задача_разбиения_множества_чисел

ВРЕМЕННАЯ СЛОЖНОСТЬ
    O(n*s), где n - количество элементов массива, s - размер суммы.

ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ
    O(s), где s - размер суммы.

УСПЕШНАЯ ПОСЫЛКА
    67425708
"""


def is_same_amounts(n, points):
    sum_points = sum(points)
    if sum_points % 2 != 0:
        return False

    half_sum = sum_points // 2
    dp = [True] + [False] * half_sum
    for i in range(1, n + 1):
        for j in range(half_sum, points[i - 1] - 1, -1):
            dp[j] = dp[j - points[i - 1]] or dp[j]
            if j == half_sum and dp[j]:
                return True
    return dp[-1]


print(is_same_amounts(int(input()), list(map(int, input().split()))))
