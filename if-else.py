import os
os.system('cls')
print('-------------------')

nome = input('Digite seu nome: ')

#conversão direta do padrão do input de string pra int
idade = int(input('Digite sua idade: '))

if (idade>=18):
    print ('Pode entrar')
    print (f'Parabéns {nome}')
else:
    print ('Não pode entrar')

print('----------------------')
