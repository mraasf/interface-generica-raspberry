from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import  BoxLayout
from kivy.uix.label import Label 
from kivy.uix.textinput import TextInput


class Soinhos_Box(App):
    
    #inicializa e constroi o app
    def build(self):
# quadrante principal
        box = BoxLayout(orientation="vertical")
# primeiro quadrante              
        box2 = BoxLayout(orientation="horizontal")
                
        box.add_widget(box2)
# segundo quadrante        
        box8 = BoxLayout()
        box.add_widget(box8)
        
        box4 = BoxLayout(orientation="vertical")
        label1 = Label(text="animal")
        label2 = Label(text="alavanca")
        label3 = Label(text="Tempo")
        box4.add_widget(label1)
        box4.add_widget(label2)
        box4.add_widget(label3)
        #box2.add_widget(label2)
        
        box2.add_widget(box4)
        
        box3 = BoxLayout(orientation="vertical")
        label1 = Label(text=" ")
        textinput1 = TextInput(text='', multiline=False)
        label2 = Label(text=" ")
        textinput2 = TextInput(text='', multiline=False)
        label3 = Label(text=" ")
        textinput3 = TextInput(text='', multiline=False)
        
        box3.add_widget(label1)
        box3.add_widget(textinput1)
        box3.add_widget(label2)
        box3.add_widget(textinput2)
        box3.add_widget(label3)
        box3.add_widget(textinput3)
        
        box2.add_widget(box3)
        
        box4 = BoxLayout(orientation="vertical")
        label1 = Label(text="escolha uma opcao")
        button3= Button(text="teste01")
        label2 = Label(text=" ")
        button4= Button(text="teste02")
        label3 = Label(text=" ")
        button5= Button(text="teste03")
        
        box4.add_widget(label1)
        box4.add_widget(button3)
        box4.add_widget(label2)
        box4.add_widget(button4)
        box4.add_widget(label3)
        box4.add_widget(button5)
        
        
        box2.add_widget(box4)
        
        # --------------------------------  segundo quadrante -------------------
        
        box5 = BoxLayout(orientation="vertical")
        label1 = Label(text="ANIMAL:")
        label2 = Label(text="TOQUES NA DIREITA:")
        label3 = Label(text="TOQUES NA ESQUERDA:")
        box5.add_widget(label1)
        box5.add_widget(label2)
        box5.add_widget(label3)
        #box2.add_widget(label2)
        
        box8.add_widget(box5)
        
        box6 = BoxLayout(orientation="vertical")
        label1 = Label(text="sagui 01")
        label2 = Label(text="05")
        label3 = Label(text="03")
        
        
        box6.add_widget(label1)
        #box6.add_widget(textinput1)
        box6.add_widget(label2)
        #box6.add_widget(textinput2)
        box6.add_widget(label3)
        #box6.add_widget(textinput3)
        #box6.add_widget(label4)
        
        box8.add_widget(box6)
        
        box7 = BoxLayout(orientation="vertical")
        label1 = Label(text="TEMPO DO TESTE: ")
        label2 = Label(text="HORA DE INICIO: ")
        label3 = Label(text="HORA DE TERMINO: ")
       

        box7.add_widget(label1)
        box7.add_widget(label2)
        box7.add_widget(label3)
        
        
        box8.add_widget(box7)
        
        box9 = BoxLayout(orientation="vertical")
        label1 = Label(text="1 minuto")
        label2 = Label(text="15:12:25")
        label3 = Label(text="15:13:25")
        
        box9.add_widget(label1)
        box9.add_widget(label2)
        box9.add_widget(label3)
        
        
        box8.add_widget(box9)
#quadrante 03        
        box10 = BoxLayout()
        label = Label(text="inserir script")
              
        
        box10.add_widget(label)
        
        box.add_widget(box10)
        
#quadrante 04         
        box11 = BoxLayout()
        box.add_widget(box11)
        
        
        
        
        box12 = BoxLayout(orientation="vertical")
        label1 = Label(text=" ")
        label2 = Label(text=" ")
        label3 = Label(text=" ")
        
        textinput = TextInput(text='', multiline=False)
        label4 = Label(text=" ")
        label5 = Label(text=" ")
        label6 = Label(text=" ")
        
        box12.add_widget(label1)
        box12.add_widget(label2)
        
        box12.add_widget(textinput)
        
        box12.add_widget(label5)
        box12.add_widget(label6)
        box10.add_widget(box12)
       
        box13 = BoxLayout(orientation="vertical")
        label1 = Label(text=" ")
        label2 = Label(text=" ")
        
        
        button = Button(text='Carregar')
        label4 = Label(text=" ")
        
        label5 = Label(text=" ")
        
        
        box13.add_widget(label1)
        box13.add_widget(label2)
        
        box13.add_widget(button)
        
        box13.add_widget(label4)
        box13.add_widget(label5)
        
        box10.add_widget(box13)
        
        box14 = BoxLayout(orientation="vertical")
        
        button1 = Button(text='Faltam 20 segundos')
        label2 = Label(text=" ")
        
        
        button2 = Button(text='Reiniciar Testes')
        label4 = Label(text=" ")
        
        button3 = Button(text='Sair')
        label5 = Label(text=" ")
        
        
       
        box14.add_widget(button1)
        box14.add_widget(label2)
        
        box14.add_widget(button2)
        box14.add_widget(label3)
        
        box14.add_widget(button3)
        box14.add_widget(label4)
        
        box11.add_widget(box14)

         
        
       
        return box
   
     
#metodo que roda o app    
Soinhos_Box().run()    
    