#Faça um prog que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, caucule
#mostre o comprimento da hipotenusa

import math
print('===CALCULADORA DA HIPOTENUSA DE UM TRIANGULO RETANGULO===')
catOposto = float(input('Digite o comprimento do Cateto Oposto: '))
catAdjacente = float(input('Digite o comprimento do Cateto Adjacente: '))
#hipotenusa = float(math.sqrt((math.pow(catOposto, 2))+(math.pow(catAdjacente, 2))))
hipotenusa = float(math.hypot(catOposto, catAdjacente))
print('Um triângulo retângulo com os catetos de comprimentos {} e {} possui uma hipotenusa com comprimento de aproximadamente {:.2f}'
      .format(catOposto, catAdjacente, hipotenusa))

