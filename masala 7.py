x = int(input('x='))

a = birlar = x % 10
b = unlar = x % 100 // 10
c = yuzlar = x // 100
if birlar == unlar or birlar == yuzlar or unlar == yuzlar:
    print('bir xil sonlar mavjud')
else:
    print('bir xil sonlar mavjud emad')
