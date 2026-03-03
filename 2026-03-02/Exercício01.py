print('--- Cálculo da média em disciplinas ---')
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
media = round((2*nota1+3*nota2)/5)
print(f'Sua média foi {media}, você está: ')
if media >= 60:
    print('Aprovado!')
elif media >= 20:
    print('Em Prova final!')
else:
    print('Reprovado!')
print('FIM') 