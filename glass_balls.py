import random
import math


# СТЕКЛЯННЫЕ ШАРЫ
# Имеется k одинаковых стеклянных шариков. Их кидают с некоторых этажей n этажного дома (n < 10^6).
# Требуется за наименьшее число бросаний X определить самый нижний этаж, при бросании с которого шарики
# разбиваются (или убедиться, что таких этажей в доме нет).
# Уточнение: количество шариков (k) <= 10, этажей (n) <= 10^6

def how_to_throw(n, k):
    if k == 1:
        return 1
    elif k > math.ceil(math.log2(n)):
        return math.ceil(n / 2.0)
    else:
        comb_sum = 0
        for i in range(0, k):
            comb_sum += count_combinations(max_throws() - 1, i)
        return comb_sum


def max_throws():
    # была найдена формула, где макс число бросков высчитывается след образом:
    # min {нат n| сочетания из m по i, где i от 0 до k включительно}
    m = 1
    comb_sum = 0
    while comb_sum < n:
        for i in range(0, k + 1):
            comb_sum += count_combinations(m, i)
        if comb_sum < n:
            comb_sum = 0
            m += 1
    return m


def is_broken(floor):
    return not floor < break_floor


def count_combinations(n, k):
    """
      A fast way to calculate binomial coefficients by Andrew Dalke (contrib).
      """
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0


if __name__ == '__main__':
    k = int(input("Введите кол-во стеклянных шаров k (k <= 10): "))
    n = int(input("Введите кол-во этажей n (n <= 10^6): "))
    print("Генерируем номер этажа, с которого шар должен разбиться...")
    break_floor = random.randint(1, int(n * 1.5))
    max_thr = max_throws()
    print("Найти нужный этаж можно максимум за " + str(max_thr) + " бросков")

    floors = []
    n_copy = n
    x = 1
    throw_floor = -1
    is_breakable = True
    d = 1
    while n > 1:
        throw_floor = how_to_throw(n, k)
        throwing = x - 1 + throw_floor
        if not floors.__contains__(throwing):
            floors.append(throwing)
            print("Шаг " + str(d) + ". Бросаем шар с " + str(throwing) + " этажа.")
            if is_broken(throwing):
                print("Шар разбился. (Осталось шаров: " + str(k - 1) + ")")
                n = throw_floor
                k -= 1
            else:
                print("Шар остался цел.")
                x = x + throw_floor
                n = n - throw_floor
                if x - 1 + throw_floor == n_copy:
                    is_breakable = False
                    n += 1
            d += 1
        else:
            n = -1
            is_breakable = True
    if is_breakable:
        print("Шары разбиваются с " + str(x) + " этажа")
    else:
        print("Шары не разбиваются с этой высоты")
    print("(Generated value: " + str(break_floor) + ")")
