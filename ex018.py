#faça um prog que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e a tangente desse angulo
#olha a biblioteca
import math
ang = float(input('Digite um ângulo e mostraremos o valor do seno, cosseno e da tangente: '))
angrad = math.radians(ang)
#seno = math.sin(ang)
#cosseno = math.cos(ang)
#tang = math.tan(ang)
print('Ângulo escolhido: {}\nSeno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(ang, math.sin(angrad), math.cos(angrad), math.tan(angrad)))
