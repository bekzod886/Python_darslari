from tkinter import *


def sel():
    selection = "Siz tanlagan soz tarjimasi= " + str(var.get())
    label.config(text=selection)


root = Tk()
root.geometry('400x250')
var = StringVar(root, '1')
R1 = Radiobutton(root, text="Hello", variable=var, value='Salom',
                 )
R1.pack(anchor=W)

R2 = Radiobutton(root, text="World", variable=var, value="Dunyo", )
R2.pack(anchor=W)
R3 = Radiobutton(root, text="students", variable=var, value="O'quvchilar", )
R3.pack(anchor=W)
R4 = Radiobutton(root, text="school", variable=var, value="Maktab", )
R4.pack(anchor=W)

B = Button(root, text="Tarjima qilish", command=sel)
B.pack()
label = Label(root)
label.pack()
root.mainloop()
