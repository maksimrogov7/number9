from tkinter import *
import random

def abc():
    can3.delete("all")
    a=random.randint(1, 3)
    if a==1:
        can3.create_oval(275, 100,  375, 200, fill='yellow')
    elif a==2:
        can3.create_rectangle(250, 100, 350, 200, fill='green')
    elif a==3:
        can3.create_polygon(250, 100,  350, 200, 350, 100, fill='red')
        
    

root = Tk()
root.title('Rogov Maxim')
root.geometry('900x600')
root.resizable(False, False)


Button(root, bg = 'magenta', text = 'Создать фигуру', command = abc).place(x=450, y=25, anchor= CENTER)
can3 = Canvas(root, width=700, height=500)
can3.place(x=450, y=500, anchor=CENTER)




root.mainloop()
