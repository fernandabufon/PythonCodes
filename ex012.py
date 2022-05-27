#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
preco = float(input('Digite o preço atual do produto: '))
precoNovo = float(preco-(preco * 0.05))
print('O produto passará a valer R${:.2f} a partir de agora.'.format(precoNovo))
