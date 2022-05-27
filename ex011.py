#Faça um prog que leia a largura e a altura de uma parede em metros, calcule sua área e a qtd de tinta necessária
#pra pintá-la, sabendo que cada L de tinta pinta uma área de 2m

largura = float(input('Largura da parede em metros: '))
altura = float(input('Altura da parede em metros: '))
print('Calculando área total da parede e a quantidade de tinta...')
areaTotal = largura*altura
qtdTinta = areaTotal/2
print('A parede tem {:.2f} metros quadrados e vai precisar de {:.0f} litros de tinta para ser completamente pintada.'.format(areaTotal, qtdTinta))
