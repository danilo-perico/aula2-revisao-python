#############################
# Autor: Danilo H. Perico   #
# Exercício 6               #
#############################

lista_completa = []
lista_pares = []
lista_impares = []
i = 0

while i < 20:
    num = int(input("Entre com um número: "))
    lista_completa.append(num)
    
    if num % 2 == 0:
        lista_pares.append(num)
    else:
        lista_impares.append(num)
    i = i+1
 
print()
print(lista_completa)
print(lista_pares)
print(lista_impares)