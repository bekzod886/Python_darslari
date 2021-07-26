from tkinter import *
m = Tk()  # bu biz yaratgan oyna

# # label yaratish
# meningLabelim = Label(m, text="Assalomu alaykum")
#
# # oynaga joylash
# meningLabelim.pack()
# m.mainloop()  # oynani ushlab turish
m.geometry('600x400')
btn = Button(m,text="Salom", bd='10',bg='yellow',command=m.destroy)

btn.pack()
m.mainloop()