#import RPi.GPIO as GPIO
import time
 
from tkinter import * 
''' 
GPIO.setmode(GPIO.BOARD)
  
#Definicao dos pinos de saida
GPIO.setup(, GPIO.OUT)#alavanca direita
GPIO.setup(, GPIO.OUT)#alavanca esquerda
GPIO.setup(, GPIO.OUT)#luz Geral 
GPIO.setup(, GPIO.OUT)#luz direita
GPIO.setup(, GPIO.OUT)#luz esquerda
GPIO.setup(, GPIO.OUT)#Alimento

#Define os pinoos de entrada
GPIO.setup(, GPIO.IN)#alavanca direita
GPIO.setup(, GPIO.IN)#alavanca esquerda
GPIO.setup(, GPIO.IN)#sensor alimento '''
 
#Estado  das saidas
estado_1 = False
estado_2 = False
estado_3 = False
 
#rotina para ligar as saida
def aciona(pino):
    #GPIO.output(pino, 0)
    return
 
#rotina para desligar as saidas
def desliga(pino):
    #GPIO.output(pino, 1)
    return
'''
#Desligando as saidas
desliga(40)
desliga(40)
desliga(40)
desliga(40)
desliga(40)
desliga(40)
'''

#Define o tamanho da tela
WINDOW_W = 478
WINDOW_H = 280
 
#Definicao de cores
BLACK          = '#000000'
BRIGHTRED      = '#ff0000'
RED            = '#9b0000'
BRIGHTGREEN    = '#00ff00'
GREEN          = '#28A828'
BRIGHTBLUE     = '#0000ff'
BLUE           = '#00009b'
WHITE          = '#ffffff'
YELLOW         = '#ffff00'
  
#cria o display
def createDisplay():
  global tk, canvas, light
  #Cria a janela tk
  tk = Tk()
  tk.title("Soinhos Box")
   
  tk.overrideredirect(True)
  tk.config(cursor="none")
   
  #tk.geometry("{0}x{1}+0+0".format(tk.winfo_screenwidth(), tk.winfo_screenheight()))
   
  #Adiciona a area para desenho
  canvas = Canvas(tk, width=WINDOW_W, height=WINDOW_H, background=BLACK)
   
  #Desenha Botao1  
  obj1Id = canvas.create_rectangle(5,5,159,155,fill=BRIGHTRED, tags = "objt1Tag")
  obj2Id = canvas.create_text( 80, 80,  text="Alavanca direita", fill="white", font=("Helvetica", 20, "bold"))
 
  canvas.tag_bind(obj1Id, '<ButtonPress-1>', onObjectClick1)
  canvas.tag_bind(obj2Id, '<ButtonPress-1>', onObjectClick1)
 
  #Desenha Botao2
  obj3Id = canvas.create_rectangle(162, 5, 316, 155,fill=GREEN,tags = "objt3Tag")
  obj4Id = canvas.create_text(236, 80,  text="Luz Geral", fill="white", font=("Helvetica", 20, "bold"))
   
  canvas.tag_bind(obj3Id, '<ButtonPress-1>', onObjectClick2)
  canvas.tag_bind(obj4Id, '<ButtonPress-1>', onObjectClick2)
 
  #Desenha Botao3
  obj5Id = canvas.create_rectangle(319, 5, 473,155,fill=BRIGHTBLUE,tags = "objt5Tag")
  obj6Id = canvas.create_text(396, 80,  text="Alavanca esquerda", fill="white", font=("Helvetica", 20, "bold"))
   
  canvas.tag_bind(obj5Id, '<ButtonPress-1>', onObjectClick3)
  canvas.tag_bind(obj6Id, '<ButtonPress-1>', onObjectClick3)
     
  canvas.pack()
 
  #Cria botao SAIR
  btn = Button(tk, height=1, text="Sair", font=("Arial", 12, "bold"), command=terminate)
  btn.pack()
   
  #Retangulo mensagem 
  canvas.create_rectangle(5,160, 473, 275,fill=WHITE)
 
  #Verifica se a paleta foi  acionada
  tk.after(100, checkPort)
  tk.mainloop() 

 
#def onObjectClick1(event):
  #Clique no botao 1
  #global estado_1
  #estado_1 = not estado_1
  #if estado_1 == True:
  '''
      deliga(38)
      desliga(36)
      deliga(38)
      desliga(36)
      deliga(38)
      desliga(36)
      aciona(40)'''
  #if estado_1 == False:
      #desliga(40)
    #Clique no botao 2
#def onObjectClick2(event):
   # global estado_2
   # estado_2 = not estado_2
    #if estado_2 == True:
      #deliga(38)
      #desliga(36)
      #deliga(38)
      #desliga(36)
      #deliga(38)
      #esliga(36)
      #aciona(40)
  #if estado_2 == False:
      #desliga(38)
#def onObjectClick3(event):
  #Clique no botao 3
  #global estado_3
  #estado_3 = not estado_3
  #if estado_3 == True:
   #   deliga(38)
    #  desliga(36)
     # deliga(38)
    #desliga(36)
    #  deliga(38)
    #  desliga(36)
    #  aciona(40)
    #  if estado_3 == False:
      #aciona(36)
#def checkPort():
    #Verifica se a alavanca foi acionada
    
    #if GPIO.input(37) == False:
        #Cria retangulo em amarelo e exibe mensagem
        #canvas.create_rectangle(10,165, 468, 270,fill=YELLOW)
        #canvas.create_text(240, 220,  text="ATIVADO", fill="BLACK", font=("Arial", 70, "bold"))
   # if GPIO.input(37) == True:
        #Cria retangulo branco
        #canvas.create_rectangle(5,160, 473, 275,fill=WHITE)
        #canvas.create_text(240, 220,  text="Aguardando", fill='#E5E4E2', font=("Arial", 50, "bold"))
        #tk.after(200,checkPort)
   #Acao do botao SAIR
def terminate():
    global tk
    tk.destroy()
def main():
    createDisplay()