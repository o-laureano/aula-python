import os
os.system('cls')

nome = input("Digite seu nome: ")
salario = float(input("Digite seu salário: "))

print('O {0} ganha R${1}'. format(nome, salario))

if (salario>=5000):
    desconto = salario*27/100
    print('O desconto do salário do {0} é de {1}'.format(nome, desconto))
else:
    desconto = salario*20/100
    print('O desconto do salário do {0} é de {1}'.format(nome, desconto))