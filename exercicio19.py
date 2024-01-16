# Exercicio 019
# Faca um Programa que peca dois números e imprima o maior deles.

num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))

if (num1 > num2):
    print(f"{num1} é o maior")
elif (num1 == num2):
    print("Os valores inseridos são iguais.")
else:
    print(f"{num2} é o maior número")