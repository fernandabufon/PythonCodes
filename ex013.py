#Faça um prog que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento
salarioAtual = float(input('Salário sem o ajuste: '))
salarioNovo = salarioAtual+(0.15*salarioAtual)
print('O salário novo do funcionário será de R${}'.format(salarioNovo))