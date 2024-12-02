graph = {
    0: [(1, 5), (2, -6)],
    1: [(2, 7),(3,4)],
    2: [(3,6)],
    3: []
}

# Инициализация переменных
d = {u: float('inf') for u in graph}  # расстояния до всех вершин
s = 0  # начальная вершина
d[s] = 0  # расстояние до начальной вершины
M0 = set()  # посещенные вершины
M1_prime = [s]  # основная очередь
M1_double_prime = []  # срочная очередь
M2 = set(u for u in graph if u != s)  # непосещенные вершины

while M1_prime or M1_double_prime:  # пока есть вершины для обработки
    if M1_double_prime:  # если срочная очередь не пуста
        u = M1_double_prime.pop()  # берем вершину из срочной очереди
    else:
        u = M1_prime.pop(0)  # берем вершину из основной очереди

    for v, weight in graph[u]:  # рассматриваем все соседние вершины
        if v in M2:  # если v в M2
            d[v] = d[u] + weight  # релаксация
            M1_prime.append(v)  # добавляем v в основную очередь
            M2.remove(v)  # удаляем v из M2
        if v in M1_prime or v in M1_double_prime:  # если v в M1
            new_distance = d[u] + weight  # вычисляем новое расстояние
            if new_distance < d[v]:  # если новое расстояние меньше
                d[v] = new_distance  # обновляем расстояние
        if v in M0:  # если v в M0
            new_distance = d[u] + weight  # вычисляем новое расстояние
            if new_distance < d[v]:  # если новое расстояние меньше
                d[v] = new_distance  # обновляем расстояние
                M1_double_prime.append(v)  # помещаем в срочную очередь

    M0.add(u)  # добавляем u в множество M0

for ver, distance in d.items():
    print(f"Расстояние до вершины {ver}: {distance}")