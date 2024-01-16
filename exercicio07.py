# Exercicio 007
# Faca um Programa que calcule a area de um quadrado, em seguida mostre o dobro desta area para o usuario.

base = float(input('Base do quadrado: '))
altura = float(input('Altura do quadrado: '))

area = base * altura
dobro = area * 2

print(f'area = {area}')
print(f'Dobro da area = {dobro}')