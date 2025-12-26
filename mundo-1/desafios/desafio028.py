from random import randint
computador = randint(0, 5)
n = int(input('Digite um número entre 0 e 5: '))
if n == computador:
    print('Parabéns! Você venceu! Eu pensei no número {}.'.format(computador))
else:
    print('Você perdeu! Eu pensei no número {}.'.format(computador))
