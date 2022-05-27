#Crie um programa que leia um numero real qualquer e mostre na tela a sua porção inteira
import math
num = float(input('Escreva um número real qualquer: '))
#numInt = math.trunc(num)
#print('A parte inteira do número {} é {}'.format(num, numInt))
#print('A parte inteira do número {} é {}'.format(num, int(num))
print('A parte inteira do número {} é {}'.format(num, (math.trunc(num))))
