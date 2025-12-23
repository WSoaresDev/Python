n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
su = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma entre {} e {} é {}\n'.format(n1, n2, s), end=' ')
print('A subtração entre {} e {} é  {}\n'.format(n1, n2, su), end=' ')
print('A multiplicação entre {} e {} é {}\n'.format(n1, n2, m), end=' ')
print('A divisão entre {} e {} é {}\n'.format(n1, n2, d), end=' ')
print('A divisão inteira entre {} e {} é {}\n'.format(n1, n2, di), end=' ')
print('A exponenciação entre {} e {} é {}\n'.format(n1, n2, e))