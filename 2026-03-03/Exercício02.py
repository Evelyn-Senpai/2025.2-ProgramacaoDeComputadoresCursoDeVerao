numero = int(input('Digite um número inteiro: '))
total = 0
if numero <= 1:
    print('Não é primo.')
else:
    for i in range(numero, 0, -1):
        if numero % i == 0:
            total += 1
    if total == 2:
        print('\033[32mÉ primo.\033[m')
    else:
        print('\033[31mNão é primo.\033[m')