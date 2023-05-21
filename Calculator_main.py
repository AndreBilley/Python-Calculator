import time
import sys
from time import sleep
from Formatting_functions import time_print
from Formatting_functions import delay_print
from Formatting_functions import menu_list
from Formatting_functions import clear
from Calculator_operations import Quadratic
from Calculator_operations import Basic_Operations
from Calculator_operations import bo
#from termcolor import colored, cprint
run = True
while run:
    def menu():
        global run
        time_print ("----------\n", 0.01)
        time_print ("Casio\n", 0.01)
        time_print ("----------\n", 0.01)
        options = ['Add', 'Subtract', 'Multiply', 'Divide', 'Quadratics', "Exit"]
        opt = menu_list(options)
        
        if opt == "Add":
            clear()
            bo.add()
        if opt == "Subtract":
            clear()
            bo.sub()
        if opt == "Multiply":
            clear()
            bo.mult()
        if opt == "Divide":
            clear()
            bo.div()
        if opt == "Quadratics":
            clear()
            Quadratic.quad_menu()
        if opt == "Exit":
            clear()
            run = False      
    menu()

