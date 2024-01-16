# Exercicio 034
# Faca um programa que calcule as raízes de uma equacão do segundo grau, na forma ax² + bx + c.

# O programa devera pedir os valores de a, b e c e fazer as consistências, informando ao usuario nas seguintes situacões:

# Se o usuario informar o valor de A igual a zero, a equacão não é do segundo
#     grau e o programa não deve fazer pedir os demais valores,
#     sendo encerrado;
# Se o delta calculado for negativo, a equacão não possui raízes reais.
#     Informe ao usuario e encerre o programa;
# Se o delta calculado for igual a zero a equacão possui apenas uma raiz
#     real; informe-a ao usuario;
# Se o delta for positivo, a equacão possui duas raiz reais;
#     informe-as ao usuario;

a = float(input("Digite o valor de a: "))

if a != 0:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    delta = (b ** 2) - (4*a*c)
    if delta > 0:
        x1 = (-b * (delta **(1/2)))/2*a 
        x2 = (-b * -(delta **(1/2)))/2*a 
        print(f"Como o delta é posiivo, a equação possui duas raízes reais: X1 = {x1} e X2 = {x2}") 
    else:
        x = (-b)/2*a
        print(f"Como o delta é igual ou menor que 0, a equação possui apenas uma raiz real: {x}") 
else:
    print("Não é equação do 2º grau.")

