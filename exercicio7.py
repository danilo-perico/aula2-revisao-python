#############################
# Autor: Danilo H. Perico   #
# Exercício 7               #
#############################

from random import randint

bilhete = []
x = 0

while x < 6:
  valor = randint(1,50)
  if valor not in bilhete:
    bilhete.append(valor)
    x += 1

print("Conjunto de números gerado: ", bilhete)    