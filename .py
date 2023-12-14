from tkinter import*
from PIL import ImageTk, Image
import random
from tkinter import messagebox
gameWindow=Tk()
gameWindow.title("Matching game")

bgImg=ImageTk.PhotoImage(Image.open('bgImg.jpg'))

count=0
correctAnswers=0
answers=[]
answer_dict={}

def btnClick(btn,number):
    global count, correctAnswers, answers, answer_dict
    if btn['image']=='pyimage1'and count<2:
        btn['image']=ImageList[number]
        count+=1
        answers.append(number)
        answer_dict[btn]=ImageList[number]
    if len(answers)==2:
        if ImageList[answers[0]]==ImageList[answers[1]]:
            for key in answer_dict:
                key['state']=DISABLED
            if correctAnswers==2:
                messagebox.showinfo("Matching images", "You've guessed correctly")
            else:
                messagebox.showinfo("No matching images","You've guessed incorrectly")
                for key in answer_dict:
                    key['image']="pyimage6"
                count=0
                answers=[]
                answer_dict={}

                return 0

btn0=Button(width=150, height=150, image=bgImg, command=lambda:btnClick(btn0,0))
btn1=Button(width=150, height=150, image=bgImg, command=lambda:btnClick(btn1,1))
btn2=Button(width=150, height=150, image=bgImg, command=lambda:btnClick(btn2,2))
btn3=Button(width=150, height=150, image=bgImg, command=lambda:btnClick(btn3,3))
btn4=Button(width=150, height=150, image=bgImg, command=lambda:btnClick(btn4,4))
btn5=Button(width=150, height=150, image=bgImg, command=lambda:btnClick(btn5,5))
btn6=Button(width=150, height=150, image=bgImg, command=lambda:btnClick(btn6,6))
btn7=Button(width=150, height=150, image=bgImg, command=lambda:btnClick(btn7,7))
btn8=Button(width=150, height=150, image=bgImg, command=lambda:btnClick(btn8,8))
btn9=Button(width=150, height=150, image=bgImg, command=lambda:btnClick(btn9,9))

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

myImg1=ImageTk.PhotoImage(Image.open("bmw.jpg").resize((100,100)))
myImg2=ImageTk.PhotoImage(Image.open("honda.jpg").resize((100,100)))
myImg3=ImageTk.PhotoImage(Image.open("merc.jpg").resize((100,100)))
myImg4=ImageTk.PhotoImage(Image.open("porsch.jpg").resize((100,100)))
myImg5=ImageTk.PhotoImage(Image.open("skoda.jpg").resize((100,100)))

ImageList=[myImg1,myImg1,myImg2,myImg2,myImg3,myImg3,myImg4,myImg4,myImg5,myImg5]
random.shuffle(ImageList)

gameWindow.mainloop()
