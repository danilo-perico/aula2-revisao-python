#############################
# Autor: Danilo H. Perico   #
# Exercício 3               #
#############################

sal = int(input("Entre com o salário (R$): "))

if sal > 1250:
    aumento = sal * 0.10
else:
    aumento = sal * 0.15

print("O aumento foi de R$", aumento)
print("O novo salário é R$", sal+aumento)
