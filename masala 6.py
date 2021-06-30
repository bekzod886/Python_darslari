# 80 bet 1 masala
x = int(input("x="))
unlar = x // 10
birlar = x % 10

if unlar % 2 == 0:
    print('o`nlar xonasidagi juft son')
else:
    print('o`nlar xonasidagi toq son')

if birlar % 2 == 0:
    print('birlar xonasidagi juft son')
else:
    print('birlar xonasidagi toq son')