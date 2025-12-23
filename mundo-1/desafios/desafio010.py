d = float(input('Quanto dinheiro você tem na carteira? R$'))
d = d / 5.15
print('Com R${} você pode comprar US${}'.format(d * 5.15, d))