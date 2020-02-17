#############################
# Autor: Danilo H. Perico   #
# Exercício 1               #
#############################

dias = int(input("Entre com os dias: "))
horas = int(input("Entre as horas: "))
minutos = int(input("Entre as minutos: "))
segundos = int(input("Entre os segundos: "))

print("Valor em segundos", dias*24*60*60+horas*60*60+minutos*60+segundos)