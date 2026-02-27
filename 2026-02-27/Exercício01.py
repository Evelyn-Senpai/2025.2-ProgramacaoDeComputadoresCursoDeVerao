print('--- Calculadora de equação do segundo grau ---')
a = float(input('Informe o valor do coeficiente A: '))
b = float(input('Informe o valor do coeficiente B: '))
c = float(input('Informe o valor do coeficiente C: '))
delta = b**2 - 4*a*c
x1 = (-b + delta**0.5)/(2*a)
x2 = (-b - delta**0.5)/(2*a)
print(f'x1 é {x1}')
print(f'x2 é {x2}')
