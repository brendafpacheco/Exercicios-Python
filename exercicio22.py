# Exercicio 022
# Faca um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Digite uma letra:").upper()

if (letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U"):
    print("A letra digitada é uma vogal.")
else: 
    print("A letra digitada é uma consoante.")