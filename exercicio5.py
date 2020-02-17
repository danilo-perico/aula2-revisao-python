#############################
# Autor: Danilo H. Perico   #
# Exercício 5               #
#############################

quantidade = 0
somatoria = 0
media = 0

while True:
    num = float(input("Entre com um número ou 0 para sair: "))
    
    if num == 0.0:
        media = somatoria / quantidade
        print()
        print("Quantidade de dígitos:", quantidade)
        print("Somatória de todos os valores:", somatoria)
        print("Média:", media)
        break
    
    quantidade = quantidade + 1
    somatoria = somatoria + num