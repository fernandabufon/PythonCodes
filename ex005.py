#Faça um programa que leia um num inteiro e mostre na tela seu sucessor e seu antecessor
numero = int(input('Escreva um número e veja seu antecessor e seu sucessor: '))
antecessor = numero-1 #podia ser a
sucessor = numero+1
print('O número escolhido foi {}.\nO antecessor desse número é {}, e seu sucessor é {}.'.format(numero, antecessor, sucessor))


#print('O número escolhido foi {}.\nO antecessor desse número é {}, e seu sucessor é {}.'.format(numero, (numero-1), (numero+1)))
#tente usar menos memória possível