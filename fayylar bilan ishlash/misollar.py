#f = open("MenHaqimda.txt",'x')
f = open("MenHaqimda.txt",'w')
for i in range(10):
    f.write('Bekzod Nasimov\n')
f = open('MenHaqimda.txt','r')
print(f.read())

