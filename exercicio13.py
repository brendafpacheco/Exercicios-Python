# Exercicio 013
# Tendo como dado de entrada a altura (h) de uma pessoa, construa um 
# algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: 
# Para homens: (72.7h) - 58 Para mulheres: (62.1h) - 44.7

altura = float(input('Digite sua altura: '))
pesoHomens = (72.7 * altura) - 58
pesoMulheres = (62.1 * altura) - 44.7

print(f"Se for homem, o peso ideal para esta altura é {pesoHomens}. Se for mulher, o peso ideal para esta altura é {pesoMulheres}")
