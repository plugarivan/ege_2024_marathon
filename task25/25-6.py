'''Пусть D(N) – шестой по величине (считая с наибольшего) нетривиальный нечётный делитель натурального числа N (нетривиальными считаются все делители, кроме 1 и самого числа). Например, D(315) = 15. Если у числа N меньше 6 различных нетривиальных нечётных делителей, то принимаем D(N) = 0. Найдите 5 наименьших натуральных чисел, превышающих 200 000 000, для которых D(N) > 0. В ответе запишите для каждого найденного N сначала значение D(N), а затем общее количество нетривиальных нечётных делителей (в порядке возрастания соответствующих чисел N).'''
i, k = 200_000_001, 0
while k != 5:
    divs = set()
    for d in range(2, round(i ** 0.5) + 1):
        if i % d == 0:
            divs.add(d)
            divs.add(i // d)
    divs = sorted((x for x in divs if x % 2), reverse=True)
    if len(divs) >= 6:
        k += 1
        print(divs[5], len(divs))
    i += 1
