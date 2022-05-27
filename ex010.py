#Crie um prog que leia quanto dinheiro uma pessoa tem na carteira e mostre qtos dólares ela pode comprar.
#Obs: 1 dolar = 3,27 reais
dinheiro = float(input('Quantos reais você tem na carteira, meu fi? '))
dolares = dinheiro/3.27
print('Você tem cerca de {:.2f} dólares na carteira.'.format(dolares))