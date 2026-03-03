print('--- Cálculo da média em disciplinas ---')
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
media = round((2*nota1+3*nota2)/5)
print(f'Sua média foi {media}, você está: ')
if media >= 60:
    print('Aprovado!')
elif media >= 20:
    print('Em Prova final!')
    nota_falta1 = 120 - media
    nota_falta2 = round((300-nota2*3)/2)
    nota_falta3 = round((300-nota1*2)/3)
    nota_falta = nota_falta1
    if nota_falta2 < nota_falta:
        nota_falta = nota_falta2
    if nota_falta3 < nota_falta:
        nota_falta = nota_falta3
    print(f'Você precisa de {nota_falta}')
    print('---------------------------------')
    nota_final = float(input('Nota final: '))
    media_opcao1 = round((media + nota_final)/2)
    media_opcao2 = round((2*nota_final + 3*nota2)/5)
    media_opcao3 = round((2*nota1 + 3*nota_final)/5)
    media_final = media_opcao1
    if media_opcao2 > media_final:
        media_final = media_opcao2
    if media_opcao3 > media_final:
        media_final = media_opcao3
    print(f'Sua média final é: {media_final}, você está: ')
    if  media_final >= 60:
        print(f'Aprovado!')
    else:
        print(f'Reprovado!')
else:
    print('Reprovado!')
print('FIM') 