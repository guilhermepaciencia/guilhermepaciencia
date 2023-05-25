"""
Operadores Lógicos
and (e), or (ou), not(não)

and - Todas as condições precisam ser verdadeiras.
se qualquervalor for considerado falso, a expressão
inteira será avaliada naquele valor.

none - é usado para representar um não valor.

"""
entrada = input('[E]ntrar ou [S]air: ')
senha = input('Senha: ')
senha_permitida = '123'

if entrada == 'E' and senha == senha_permitida:
    print('Entrar')
else:
    print('Sair')


#or - se tiver qualquer valor verdadeiro a expressão
#inteira será avaliada naquele valor.

entrada = input('[E]ntrar ou [S]air: ')
senha = input('Senha: ')
senha_permitida = '123'

if (entrada == 'E'or entrada == 'e') and senha == senha_permitida:
    print('Entrar')
else:
    print('Sair')


#operador not - usado para inverter opeções
#not True = False
#not False = True

senha = input('Senha: ')
if senha != '123456':
    print('Senha incorreta.')


#operadores in e not in
#in = esta entre
#not in =  não esta estre
#
# String são iteráveis
#
# 0 1 2 3 4
# G U I G A
#-4-3-2-1-0

nome = 'Guiga'
print(nome[3])

print('e' in nome)
print('e' not in nome) 