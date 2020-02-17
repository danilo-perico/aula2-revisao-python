#############################
# Autor: Danilo H. Perico   #
# Exercício 9               #
#############################

class Retangulo:
    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2

    def area(self):
        return self.lado1*self.lado2

    def perimetro(self):
        return 2*self.lado1 + 2*self.lado2

def main():
    lado_um = float(input("Entre com um lado:"))
    lado_dois = float(input("Entre com outro lado:"))
    ret1 = Retangulo(lado_um,lado_dois)
    lado_um = float(input("Entre com um lado:"))
    lado_dois = float(input("Entre com outro lado:"))
    ret2 = Retangulo(lado_um,lado_dois)

    print( ret1.area() )
    print( ret1.perimetro() )

    print( ret2.area() )
    print( ret2.perimetro() )

main()