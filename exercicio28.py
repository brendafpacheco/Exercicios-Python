# Exercicio 028
# Faca um Programa que pergunte em que turno você estuda. Peca para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Invalido!", conforme o caso.

turno = str(input("M - matutino | V - vespertino | N - noturno")).upper()

if (turno == 'M'):
    print("Bom dia!")
elif (turno == 'V'):
    print("Boa tarde!")
elif (turno == 'N'):
    print("Boa noite!")
else:
    print("Valor inválido.")