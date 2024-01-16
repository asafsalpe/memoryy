from tkinter import* #tkinter bibliotēka
from PIL import ImageTk, Image
import random
from tkinter import messagebox

gW=Tk()#logs
gW.title("Matching game")

bgImg=ImageTk.PhotoImage(Image.open('bgImg.jpg'))#fona attēls priekš visām kartītēm

count=0 #mainīgie
correctAnswers=0
answers=[]
answer_dict={}
answerCount=0

def btnClick(btn,number): #funkcija kartītes apgriešanai
    global count, correctAnswers, answers, answer_dict, answerCount
    if btn['image']=='pyimage1'and count<2: #ja kartīte nav apgriesta un apgriestas mazāk par 2 kartītēm
        btn['image']=ImageList[number]
        count+=1
        answers.append(number)
        answer_dict[btn]=ImageList[number]
    if len(answers)==2: #ja apgriestas 2 kartītes
        if ImageList[answers[0]]==ImageList[answers[1]]: #vai kartītes vienādas
            for key in answer_dict: #atspējot vienādās kartītes
                key['state']=DISABLED
            correctAnswers+=2
            if correctAnswers==2:# ja ir apgriestas vienādas kartītes
                messagebox.showinfo("Matching images", "Correct")
                correctAnswers=0
                answerCount+=1
            if answerCount==5: #ja pareizi atminētas visas 
                messagebox.showinfo("Congrats!", "You win!!!")
                reset()
        else: #ja apgrieztas dažādas kartītes
            messagebox.showinfo("Matching images","Incorrect")
            for key in answer_dict: #apgriest kartīti atpakaļ
                key['image']="pyimage1"
        count=0
        answers=[]
        answer_dict={}
    
    return 0

def reset(): #funkcija spēles sākšanai no jauna
    global count, correctAnswers, answers, answer_dict, answerCount
    btn0.config(state=NORMAL) #aktivizē visas pogas
    btn1.config(state=NORMAL)
    btn2.config(state=NORMAL)
    btn3.config(state=NORMAL)
    btn4.config(state=NORMAL)
    btn5.config(state=NORMAL)
    btn6.config(state=NORMAL)
    btn7.config(state=NORMAL)
    btn8.config(state=NORMAL)
    btn9.config(state=NORMAL)
    
    btn0["image"]="pyimage1"#nomaina visām pogām bildi uz fona attēlu
    btn1["image"]="pyimage1"
    btn2["image"]="pyimage1"
    btn3["image"]="pyimage1"
    btn4["image"]="pyimage1"
    btn5["image"]="pyimage1"
    btn6["image"]="pyimage1"
    btn7["image"]="pyimage1"
    btn8["image"]="pyimage1"
    btn9["image"]="pyimage1"

    count=0 #mainīgos atiestata
    correctAnswers=0
    answers=[]
    answer_dict={}
    answerCount=0
    random.shuffle(ImageList)

    return 0

def info(): #funkcija spēles noteikumiem
    gWs=Toplevel()#jauns logs
    gWs.title('Rules')
    gWs.geometry('710x170')#norāda loga parametrus
    desc=Label(gWs, text="Rules", font="Helvica 24 bold")
    desc.grid(row=0, column=0)
    desc=Label(gWs, text="The player turns over 2 cards", font="Helvica 14")
    desc.grid(row=1, column=0)
    desc=Label(gWs, text="If the pictures match, the cards stay overturned", font="Helvica 14")
    desc.grid(row=2, column=0)
    desc=Label(gWs, text="If they do not match the cards are turned over again, and the player tries again", font="Helvica 14")
    desc.grid(row=3, column=0)
    desc=Label(gWs, text="The game ends when the player has matched all cards", font="Helvica 14")
    desc.grid(row=4, column=0)
    return 0 

btn0=Button(width=150, height=150, image=bgImg, command=lambda:btnClick(btn0,0))#pogas
btn1=Button(width=150, height=150, image=bgImg, command=lambda:btnClick(btn1,1))
btn2=Button(width=150, height=150, image=bgImg, command=lambda:btnClick(btn2,2))
btn3=Button(width=150, height=150, image=bgImg, command=lambda:btnClick(btn3,3))
btn4=Button(width=150, height=150, image=bgImg, command=lambda:btnClick(btn4,4))
btn5=Button(width=150, height=150, image=bgImg, command=lambda:btnClick(btn5,5))
btn6=Button(width=150, height=150, image=bgImg, command=lambda:btnClick(btn6,6))
btn7=Button(width=150, height=150, image=bgImg, command=lambda:btnClick(btn7,7))
btn8=Button(width=150, height=150, image=bgImg, command=lambda:btnClick(btn8,8))
btn9=Button(width=150, height=150, image=bgImg, command=lambda:btnClick(btn9,9))

btn0.grid(row = 0, column = 0)#pogu novietojums
btn1.grid(row = 0, column = 1)
btn2.grid(row = 0, column = 2)
btn3.grid(row = 0, column = 3)
btn4.grid(row = 0, column = 4)
btn5.grid(row = 1, column = 0)
btn6.grid(row = 1, column = 1)
btn7.grid(row = 1, column = 2)
btn8.grid(row = 1, column = 3)
btn9.grid(row = 1, column = 4)

myImg1=ImageTk.PhotoImage(Image.open("bmw.jpg").resize((150,150)))#bildes pogām
myImg2=ImageTk.PhotoImage(Image.open("honda.jpg").resize((150,66)))
myImg3=ImageTk.PhotoImage(Image.open("merc.jpg").resize((150,150)))
myImg4=ImageTk.PhotoImage(Image.open("porsch.jpg").resize((150,58)))
myImg5=ImageTk.PhotoImage(Image.open("skoda.jpg").resize((150,114)))

ImageList=[myImg1,myImg1,myImg2,myImg2,myImg3,myImg3,myImg4,myImg4,myImg5,myImg5]#iedala katrai pogai bildi 
random.shuffle(ImageList)

mainMenu=Menu(gW)#izvēlne
gW.config(menu=mainMenu)

options=Menu(mainMenu, tearoff=False)#izvēlne
mainMenu.add_cascade(label="Options", menu=options)

options.add_command(label="New game", command=reset)# sākt no jauna un aizvērt
options.add_command(label="Exit", command=gW.quit)

mainMenu.add_command(label="About", command=info)#noteikumi

gW.mainloop()