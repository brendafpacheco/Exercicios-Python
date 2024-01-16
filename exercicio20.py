# Exercicio 020
# Faca um Programa que peca um valor e mostre na tela se o valor é positivo ou negativo.

num1 = int(input("Digite um número: "))

if (num1 > 0):
    print(f"O número {num1} é positivo.")
elif (num1 == 0):
    print(f"O número {num1} é neutro.")
else:
    print(f"O número {num1} é negativo.")