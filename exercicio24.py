# Exercicio 024
# Faca um Programa que leia três números e mostre o maior deles.

numero1 = float(input("Número 1:"))
numero2 = float(input("Número 2:"))
numero3 = float(input("Número 3:"))

if numero1 > numero2 and numero1 > numero3:
    print(f"{numero1} foi o maior numero digitado.")
elif numero2 > numero1 and numero2 > numero3:
    print(f"{numero2} foi o maior numero digitado.")
else:
    print(f"{numero3} foi o maior numero digitado.")