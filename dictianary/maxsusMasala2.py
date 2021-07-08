person1yoshi = int(input("Person1: "))
person2yoshi = int(input("Person2: "))
person1 = {
    "name": "John",
    "father": "Bill",
    "mother": "Anna",
    "married": 0
}
person2 = {
    "name": "Kate",
    "father": "Pet",
    "mother": "Maria",
    "married": 0
}
person3 = {}
person1["married"]=person1yoshi
person2["married"]=person2yoshi
print(person1)
print(person2)
if person1["married"]==person2["married"]:
    person3.update({"name":"Dote","father":"John","mother":"Kate"})
    print(person3)
else:
    print("Ular turmush qurmagan")
