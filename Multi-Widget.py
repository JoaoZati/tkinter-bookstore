from tkinter import *

list_convert = [1000, 2.20462, 35.274]


def convert():
    print(input_kg.get())
    for indice, value in enumerate(list_convert):
        converted = round(value * float(input_kg.get()), 2)
        list_text[indice].delete('1.0', END)
        list_text[indice].insert(END, converted)


window = Tk()

input_kg = StringVar()

l1 = Label(window, text='Kg')
l1.grid(row=0, column=0)

e1 = Entry(window, textvariable=input_kg)
e1.grid(row=0, column=1)

b1 = Button(window, text='Covert', command=convert)
b1.grid(row=0, column=2)

list_text = []
for i in range(3):
    list_text.append(Text(window, height=1, width=30))
    list_text[i].grid(row=1, column=i)

window.mainloop()
