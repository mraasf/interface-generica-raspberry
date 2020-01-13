from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

#hardware

left = 16
right = 18

win = Tk()
win.title("marmoset box")

#functions of buttons

def ledToggle():
    if left.is_lit:
     left.off()
     leftButton["text"] = "on"
    else:
     left.on()
     leftButton["text"] = "Off"
# widgets
leftButton = Button(win, text="ON" ,command = ledToggle)
leftButton.grid(row=0, column=1)