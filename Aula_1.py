"""
sep = separador de dados
end = o que será exibido no fim do texto, por padrão
são exibido a quebra de linha \r ou \n
"""
#print(12, 34, sep='-', end='# \n')
#print(56, 78, sep='-')

"""
string = texto, utiliza com ' ' ou " "
"""
#print('Guilherme henrique')
"""
int -> numeros inteiro
ex: 11 ou -11

float -> flutuante ou decimal
ex: 1.2 ou 2.1
"""
print(1, -1, 1, 2, -1.2)

"""
tipo de dados bool(boolean)
sim(True ou não (False))
"""
print(10 == 10) #Sim
print(10 == 11) #Não

# Type
print(type('Guilherme'))#type informa o tipo de dados: str, int, float ou bool

nome = 'Guilherme'
idade = 28
maior_idade = idade >= 18
print('Nome:', nome, 'Idade:',idade)
print('É maior de idade?', maior_idade)