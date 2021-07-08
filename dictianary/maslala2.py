shaxslar = [
    {
        "Otasini ismi": "Davron",
        "ismi":"Ali",
        "yoshi": 18,
        "jinsi": "erkak"
    },
    {
        "Otasini ismi": "Farrux",
        "ismi":"Vali",
        "yoshi": 21,
        "jinsi": "erkak"
    },
    {
        "Otasini ismi": "Abir",
        "ismi":"Kamola",
        "yoshi": 22,
        "jinsi": "ayol"
    }
]

v = []
for ism in shaxslar:
    if ism["jinsi"] =="erkak":
        ism["familyasi"] =ism["Otasini ismi"]+"ov"
        v.append(ism)
    else:
        ism["familyasi"] = ism["Otasini ismi"]+"ova"
        v.append(ism)
print(v)











