import random
from tkinter import *
from tkinter import ttk
#from tkinter import tk

FILENAME='connection.txt'

window = Tk()
choice = ["Select Level", "Level 1: Perception", "Level 2: Connections", "Level 3: Reflection", "Final Card"]


class Connection:
    def __init__(self, window):
        self.l1 = Label(window, font=("Comic Sans MS", 35), text="Level 2: Connection", pady=25, bg='#b81f1f').pack()
        self.q = Connection.openFile2(self)
        self.questionLbl = Label(window, font=("Comic Sans MS", 12), text=self.q, padx=15, pady=25, bg='#b81f1f').pack()
        #self.newQBtn = Button(window,)

        '''
        self.choice = ["Level 1: Perception", "Level 2: Connections", "Level 3: Reflection", "Final Card"]

        self.variable = StringVar(window)
        self.variable.set("Select Level")

        self.dropdown = OptionMenu(
            window,
            self.variable,
            *self.choice
        )
        self.dropdown.pack()
        '''

        #Perception.submitLevel(self.variable)
        


    def openFile2(self):
        f = open(FILENAME, 'r')
        #print(random.choice(list(f)))
        questiontxt = random.choice(list(f))
        #question=Label(window, font=("Comic Sans MS", 16), text=questiontxt)
        #question.pack()
        f.close()
        return questiontxt
        '''
        newQb=Button(window, font=("Comic Sans MS", 12), text="New Question", command=Perception.openFile2)
        if newQb.pack():
            Perception.openFile2
        '''

    def printQ(self, q):
        question=Label(window, font=("Comic Sans MS", 16), text=q, bg="#b81f1f")
        question.pack()

    def mainpg(self):
        window.destroy()
        import mainMenu

    def connection(self):
        window.destroy()
        import connectionpg

    def reflection(self):
        window.destroy()
        import reflectionpg
    
    def perception(self):
        window.destroy()
        import perceptionpg

    
    def finalCard(self):
        window.destroy()
        import finalpg

    #def newQuestionCmd(self):



    def submitLevel(self, e):
        if my_combo.get() == choice[1]:
            newQ = Connection.openFile2(self)
            #self.questionLbl.configure(text=newQ)
            self.questionLbl["text"]=newQ
            #self.questionLbl.set(newQ)
        elif my_combo.get() == choice[2]:
            Connection.connection(self)
        elif my_combo.get() == choice[3]:
            Connection.reflection(self)
        elif my_combo.get() == choice[4]:
            Connection.finalCard(self)   
        else:
            pass 
    

#choice = ["Level 1: Perception", "Level 2: Connections", "Level 3: Reflection", "Final Card"]
'''
variable = StringVar(window)
variable.set("Select Level")

dropdown = OptionMenu(
    window,
    variable,
    *choice
    )
dropdown.pack()
'''
#my_combo = ttk.Combobox(window, value=choice).pack(padx=200)

window.title("Level 2: Connection")
window.geometry("700x500")  # width x height
# window.config(bg=rgb_hack((255, 0, 122))) # suppose to change background color
window.config(bg='#b81f1f')
window1 = Connection(window)

flag = True
#while flag:
    #q = window1.openFile2()
    #window1.printQ(q)
    #question=Label(window, font=("Comic Sans MS", 16), text=q, bg="#b81f1f")
    #question.pack()
    #newQb=Button(window, font=("Comic Sans MS", 12), text="New Question", command=window1.openFile2())
    #newQb.place(y=-300)
    #newQb.pack()
    #lvlSwitch = "window1.".append(window1.submitLevel(variable))
   #print(lvlSwitch)
    #switchBtn=Button(window, font=("Comic Sans MS", 12), text="Submit", command=lvlSwitch).pack()
    #flag=False

l2 = Label(window, font=("Comic Sans MS", 17), text="Change Level", padx=20, pady=10, bg='#b81f1f').pack()
# create dropdown menu
my_combo = ttk.Combobox(window, value=choice)
my_combo.current(0)
my_combo.pack()

#bind drop down menu
my_combo.bind("<<ComboboxSelected>>", window1.submitLevel)

window.mainloop()


