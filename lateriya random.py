import random
imkon = 1
while imkon<=5:
    son = random.randint(1,10)
    kiritlilganSon = int(input("son: "))
    if kiritlilganSon == son:
        print("Yuttingiz")
        break
    else:
        print("Dam oling")
    imkon+=1