print('--- Lista de pessoas ---')
pessoas = []
for i in range(5):
    nome = input('Nome: ')
    sexo = input('Sexo: ')
    pessoas.append(nome)
    pessoas.append(sexo)
mulheres = 0
homens = 0
for s in range(len(pessoas)):
    if s == 'F':
        mulheres += 1
    else:
        homens += 1
print(f'Tem {mulheres} mulheres')
print(f'Tem {homens} homens')