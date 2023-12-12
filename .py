from tkinter import*
from PIL import ImageTk, Image
import random
gameWindow=Tk()
gameWindow.title("Memory game")

bgImg=ImageTk.PhotoImage(Image.open('skoda.jpg'))

btn0=Button(width=20, height=10, image=bgImg)
btn1=Button(width=20, height=10)
btn2=Button(width=20, height=10)
btn3=Button(width=20, height=10)
btn4=Button(width=20, height=10)
btn5=Button(width=20, height=10)
btn6=Button(width=20, height=10)
btn7=Button(width=20, height=10)
btn8=Button(width=20, height=10)
btn9=Button(width=20, height=10)

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

myImg1=ImageTk.PhotoImage(Image.open("bmw.png"))
myImg2=ImageTk.PhotoImage(Image.open("honda.jpg"))
myImg3=ImageTk.PhotoImage(Image.open("merc.jpg"))
myImg4=ImageTk.PhotoImage(Image.open("porsch.png"))
myImg5=ImageTk.PhotoImage(Image.open("skoda.jpg"))

gameWindow.mainloop()
