# ism familiya kiritish bunda agar kiritgan satrda probel bo'lmasa qayta kiritsin
while True:
    name = input("ism: ")
    """grandFatherName = input("ism: ")
    fatherName = input("ism: ")
    jinsi = input("ism: ")"""
    name = name.split()
    if len(name) == 1:
        break
    elif len(name) > 1:
        print("Faqat ism  kerak ortiqchani yozmang!")
    else:
        print("Ism  kiriting!")

while True:

    grandFatherName = input("Familiya: ")
    """fatherName = input("ism: ")
    jinsi = input("ism: ")"""
    grandFatherName = grandFatherName.split()
    if len(grandFatherName) == 1:
        break
    elif len(grandFatherName) > 1:
        print("familiya kiriting!")
    else:
        print("familiyani kiriting!")