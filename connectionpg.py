import random
from tkinter import *

FILENAME='connection.txt'

window = Tk()
choice = ["Level 1: Perception", "Level 2: Connections", "Level 3: Reflection", "Final Card"]




class Perception:
    def __init__(self, window):
        self.l1 = Label(window, font=("Comic Sans MS", 35), text="Level 2: Connection", pady=25, bg='#b81f1f')
        self.l1.pack()
        self.changelvlB = Button(window, font=("Comic Sans MS", 12), text="Change Level")
        self.changelvlB.place(x=2000, y=25)
        self.changelvlB.pack()

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
        question=Label(window, font=("Comic Sans MS", 16), text=q)
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

    def submitLevel(self, variable):
        #newLvl = ""
        if variable.get() == choice[0]:
            newLvl="perception"
            Perception.perception
        elif variable.get() == choice[1]:
            newLvl="connection"
            Perception.connection
        elif variable.get() == choice[2]:
            newLvl="reflection"
            Perception.reflection
        elif variable.get() == choice[3]:
            newLvl="finalCard"
            Perception.finalCard
        #return newLvl
        
        #newQb=Button(window, font=("Comic Sans MS", 12), text="Submit", command=newLvl).pack()
    



#choice = ["Level 1: Perception", "Level 2: Connections", "Level 3: Reflection", "Final Card"]

variable = StringVar(window)
variable.set("Select Level")

dropdown = OptionMenu(
    window,
    variable,
    *choice
    )
dropdown.pack()

window.title("Level 2: Connection")
window.geometry("700x500")  # width x height
# window.config(bg=rgb_hack((255, 0, 122))) # suppose to change background color
window.config(bg='#b81f1f')
window1 = Perception(window)

flag = True
while flag:
    q = window1.openFile2()
    window1.printQ(q)
    newQb=Button(window, font=("Comic Sans MS", 12), text="New Question", command=window1.openFile2())
    #newQb.place(y=-300)
    newQb.pack()
    #lvlSwitch = "window1.".append(window1.submitLevel(variable))
   #print(lvlSwitch)
    #switchBtn=Button(window, font=("Comic Sans MS", 12), text="Submit", command=lvlSwitch).pack()
    flag=False

window.mainloop()


