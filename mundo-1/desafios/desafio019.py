nome1 = str(input('Digite o primeiro aluno: '))
nome2 = str(input('Digite o segundo aluno: '))
nome3 = str(input('Digite o terceiro aluno: '))
nome4 = str(input('Digite o quarto aluno: '))
from random import choice
lista = [nome1, nome2, nome3, nome4]
print('O escolhido foi: {}'.format(choice(lista)))