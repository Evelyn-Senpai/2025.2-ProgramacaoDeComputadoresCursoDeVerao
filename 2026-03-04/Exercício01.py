print('\033[34m--- Soma dos multiplos de 3 ou 5 ---\033[m')
soma = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        soma += i
print(f'\033[32mA soma dos multiplos de 3 ou 5 é {soma}\033[m')