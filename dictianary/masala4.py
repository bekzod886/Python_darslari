yosh = int(input("Yosh: "))
shaxs ={
    "ismi":"Ali",
    "Yoshi": 10,
    "oquvchi": True
}
if shaxs["Yoshi"]+yosh>19:
    shaxs["oquvchi"]=False
print(shaxs)
if shaxs["Yoshi"]+yosh>19:
    del shaxs["ismi"]
print(shaxs)
