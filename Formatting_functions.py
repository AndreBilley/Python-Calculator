import time
import sys
from time import sleep

def time_print(s, t):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(t)
        
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.035)
        
delete = "\033[A                                                       \033[A"
enter = (" ▾")
        
        
#####################-Menu List-############################
def menu_list(options):
    num_of_options = 0
    option_list = []
    for x in options:
        num_of_options += 1    # records number of options
        str_option = str(num_of_options) # converts to string
        option_list.append(str_option)   # adds option to list
        
        str_option = ("[" + str_option + "]")
        print (
            str_option,
            x.title(),
            )
        time.sleep(0.05)

    temp_choice = input("\nEnter a digit to continue: ")
    while not temp_choice in option_list:  #while the input is not in the list
        print(delete)
        end = ''
        time_print(("CHOOSE A VALID OPTION!") + end, 0.001)
        input(enter)
        print(delete)
        print(delete)
        temp_choice = input("\nEnter a digit to continue: ")

    #converts the input digit to string option
    temp_choice = int(temp_choice)
    opt = options[temp_choice - 1]

    return opt

########################-Clear-#########################
from subprocess import call
from os import name


def clear(permanent_text=[]):
    call("clear" if name == "posix" else "cls", shell=True)
    if permanent_text:
        for x in permanent_text:
            print(str(x))
#########################################################