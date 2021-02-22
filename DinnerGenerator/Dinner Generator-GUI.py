import tkinter as tk
import random
import pandas

class Dinner:
    def __init__(self,name,ingredients,prepTime):
        self.name=name
        self.ingredients=ingredients
        self.prepTime=prepTime
        
p1=Dinner("Chicken Alfredo: ",'noodles, chicken, alfredo sauce',"1 hour")
p2=Dinner('Chilli: ','beans, meat, tomato sauce','6 hours')
p3=Dinner("Pulled Pork: ",'pork chuck, root beer, barbecue sauce','8 hours')
p4=Dinner('Spaghetti: ','noodles, marinara, beef,','30 minutes')
p5=Dinner('Grilled Cheese & Tomato soup: ', 'bread, cheese, butter, tomato soup, milk','30 minutes')
p6=Dinner('Stir fry: ','rice, chicken, broccoli, soy sauce, teriyaki','1 hour')    


def myfunc(self):
        print(self.name+'\n'+self.ingredients+'\n'+self.prepTime)


Dinner=['alfredo','chilli','pulledPork','spaghetti','grilled cheese','stir fry']

def generator():
    for x in random.choices(Dinner):
        if x=='alfredo':
            txt_block.write(p1.myfunc())
        elif x =='chilli':
            txt_block.write(p2.myfunc())
        elif x=='pulledPork':
            txt_block.write(p3.myfunc())
        elif x=='spaghetti':
            txt_block.write(p4.myfunc())
        elif x=='grilled cheese':
            txt_block.write(p5.myfunc())
        elif x=='stir fry':
            txt_block.write(p6.myfunc())
        



window = tk.Tk()
window.title("Dinner Generator")
window.rowconfigure(0, minsize=600, weight=1)
window.columnconfigure(1, minsize=600, weight=1)

txt_block = tk.Text(window, bg="#252525", fg="#FFFFFF")
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2, bg="#151515")
btn_pick = tk.Button(fr_buttons, text="Open", command=generator, bg="#252525", fg="#FFFFFF")


btn_pick.grid(row=0, column=0, sticky="ew", padx=5, pady=5)


fr_buttons.grid(row=0, column=0, sticky="ns")
txt_block.grid(row=0, column=1, sticky="nsew")

window.mainloop()