# Exercicio 009
# Faca um Programa que peca a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9).

grausF = float(input('Informe a temperatura em ºF'))

grausC =  (5 * (grausF-32) / 9)

print(f"A temperatura {grausF} em Farenheit é {grausC} em Celsius")