# Exercicio 027
# Faca um Programa que leia três números e mostre-os em ordem decrescente.

numero1 = float(input("Número 1:"))
numero2 = float(input("Número 2:"))
numero3 = float(input("Número 3:"))

if numero1 > numero2 > numero3:
    print(numero1, numero2, numero3)
elif numero1 > numero3 > numero2:
    print(numero1, numero3, numero2)
elif numero2 > numero1 > numero3:
    print(numero2, numero1, numero3)
elif numero2 > numero3 > numero1:
    print(numero2, numero3, numero1)
elif numero3 > numero1 > numero2:
    print(numero3, numero1, numero2)
else:
    print(numero3, numero2, numero1)