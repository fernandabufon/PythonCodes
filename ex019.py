#faça um prog que leia quatro nomes, sorteie e escreva o numero escolhido na tela

from random import choice
nome1 = str(input('Digite o nome do aluno um: '))
nome2 = str(input('Digite o nome do aluno dois: '))
nome3 = str(input('Digite o nome do aluno três: '))
nome4 = str(input('Digite o nome do aluno quatro: '))
lista = [nome1, nome2, nome3, nome4]
sorteio = choice(lista)
print("O aluno sorteado foi o {}".format(sorteio))

