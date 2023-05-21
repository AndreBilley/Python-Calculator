import time
import sys
from time import sleep
from Formatting_functions import time_print
from Formatting_functions import delay_print
from Formatting_functions import menu_list
from Formatting_functions import clear

class Quadratic():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    

        

    def roots(self):
        self.a = int(input("ax² = "))
        self.b = int(input("bx = "))
        self.c = int(input("c = "))
        point_a = (-1*self.b + (self.b**2-4*self.a*self.c)**0.5) / 2*self.a
        point_b = (-1*self.b - (self.b**2-4*self.a*self.c)**0.5) / 2*self.a
        print('x1 = ', point_a, ' x2 = ', point_b)

    def turning_points(self):
        self.a = int(input("ax² = "))
        self.b = int(input("bx = "))
        self.c = int(input("c = "))
        point_a = self.b / 2
        point_b = self.c - point_a**2
        print('x1 = ', point_a, ' x2 = ', point_b)

    def quad_menu():
        options = ['Roots', 'Turning Points']
        opt = menu_list(options)
        if opt == "Roots":
            clear()
            q.roots()
        if opt == "Turning Points":
            clear()
            q.turning_points()
            
            
class Basic_Operations:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    
    def add(self):
        sleep(0.5)
        self.n1 = int(input("Enter first number > "))
        self.n2 = int(input("Enter second number > "))
        sleep(0.5)
        print (self.n1+self.n2)

    def sub(self):
        sleep(0.5)
        self.n1 = int(input("Enter first number > "))
        self.n2 = int(input("Enter second number > "))
        sleep(0.5)
        print (self.n1-self.n2)

    def mult(self):
        sleep(0.5)
        self.n1 = int(input("Enter first number > "))
        self.n2 = int(input("Enter second number > "))
        sleep(0.5)
        print (self.n1*self.n2)

    def div(self):
        sleep(0.5)
        self.n1 = int(input("Enter first number > "))
        self.n2 = int(input("Enter second number > "))
        sleep(0.5)
        print (self.n1/self.n2)
        
bo = Basic_Operations(0,0)        
q = Quadratic(0, 0, 0)