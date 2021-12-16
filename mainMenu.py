from tkinter import *

class mainpg:
    def __init__(self, window):
        self.mainLabel = Label(window,
                               text="We're Really Not Strangers",
                               font=("Comic Sans MS", 35, "bold"),
                               pady=70,
                               bg='#b81f1f'
                               # fg='Red'
                               )
        self.mainLabel.pack()

        self.label2 = Label(window, font=("Comic Sans MS", 24), bg='#b81f1f', text="pick a level:")
        self.label2.pack()

        self.btn1 = Button(window, font=("Comic Sans MS", 17), text="Level 1: Perception", pady=10,
                           command=self.perception)
        self.btn1.pack()
        self.btn2 = Button(window, font=("Comic Sans MS", 17), text="Level 2: Connection", pady=10,
                           command=self.connection)
        self.btn2.pack()
        self.btn3 = Button(window, font=("Comic Sans MS", 17), text="Level 3: Refelction", pady=10,
                           command=self.reflection)
        self.btn3.pack()

    def perception(self):
        window.destroy()
        import perceptionpg

    def connection(self):
        window.destroy()
        import connectionpg

    def reflection(self):
        window.destroy()
        import reflectionpg


window = Tk()

window.title("Welcome")
window.geometry("700x500")  # width x height
# window.config(bg=rgb_hack((255, 0, 122))) # suppose to change background color
window.config(bg='#b81f1f')
window1=mainpg(window)
window.mainloop()
