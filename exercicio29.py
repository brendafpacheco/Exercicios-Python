# Exercicio 029
# As Organizacões Tabajara resolveram dar um aumento de salario aos seus colaboradores e lhe contrataram para desenvolver 
#o programa que calculara os reajustes.
# Faca um programa que recebe o salario de um colaborador e o reajuste segundo o seguinte critério, baseado no salario 
#atual:

# salarios até R$ 280,00 (incluindo) : aumento de 20%
# salarios entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salarios entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salarios de R$ 1500,00 em diante :
#     aumento de 5% Após o aumento ser realizado,
# informe na tela:
#     o salario antes do reajuste;
#     o percentual de aumento aplicado;
#     o valor do aumento;
#     o novo salario, após o aumento.

salario_anterior = float(input("Informe seu salário anterior:"))

if salario_anterior > 0 and salario_anterior <= 280:
    percentual_de_aumento = 0.2
    valor_aumento = salario_anterior * percentual_de_aumento
    salario_atual = salario_anterior + valor_aumento
    print(f'Salário antes do reajuste: {salario_anterior} \n Percentual de aumento aplicado: 20% \n Valor do aumento: {valor_aumento} \n Salário atual: {salario_atual}')
elif salario_anterior > 280 and salario_anterior <= 700: 
    percentual_de_aumento = 0.15
    valor_aumento = salario_anterior * percentual_de_aumento
    salario_atual = salario_anterior + valor_aumento
    print(f'Salário antes do reajuste: {salario_anterior} \n Percentual de aumento aplicado: 15% \n Valor do aumento: {valor_aumento} \n Salário atual: {salario_atual}')
elif salario_anterior > 700 and salario_anterior <= 1500: 
    percentual_de_aumento = 0.10
    valor_aumento = salario_anterior * percentual_de_aumento
    salario_atual = salario_anterior + valor_aumento
    print(f'Salário antes do reajuste: {salario_anterior} \n Percentual de aumento aplicado: 10% \n Valor do aumento: {valor_aumento} \n Salário atual: {salario_atual}')
elif salario_anterior >= 1500: 
    percentual_de_aumento = 0.05
    valor_aumento = salario_anterior * percentual_de_aumento
    salario_atual = salario_anterior + valor_aumento
    print(f'Salário antes do reajuste: {salario_anterior} \n Percentual de aumento aplicado: 5% \n Valor do aumento: {valor_aumento} \n Salário atual: {salario_atual}')
else:
    print("Valor inválido.") 