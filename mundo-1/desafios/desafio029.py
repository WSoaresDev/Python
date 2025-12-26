velocidade = float(input("Qual é a velocidade do carro? "))

limite = 80
valor_por_km = 7.0

if velocidade > limite:
    excesso = velocidade - limite
    multa = excesso * valor_por_km
    print(f"Você foi MULTADO! Ultrapassou o limite em {excesso:.1f} km/h.")
    print(f"O valor da multa é R${multa:.2f}")
else:
    print("Dentro do limite. Tenha um bom dia!")
