import math
a = int(input("a= "))
b = int(input("b= "))
burchak = int(input("burchakni kiriting= "))
if burchak>0 and burchak<=180:
    print(math.sqrt(a*a+b*b-2*a*b*math.cos(burchak*math.pi/180)))
else:
    print("Burchak bunde berib bolmedi")
