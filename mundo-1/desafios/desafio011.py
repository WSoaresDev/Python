largura = float(input('Largura da parede (m): '))
altura = float(input('Altura da parede (m): '))
area = largura * altura
litros = area / 2.5
print(f'A área da parede é {area:.2f} m².')
print(f'Quantidade de tinta necessária: {litros:.2f} litros.')
