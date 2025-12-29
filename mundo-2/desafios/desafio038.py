'''Programa que lê dois números e mostra uma mensagem indicando qual é o maior, ou se são iguais.'''

n1 = int(input('Digite o PRIMEIRO número: '))
n2 = int(input('Digite o SEGUNDO número: '))
igual = n1 == n2
maior = n1 > n2
menor = n1 < n2
if igual:
    print('Os dois números são iguais.')
elif maior:
    print('O número {} é maior.'.format(n1))
else:
    print('O número {} é maior.'.format(n2))