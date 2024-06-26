'''В терминологии сетей TCP/IP маска сети – это двоичное число, меньшее 232; в маске сначала (в старших разрядах) стоят единицы, а затем с некоторого места нули. Маска определяет, какая часть IP-адреса узла сети относится к адресу сети, а какая – к адресу самого узла в этой сети. Обычно маска записывается по тем же правилам, что и IP-адрес – в виде четырёх байт, причём каждый байт записывается в виде десятичного числа. Адрес сети получается в результате применения поразрядной конъюнкции к заданному IP-адресу узла и маске.
Например, если IP-адрес узла равен 131.32.255.131, а маска равна 255.255.240.0, то адрес сети равен 131.32.240.0.
Для узла с IP-адресом 220.128.112.142 адрес сети равен 220.128.96.0. Чему равен третий слева байт маски? Ответ запишите в виде десятичного числа.
'''
from ipaddress import *

for m in range(33):
    net = ip_network(f'220.128.112.142/{m}', 0)
    if '220.128.96.0' in str(net):
        print(net.netmask)
