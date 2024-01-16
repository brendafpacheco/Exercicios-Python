# Exercicio 005
# Faca um Programa que converta metros para centímetros.

def conversor(metro):
    centimetros = metro*100
    print(f"{metro} metros correspondem a {centimetros} centímetros")

conversor(5)

metros = float(input("Digite o valor em metros: "))
centimetros = metros * 100
print(f"{metros} metros equivalem a {centimetros} centimetros.")