#importar um pacote de SO
import os

#limpar tela
os.system('cls')
print('--------------------------')

nome = input('Digite seu nome: ')
print('Você digitou ' + nome)

idade = input('Digite seu idade: ')
print(f'Sua idade é {idade}')
#sempre que o número vier como input ele virá como string

print ('O ' + nome + ' tem a idade de ' + idade)
print (f'O {nome} tem a idade de {idade}')
dias = 365*int(idade)
print(f'O {nome} viveu cerca de {dias} dias')

