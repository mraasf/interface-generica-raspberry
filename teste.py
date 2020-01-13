#Autor : mraasf
 
 
import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BOARD)


#entradas das paletas // contador de toques
left = 36
right = 38

#Define os pinos como saida
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(29, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(29, GPIO.OUT)
GPIO.setup(40, GPIO.OUT) 

#entradas das paletas
GPIO.setup(36, GPIO.IN)
GPIO.setup(38, GPIO.IN)


#desliga todos as saidas
GPIO.output(16,0)#pino 16
GPIO.output(18,0)#pino 18
GPIO.output(29,0)#pino 29
GPIO.output(31,0)#pino 31

GPIO.output(40,0)#pino 40 saida house light
contador = 1

while(1):

    if contador == 1:
        GPIO.output(16, 1)
        print ("paleta direita")
        contador+=1
        time.sleep(1)
        GPIO.output(16, 0)
    #Caso contador = 2, aciona a saida
    if contador == 2:
        GPIO.output(18, 1)
        print ("paleta esquerda")
        contador+=1
        time.sleep(1)
        GPIO.output(18, 0)
 
    #Caso contador = 3, aciona a saida
    if contador == 3:
        GPIO.output(29, 1)
        print ("lampada direita")  
        contador+=1
        time.sleep(1)
        GPIO.output(29, 0)
        #Caso contador = 4, aciona a saida
    if contador == 4:
        GPIO.output(31, 1)
        print ("lampada esquerda ")
        contador+=1
        time.sleep(1)
        GPIO.output(31, 0)
            #Caso contador = 5, aciona a saida
    if contador == 5:
        GPIO.output(33, 1)
        print ("alimento ")
        contador+=1
        time.sleep(1)
        GPIO.output(33, 0)    
    if contador == 6:
        GPIO.output(40, 1)
        print ("house light ")
        contador+=1
        time.sleep(1)
        GPIO.output(40, 0)
     
    #Caso contador = 7, desliga todas as saidas
    #zera a variavel contador
    if contador == 7:
        print ("teste terminou \n desligando as saidas e zerando o contador")
        GPIO.output(16,0)
        GPIO.output(18,0)
        GPIO.output(29,0)
        GPIO.output(31,0)
        GPIO.output(33,0)
        GPIO.output(40,0)
        contador = 0
    #left = 0 
    #if GPIO.input(left) == 0:
    #    print("left desligado")
    #if GPIO.input(left) == 1:
    #GPIO.output(16,1)
     #   GPIO.output(18,1)
     #   print("left LIGADO")
      
   


