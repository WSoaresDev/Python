p = float(input('Qual é o preço do produto? R$'))
d = p - (p * 5 / 100)
print('O preço do produto com 5% de desconto é R${:.2f}'.format(d))