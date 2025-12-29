nota1 = int(input('Primeira nota: '))
nota2 = int(input('Segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('Média {:.1f}. REPROVADO'.format(media))
elif media >= 5.0 and media < 7.0:
    print('Média {:.1f}. RECUPERAÇÃO'.format(media))
else:
    print('Média {:.1f}. APROVADO'.format(media))