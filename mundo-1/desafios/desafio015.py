dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
preco_dias = dias * 60
preco_km = km * 0.15
total = preco_dias + preco_km
print('O total a pagar é R${:.2f}'.format(total))