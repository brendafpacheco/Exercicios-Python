# Exercicio 015
# Faca um Programa que pergunte quanto você ganha por hora e o número de horas 
# trabalhadas no mês. Calcule e mostre o total do seu salario no referido mês, 
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para
# o sindicato, faca um programa que nos dê: salario bruto. quanto pagou ao INSS. quanto
# pagou ao sindicato. o salario líquido. calcule os descontos e o salario líquido, 
# conforme a tabela abaixo:

# + Salario Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salario Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

salarioPorHora = float(input('Salário recebido por hora trabalhada: '))
horasTrabalhadasMes = float(input('Horas trabalhadas no mês: '))
salarioBruto = (salarioPorHora * horasTrabalhadasMes)
impostoRenda = salarioBruto * 0.11
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.05
descontos = impostoRenda + inss + sindicato
salarioLiquido = salarioBruto - descontos

print(f" + Salário Bruto : R$ {salarioBruto} \n - IR (11%) : R$ {impostoRenda} \n - INSS (8%) : R$ {inss} \n - Sindicato ( 5%) : R$ {sindicato} \n  = Salário Liquido : R$ {salarioLiquido}")
