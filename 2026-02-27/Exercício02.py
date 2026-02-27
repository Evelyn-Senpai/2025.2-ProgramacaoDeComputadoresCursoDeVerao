print('--- Calculadora de juros com aporte ---')
c = float(input('Informe o capital inicial: '))
d = float(input('Informe o aporte mensal: '))
i = float(input('Informe o rendimento mensal em %: '))
n = float(input('Informe o número de meses: '))
p = 1+i/100
saldo = c*p**n + d*(p**n-p)/(i/100)
print(f'O saldo final é {saldo}')
