#############################
# Autor: Danilo H. Perico   #
# Exercício 4               #
#############################

combustivel = input("Escolha o combustível:\na- Álcool\ng- Gasolina\n")
qtd = float(input("Entre a quantidade (litros): "))

if combustivel == "a":
  if qtd > 0 and qtd <= 20:
    total = qtd * 3.19 - qtd * 3.19 * 0.03
  else:
    total = qtd * 3.19 - qtd * 3.19 * 0.05
elif combustivel == "g":
  if qtd > 0 and qtd <= 20:
    total = qtd * 4.59 - qtd * 4.59 * 0.04
  else:
    total = (qtd * 4.59) - (qtd * 4.59 * 0.06)

print("Valor total: R$ %.2f" % total)