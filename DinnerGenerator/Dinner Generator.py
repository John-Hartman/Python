class Dinner:
    def __init__(self,name,ingredients,prepTime):
        self.name=name
        self.ingredients=ingredients
        self.prepTime=prepTime
    def myfunc(self):
        print(self.name+'\n'+self.ingredients+'\n'+self.prepTime)
p1=Dinner("Chicken Alfredo: ",'noodles, chicken, alfredo sauce',"1 hour")
p2=Dinner('Chilli: ','beans, meat, tomato sauce','6 hours')
p3=Dinner("Pulled Pork: ",'pork chuck, root beer, barbecue sauce','8 hours')
p4=Dinner('Spaghetti: ','noodles, marinara, beef,','30 minutes')
p5=Dinner('Grilled Cheese & Tomato soup: ', 'bread, cheese, butter, tomato soup, milk','30 minutes')
p6=Dinner('Stir fry: ','rice, chicken, broccoli, soy sauce, teriyaki','1 hour')
print(p1.myfunc(),p2.myfunc(),p3.myfunc(),p4.myfunc(),p5.myfunc(),p6.myfunc())

Dinner=['alfredo','chilli','pulledPork','spaghetti','grilled cheese','stir fry']
import random

for x in random.choices(Dinner):
    if x=='alfredo':
        print(p1.myfunc())
    elif x =='chilli':
        print(p2.myfunc())
    elif x=='pulledPork':
        print(p3.myfunc())
    elif x=='spaghetti':
        print(p4.myfunc())
    elif x=='grilled cheese':
        print(p5.myfunc())
    elif x=='stir fry':
        print(p6.myfunc())
