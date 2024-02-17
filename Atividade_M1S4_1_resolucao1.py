# 5 clientes
# Nome --> str
# CPF --> str
# Idade --> int

# Criar Lista add todos clientes
# Usar 'input()'

# Armazenar cada cliente através de um Dict --> opcional
# Utilizar Classes --> opcional

clientes = []
cpfs = []
idades = []

for cliente in range(5):
    
    nome =  str(input())
    clientes.append(nome)
    cpf = str(input())
    cpfs.append(cpf)
    idade = int(input())
    idades.append(idade)

print(f'Cliente: {clientes[0]}' f' CPF: {cpfs[0]}' f' Idade: {idades[0]}')
print(f'Cliente: {clientes[1]}' f' CPF: {cpfs[1]}' f' Idade: {idades[1]}')
print(f'Cliente: {clientes[2]}' f' CPF: {cpfs[2]}' f' Idade: {idades[2]}')
print(f'Cliente: {clientes[3]}' f' CPF: {cpfs[3]}' f' Idade: {idades[3]}')
print(f'Cliente: {clientes[4]}' f' CPF: {cpfs[4]}' f' Idade: {idades[4]}')

