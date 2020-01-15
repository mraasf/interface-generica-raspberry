#Autor : mraasf
import time
contador = 1

 
while(contador != 0 ):
    i = 1
    
    print("\n----------------------------------------MENU DE OPCOES----------------------------------------------------")
    print("0 - SAIR")
    print("1  - paleta direita")
    print("2- paleta esquerda")
    print("3 - lampada direita ")
    print("4 - lampada esquerda ")
    print("5 - lampada principal ")
    print("6 - Alimento ")
    print("----------------------------------------------------------------------------------------------------------\n")
    contador = int(input("DIGITE A SUA OPCAO: "))
    if 0 < contador > 0:
        tempo = int(input("DIGITE o tempo em segundos: "))
    j=1
    while(0 < contador < 8):
        if contador == 1:
            print ("paleta direita",j)
            time.sleep(1)
            if j >= tempo:
                contador=8
        j=j+1
        if contador == 2:
            print ("paleta esquerda")
            time.sleep(1)
            if j >= tempo:
                contador=8
        j=j+1
        if contador == 3:
            print ("lampada direita")
            time.sleep(1)
            if i >= tempo:
                contador=8
        i=i+1
        if contador == 4:
            print ("lampada esquerda")
            time.sleep(1)
            if i >= tempo:
                contador=8
        i=i+1
        if contador == 5:
            print ("lampada principal")
            time.sleep(1)
            if i >= tempo:
                contador=8
        i=i+1
        if contador == 6:
            print ("alimento")
            time.sleep(1)
            if i >= tempo:
                contador=8
        i=i+1
        if contador == 7:
            print ("tudo ativo")
            time.sleep(1)
            if i >= tempo:
                contador=8
        i=i+1
        
