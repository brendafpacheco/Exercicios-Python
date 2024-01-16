# Exercicio 018
# Faca um programa que peca o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo
# aproximado de download do arquivo usando este link (em minutos).

sizeFile = float(input("Informe o tamanho do arquivo para download: "))
velocidade = float(input("Informe a velocidade do link em Mbps: "))

tempos = (sizeFile * 8) / velocidade
minutos = tempos // 60
segundos = tempos % 60
print(f"{minutos:.0f} Minutos e {segundos:.0f} Segundos")