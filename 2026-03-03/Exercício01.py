from random import randint
inferior = 1
superior = 100
sorteado = randint(inferior, superior)
while True:
    chute = int(input(f'Digite um número entre {inferior} e {superior}: '))
    if chute == sorteado:
        print('Parabéns!')
        break
    elif chute > 100 or chute < 1:
        print('O chute precisa ser no minímo 1 e no máximo 100.')
    elif chute < sorteado:
        inferior = chute
        print('Tente outra vez: ')
    else:
        superior = chute
        print('Tente outra vez: ')
