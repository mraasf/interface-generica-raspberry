from  tkinter import *

janela = TK()
janela.title("janela principal")
janela["bg"]  = "green"
janela.geometry("800x300")

def bt_click():
    print("bt_click")
    lb ["text"] = "01"

bt= Button(janela, width=20, text = "saida 01")
bt.place(x=100 , y = 100)


lb = Label(janela,text="01")
lb.place(x=100 , y = 150)
janela.mainloop()