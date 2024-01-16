# Exercicio 030
# Faca um programa para o calculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salario bruto (conforme tabela abaixo) e 10% para o INSS e que o FGTS corresponde a 11% do Salario Bruto, mas não é descontado (é a empresa que deposita).

# O Salario Líquido corresponde ao Salario Bruto menos os descontos. O programa devera pedir ao usuario o valor da sua hora e a quantidade de horas trabalhadas no mês.

# Desconto do IR: Salario Bruto até 900 (inclusive) - isento Salario Bruto até 1500 (inclusive) - desconto de 5% Salario Bruto até 2500 (inclusive) - desconto de 10% Salario Bruto acima de 2500 - desconto de 20%

# Imprima na tela as informacões, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

#     Salario Bruto: (5 * 220)        : R$ 1100,00
#     (-) IR (5%)                     : R$   55,00
#     (-) INSS ( 10%)                 : R$  110,00
#     FGTS (11%)                      : R$  121,00
#     Total de descontos              : R$  165,00
#     Salario Liquido                 : R$  935,00
    
valor_hora = float(input("Informe o valor da sua hora:"))
qtd_horas_mes = float(input("Informe a quantidade de horas trabalhadas no mês: "))

salario_bruto = valor_hora * qtd_horas_mes

if salario_bruto >= 0 and salario_bruto <= 900:
    desconto_ir = 0.0
elif salario_bruto <= 1500:
    desconto_ir = 0.05
elif salario_bruto <= 2500:
    desconto_ir = 0.10
elif salario_bruto > 2500:
    desconto_ir = 0.20


ir = salario_bruto * desconto_ir
inss = salario_bruto * 0.10
fgts = salario_bruto * 0.11

total_descontos = ir + inss
salario_liquido = salario_bruto - total_descontos

print(
    f"\nSalário Bruto     : R${salario_bruto:.2f}",
    f"\n(-) IR (5%)       : R${ir:.2f}",
    f"\n(-) INSS ( 10%)   : R${inss:.2f}",
    f"\nFGTS (11%)        : R${fgts:.2f}",
    f"\nTotal de descontos: R${total_descontos:.2f}",
    f"\nSalário Liquido   : R${salario_liquido:.2f}",
)