def chessboard_slon(n, m, queries):
    # множества для слонов
    slons = set()  # храним координаты слонов
    results = []

    for t, x, y in queries:
        if t == 1:
            # поставить слона
            slons.add((x, y))
        elif t == 2:
            # убрать слона
            slons.remove((x, y))
        elif t == 3:
            d1 = x + y  # диагональ типа d1
            d2 = x - y  # диагональ типа d2
            min_moves = float('inf')  # будет использоваться для нахождения минимума
            
            for sx, sy in slons:
                if sx + sy == d1 or sx - sy == d2:
                    min_moves = min(min_moves, 1)  # слон может достигать в 1 ход
                else:
                    # поскольку слон может находиться только на одной диагонали
                    # проверим возможность достижения за 2 хода
                    if (sx + sy) % 2 == d1 % 2:  # обе диагонали четные или обе нечетные
                        min_moves = min(min_moves, 2)  # слон сможет достигнуть за 2 хода

            if min_moves == float('inf'):
                results.append(-1)  # если не нашли доступных слонов
            else:
                results.append(min_moves)

    return results

# чтение входных данных
n, m = map(int, input().split())
q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(q)]

# получение результатов
results = chessboard_slon(n, m, queries)

# вывод результатов для запросов 3 типа
for result in results:
    print(result)

