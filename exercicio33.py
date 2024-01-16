# Exercicio 033
# Faca um Programa que peca os 3 lados de um triângulo. O programa devera informar se os valores podem ser um triângulo. 
#Indique, caso os lados formem um triângulo, se o mesmo é: equilatero, isósceles ou escaleno.
# Dicas: Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro; Triângulo 
#Equilatero: três lados iguais; Triângulo Isósceles: quaisquer dois lados iguais; Triângulo Escaleno: três lados 
#diferentes;

lado1 = float(input("Lado 1: "))
lado2 = float(input("Lado 2: "))
lado3 = float(input("Lado 3: "))

if (lado1 + lado2) > lado3 or (lado2 + lado3) > lado1 or (lado3 + lado1) > lado2:
    if lado1 == lado2 and lado2 == lado3:
        tipo_triangulo = "Equilátero"
    elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
        tipo_triangulo = "Isósceles"
    elif lado1 != lado2 and lado2 != lado3:
        tipo_triangulo = "Escaleno"
else:
    print("Não é um triângulo.")
    
print(f'É um triângulo: {tipo_triangulo}') 