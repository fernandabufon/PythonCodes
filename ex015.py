dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos km foram rodados? '))
valor = float((60*dias)+(0.15*km))
print('O aluguel ficou R$ {:.2f}'.format(valor))
