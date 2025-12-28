nome = str(input('Qual é o seu Nome? '))
print('-=-' * 10)
if nome == 'Wendel' or nome == 'Rebeca':
    print('Seu nome é lindo!')

    print('-=-' * 10)

elif nome == 'Pedro' or nome == 'Maria' or nome == 'José':
    print('Seu nome é ridiculo.!')

    print('-=-' * 10)

elif nome in 'Ana Clara Sofia Laura':
    print('É um nome feminino muito popular!')

    print('-=-' * 10)

else:
    print ('Seu nome é normal.')