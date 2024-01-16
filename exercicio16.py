# Exercicio 016
# Faca um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
# quadrados da area a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a 
# tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Informe ao usuario a quantidades de latas de tinta a serem compradas e o preco total.

import math
area = float(input('area a ser pintada em m²: '))
areaLata = 18 * 3 #54m²
qtdLatas = math.ceil(area / areaLata)
preco = qtdLatas * 80
print(f"Você precisa comprar {qtdLatas:.0f} lata(s), custando R${preco:.2f}")
