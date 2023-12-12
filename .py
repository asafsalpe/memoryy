from tkinter import*
from PIL import ImageTk, Image
import random
from tkinter import messagebox
gameWindow=Tk()
gameWindow.title("Memory game")

bgImg=ImageTk.PhotoImage(Image.open('bgImg.jpg'))

btn0=Button(width=150, height=150, image=bgImg)
btn1=Button(width=150, height=150, image=bgImg)
btn2=Button(width=150, height=150, image=bgImg)
btn3=Button(width=150, height=150, image=bgImg)
btn4=Button(width=150, height=150, image=bgImg)
btn5=Button(width=150, height=150, image=bgImg)
btn6=Button(width=150, height=150, image=bgImg)
btn7=Button(width=150, height=150, image=bgImg)
btn8=Button(width=150, height=150, image=bgImg)
btn9=Button(width=150, height=150, image=bgImg)

btn0.grid(row = 0, column = 0)
btn1.grid(row = 0, column = 1)
btn2.grid(row = 0, column = 2)
btn3.grid(row = 0, column = 3)
btn4.grid(row = 0, column = 4)
btn5.grid(row = 1, column = 0)
btn6.grid(row = 1, column = 1)
btn7.grid(row = 1, column = 2)
btn8.grid(row = 1, column = 3)
btn9.grid(row = 1, column = 4)

myImg1=ImageTk.PhotoImage(Image.open("bmw.jpg").resize((150,150)))
myImg2=ImageTk.PhotoImage(Image.open("honda.jpg").resize((150,150)))
myImg3=ImageTk.PhotoImage(Image.open("merc.jpg").resize((150,150)))
myImg4=ImageTk.PhotoImage(Image.open("porsch.jpg").resize((150,150)))
myImg5=ImageTk.PhotoImage(Image.open("skoda.jpg").resize((150,150)))

gameWindow.mainloop()
