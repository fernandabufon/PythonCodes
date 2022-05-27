#faça um prog que leia o nome de quatro alunos e mostre a ordem sorteada
from random import shuffle
aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))
lista = [aluno3, aluno4, aluno2, aluno1]
shuffle(lista)
print('A ordem sorteada foi: ')
print(lista)

