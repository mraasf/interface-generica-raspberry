# script by mraasf
from tkinter import *
janela = Tk()


# paletas direita e esquerda
bt = Button(janela, width= 15 , text="left")
bt.place(x=30, y=50)
bt = Button(janela, width= 15 , text="Right")
bt.place(x=220, y=50)
lb = Label(janela, width= 20 , text="pallet")
lb.place(x=100 , y=100)

# luzes direita esquerda e house

bt = Button(janela, width= 10 , text="left")
bt.place(x=20 , y=150)
bt = Button(janela, width= 10 , text="House")
bt.place(x=160, y=150)
bt = Button(janela, width= 10 , text="Right")
bt.place(x=280, y=150)
lb = Label(janela, width= 20 , text="light")
lb.place(x=100 , y=200)


# alimento

bt = Button(janela, width= 30 , text="feeder")
bt.place(x=50, y=250)


bt = Button(janela, width= 30 , text="Sair")
bt.place(x=50, y=300)


janela.geometry("400x400+200+200")
janela.mainloop()