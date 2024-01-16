# Exercicio 011
# Faca um Programa que peca 2 números inteiros e um número real. Calcule e mostre: o produto do dobro do primeiro com metade do segundo. a soma do triplo do primeiro com o terceiro. o terceiro elevado ao cubo.

int1 = int(input('Número inteiro 1: '))
int2 = int(input('Número inteiro 2: '))
float1 = float(input('Número real: '))

calc1 = ((2*int1) * (int2/2))
calc2 = ((3*int1) + float1)    
calc3 = (float1 ** 3)