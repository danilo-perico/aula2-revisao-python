#############################
# Autor: Danilo H. Perico   #
# Exercício 8               #
#############################

def ano(a,b,c):
    return a*b==(c-1900)

a=int(input('Dia:'))
b=int(input('Mes:'))
c=int(input('Ano:'))

if ano(a,b,c)==True:
    print('Data Mágica!')
else:
    print('A data não é mágica!')

datas=[]
for x in range(1901,2001):
    for y in range(1,13):
        for z in range(1,32):
            if ano(z,y,x)==True:
                datas.append('%d/%d/%d'%(z,y,x))

print('Seguem todas as datas mágicas do século XX:')

for data in datas:
    print(data)