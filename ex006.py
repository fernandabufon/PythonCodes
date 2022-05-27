#Crie um algoritmo que leia um numero e mostre o seu dobro, o triplo e a raiz quadrada.
numero = int(input('Digite um número e descubra seu dobro, triplo e a sua raiz quadrada: '))
dobro = numero*2
triplo = numero*3
raiz = numero**(1/2)
print('Número escolhido: {}\nDobro: {}\nTriplo: {}\nRaiz Quadrada: {}'.format(numero, dobro, triplo, raiz))

print('Número escolhido: {}\nDobro: {}\nTriplo: {}\nRaiz Quadrada: {:.3f}'.format(numero, (numero*2), (numero*3), (numero**(1/2))))
