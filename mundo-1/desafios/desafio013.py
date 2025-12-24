s = float(input('Qual é o salário do funcionário? R$'))
a = s + (s * 15 / 100)
print('O salário do funcionário era R${:.2f}, mas com um aumento de 15% é R${:.2f}'.format(s, a))