# Exercicio 023
# Faca um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcancada por aluno e apresentar: A mensagem "Aprovado", se a média alcancada for maior ou igual a sete; A mensagem "Reprovado", se a média for menor do que sete; A mensagem "Aprovado com Distincão", se a média for igual a dez.

nota1 = float(input("Digite a nota 1:"))
nota2 = float(input("Digite a nota 2:"))

media = (nota1 + nota2) / 2

if (media >= 7):
    print("Aprovado!")
elif (media < 7): 
    print("Reprovado")
elif (media == 10):
    print("Aprovado com distinção.") 