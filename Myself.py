#Marc Steven Marquez, A121
from tkinter import Tk, Label, PhotoImage, LEFT, RIGHT, RIDGE
root = Tk()

text = Label(root,
             font=('Arial', 16, 'bold'),
             foreground='black',
             background='purple',
             pady=12,
             text='Marc Steven Quiachon Marquez \n Davao City, June 2002 ')
text.pack(side=RIGHT)

me = PhotoImage(file='superdog.gif')
meLabel = Label(root,
                borderwidth=5,
                relief=RIDGE,
                image=me,)
meLabel.pack(side=LEFT)

root.mainloop()