import tkinter as tk
import customtkinter as tks

root = tk.Tk()
root.geometry('300x200')
root['bg'] = 'lightblue'

symbols = ['*', '/', '+', '-', '7', '8', '9', '0', '4', '5', '6', 'C', '1', '2', '3', '=']

c = 0
r = 1


def func(x):

    if x == "C":
        text1.configure(text='')

    elif x == '=':
        text1['text'] = eval(text1['text'])
    else:
        text1['text'] += x


for j in range(4):

    root.columnconfigure(weight=1, index=j, minsize=4)

for b in range(5):

    root.rowconfigure(index=b, weight=1, minsize=4)


text1 = tk.Label(root, text='', bg='lightblue')
text1.grid(row=0, column=0, columnspan=4)

for i in symbols:
        btn = tks.CTkButton(root, text=i, command=lambda x=i: func(x)).grid(row=r, column=c, sticky='nsew')

        c += 1
        if c > 3:

             r += 1
             c = 0

root.mainloop()