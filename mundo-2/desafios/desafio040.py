'''Programa que lê as duas notas de um aluno, calcula e mostra a sua média. No final, informa se o aluno está APROVADO, em RECUPERAÇÃO ou REPROVADO, de acordo com a média atingida: 
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO'''

nota1 = int(input('Primeira nota: '))
nota2 = int(input('Segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('Média {:.1f}. REPROVADO'.format(media))
elif media >= 5.0 and media < 7.0:
    print('Média {:.1f}. RECUPERAÇÃO'.format(media))
else:
    print('Média {:.1f}. APROVADO'.format(media))