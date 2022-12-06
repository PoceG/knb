from tkinter import *
import random
root = Tk()
lbl1 = Label(root, text='Opponent choise')
lbl2 = Label(root, text='Your choise')
lbl3 = Label(root, text='Result')
def kamen():
    a = ['kamen', 'nozhnicy', 'bumaga']
    rand = random.choice (a)
    lbl1.config(text=rand)
    lbl2.config(text = 'kamen')
    if rand == 'nozhnicy':
        lbl3.config(text = 'Win')
    if rand == 'bumaga':
        lbl3.config(text = 'Lose')
    if rand == 'kamen':
        lbl3.config(text = 'Nothing')
def nozhnicy():
    a = ['kamen', 'nozhnicy', 'bumaga']
    rand = random.choice (a)
    lbl1.config(text=rand)
    lbl2.config(text = 'nozhnicy')
    if rand == 'bumaga':
        lbl3.config(text = 'Win')
    if rand == 'kamen':
        lbl3.config(text = 'Lose')
    if rand == 'nozhnicy':
        lbl3.config(text = 'Nothing')
def bumaga():
    a = ['kamen', 'nozhnicy', 'bumaga']
    rand = random.choice (a)
    lbl1.config(text=rand)
    lbl2.config(text = 'bumaga')
    if rand == 'kamen':
        lbl3.config(text = 'Win')
    if rand == 'nozhnicy':
        lbl3.config(text = 'Lose')
    if rand == 'bumaga':
        lbl3.config(text = 'Nothing')
btn1 = Button(root, text="kamen", width=30, height=5, bg="white",fg="black", command=lambda:kamen())
btn2 = Button(root, text="nozhnicy", width=30, height=5, bg="white",fg="black", command=lambda:nozhnicy())
btn3 = Button(root, text="bumaga", width=30, height=5, bg="white",fg="black", command=lambda:bumaga())
lbl1.pack()
lbl2.pack()
lbl3.pack()
btn1.pack()
btn2.pack()
btn3.pack()
root.mainloop()
