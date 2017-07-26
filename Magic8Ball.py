from random import randrange
from PIL import Image, ImageTk
from tkinter import *
import time, sys

FortuneList = ["As I see it , yes", "Ask again later", "Better not tell you now",
               "Cannot predict now", "Concentrate and ask again", "Don't count on it",
               "It is certain", "It is decidedly so", "Most likely", "My reply is no",
               "My sources say no", "Outlook is good", "Outlook not so good",
               "Reply hazy, try again", "Signs point to yes", "Very doubtful",
               "Without a doubt", "Yes", "Yes, definitely", "You may rely on it"]

userInput = ""
N = len(FortuneList)


class Example(Frame):
  
    def __init__(self,root):
        super().__init__()   
         
        self.initUI(root)
        
    def initUI(self,root):
        self.userString = StringVar()
        self.answerString = StringVar()

        self.master.title("Magic 8 Ball")
        self.pack(fill=BOTH, expand=True)
    
         
        self.label1 = Label(self, text= "Magic 8 Ball", width=15)
        self.label1.grid(row=0, column = 1 )

        self.label2 = Label(self, text= "Question: ", width=10)
        self.label2.grid(row=1, column =0, sticky= W)

        self.Entry2 = Entry(self)
        self.Entry2.grid(row=1, column = 1,columnspan= 2, sticky= W+E)

        self.label3 = Label(self, text= "Answer: ", width=10)
        self.label3.grid(row=2, column =0, sticky= W)
        
        self.label4 = Label(self, text='', width=10)
        self.label4.grid(row=2, column = 1,columnspan= 2, sticky= W+E)
              
        self.button1= Button(self, text="Ask",command =self.get_answer, fg ="Black", bg ="orange")
        self.button1.grid(row=3, column= 0)

        self.button1= Button(self, text="Clear", command= self.clear_question, fg ="Black", bg ="orange")
        self.button1.grid(row=3, column= 1)

        self.button1= Button(self, text="Quit",command=root.destroy, fg ="Black", bg ="orange")
        self.button1.grid(row=3, column= 2)

    def get_answer(self):
        self.label4['text']= FortuneList[randrange(0,N)]

    def clear_question(self):
        self.Entry2.delete(0, 'end')

    def close_window (root): 
        root.destroy()
        
def main():
  
    root = Tk()
    root.geometry("300x100+300+300")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  



