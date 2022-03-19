vendas_funcionario_1 = int(input('Entre com as vendas do funcionário 1: '))
vendas_funcionario_2 = int(input('Entre com as vendas do funcionário 2: '))
vendas_funcionario_3 = int(input('Entre com as vendas do funcionário 3: '))

if vendas_funcionario_1 >= 1000:
    bonus = vendas_funcionario_1 * 0.01
else:
    bonus = 0
print('O funcionário 1 ganhou {} de bônus'.format(bonus))
    
if vendas_funcionario_2 >= 1000:
    bonus = vendas_funcionario_2 * 0.01
else:
    bonus = 0
print('O funcionário 2 ganhou {} de bonus'.format(bonus))

if vendas_funcionario_3 >= 1000:
    bonus = vendas_funcionario_3 * 0.01
else:
    bonus = 0
print('O funcionário 3 ganhou {} de bônus'.format(bonus))


