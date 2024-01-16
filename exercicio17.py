# Exercicio 017
# Faca um Programa para uma loja de tintas.
# O programa devera pedir o tamanho em metros quadrados da area a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuario as quantidades de tinta a serem compradas e os respectivos precos em 3 situacões:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o preco seja o menor.
#     Acrescente 10% de folga e sempre arredonde os valores para cima,
#     isto é, considere latas cheias.
import math
metros_quadrados = float(input("Informe a área a ser pintada: "))
metros_quadrados_mais_dez = metros_quadrados * 1.0 #mais dez por cento de folga


cobertura_litro = 6
rendimento_galao = cobertura_litro * 3.6
preco_galao = 25.0
rendimento_lata = cobertura_litro * 18
preco_lata = 80.0

somente_latas = math.ceil(metros_quadrados / rendimento_lata)
print(somente_latas)
somente_galoes = math.ceil(metros_quadrados / rendimento_galao)
print(somente_galoes)

latas = math.floor(metros_quadrados_mais_dez / rendimento_lata)
print(latas)

galoes = math.ceil(
    metros_quadrados_mais_dez / rendimento_galao
)
print(galoes)