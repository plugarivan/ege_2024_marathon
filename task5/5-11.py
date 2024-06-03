'''(А. Минак) На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.
1. Строится запись числа N в восьмеричной системе счисления.
2. Далее эта запись обрабатывается по следующему правилу:
  а) если сумма цифр в восьмеричной записи числа чётная, то к этой записи дописываются слева и справа первая цифра его восьмеричной записи;
  б) если сумма цифр в восьмеричной записи числа нечётная, то к этой записи дописывается справа последняя цифра его восьмеричной записи.
Полученная таким образом запись является восьмеричной записью искомого числа R. Например, для исходного числа 17 = 218 результатом является число 2118 = 137, а для исходного числа 25 = 318 это число 33138 = 1739.
Укажите максимальное число N, после обработки которого с помощью этого алгоритма получается число R, меньшее 1100.
'''
for n in range(1, 1000):
    s = oct(n)[2:]
    if sum(map(int, s)) % 2 == 0: s = s[0] + s + s[0]
    else: s += s[-1]
    if int(s, 8) < 1100:
        print(n)
