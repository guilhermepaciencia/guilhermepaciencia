"""
nome = 'Guilherme Paciência'
altura = 1.82
peso = 146.3
imc = peso / (altura * altura)

print(nome, 'tem', altura, 'e pesa', peso ,'quilos', 'e seu IMC é: ', imc)

# F-String

f_string = f'{nome} tem {altura:.2f}de altura e pesa {peso} quilos e seu IMC é: {imc:.2f}'
"""

nome = input('Informe seu nome: ')
altura = float(input('Informe sua altura: '))
peso = int(input('Informe seu peso: '))
imc = peso / (altura * altura)

print(f'Meu nome é {nome} e tenho {altura} de altura,')
print(f'peso {peso} e meu IMC é: {imc:.2f}')

