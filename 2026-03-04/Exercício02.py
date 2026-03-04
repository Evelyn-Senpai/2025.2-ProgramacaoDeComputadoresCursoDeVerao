print('--- Sequência de Collatz ---')
n = int(input('Informe um número: '))
total = 1
print('A sequência é: ')
while n != 1:
    print(f'\033[32m{n} -> ', end = '')
    if n % 2 == 0:
        n //= 2
        total += 1
    else:
        n = n * 3 + 1
        total += 1
print(f'1\033[m')
print(f'O tamanho da sequência é \033[33m{total}\033[m')
