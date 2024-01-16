# Exercicio 014
# João Papo-de-Pescador, homem de bem, comprou um microcomputador para 
# controlar o rendimento diario de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo 
# regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma
# multa de R$ 4,00 por quilo excedente.
# João precisa que você faca um programa que leia a variavel peso (peso 
# de peixes) e calcule o excesso.
# Gravar na variavel excesso a quantidade de quilos além do limite e na 
# variavel multa o valor da multa que João devera pagar. Imprima os dados
# do programa com as mensagens adequadas.

peso = float(input('Insira o peso do peixe: '))

if (peso > 50):
    excesso = (peso - 50)
    multa = excesso * 4.00
    print(f'O peixe inserido tem excesso de peso: {excesso} kg. A multa a ser paga por esse excesso é de {multa}')
else:
    print('Não ha excesso de peso.')