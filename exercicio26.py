# Exercicio 026
# Faca um programa que pergunte o preco de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

preco1 = float(input("Preço 1:"))
preco2 = float(input("Preço 2:"))
preco3 = float(input("Preço 3:"))

if (preco1 < preco2 and preco1 < preco3): 
    print(f"Compre o produto de preço {preco1}.")
elif (preco2 < preco1 and preco2 < preco3): 
    print(f"Compre o produto de preço {preco2}.")
elif (preco3 < preco1 and preco3 < preco2): 
    print(f"Compre o produto de preço {preco3}.")