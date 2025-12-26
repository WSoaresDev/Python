a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))

print('=============================================')

if a > b and a > c:
    print('O maior número é {}'.format(a))
elif b > a and b > c:
    print('O maior número é {}'.format(b))
else:
    print('O maior número é {}'.format(c))

if a < b and a < c:
    print('O menor número é {}'.format(a))
elif b < a and b < c:
    print('O menor número é {}'.format(b))
else:
    print('O menor número é {}'.format(c))
