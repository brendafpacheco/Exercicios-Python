# Exercicio 035
# Faca um Programa que peca um número correspondente a um determinado ano e em seguida informe se este ano é ou não 
#bissexto.

ano = int(input("Informe um ano: "))

if ano % 100 == 0 or ano % 4 == 0:
    print("O ano é bissexto.")  
else:
    print("O ano não é bissexto.")
