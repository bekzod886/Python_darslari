try:
    n = int(input())
    if n%2==0:
        raise Exception()
except:
    print("Juft son kiritmang")
else:
    print("To'g'ri")
finally:
    print("Dastur tugadi")