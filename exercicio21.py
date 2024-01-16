# Exercicio 021
# Faca um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Invalido.

sexo = input("Digite um sexo:")

if (sexo == "F" or sexo == "f"): 
    print("F - Feminino")
elif (sexo == "M" or sexo == "m"):
    print("M - Masculino")
else:
    print("Sexco inválido")