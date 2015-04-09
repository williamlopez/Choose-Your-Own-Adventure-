 # Choose.py
# by [Marcos,William,Justin,Luis]
# Description: starter code for the Choose Your
# Own Adventure Project
#asdlf;j
# Import Statements
from tkinter import *
import tkinter.simpledialog
import tkinter.messagebox

root = Tk()
w = Label(root, text="Choose Your Own Adventure")
w.pack()

def intro():
    """ Introductory Function -> starts the story going """
    messagebox.showinfo("Title", "\nHello, you are a high schooler from Luisito High School. " + \
                        "You want to try out to a professional soccer club form Oregon like Timbers. Alright? ")
    choice = simpledialog.askinteger("Choose wisely",
                                   "Would you like to try out? (When 1 is 'yes' and 2 is 'no'). ")
    if choice == 1:
        choice1()
    elif choice == 2:
        choice2()
    else:
        intro()

################ Student A Functions #####################
def choice1():
    choice = simpledialog.askinteger("Choose wisely",
                                     "Eat appropriate food before training?  Now you must choose 1(Yes) or 2(No) again.")
    if (choice == 1):
        messagebox.showinfo("Yes",
                            "Training goes amazing! You're offered a spot on the team.")

    elif (choice == 2):
        messagebox.showinfo("No",
                            "Training goes bad, and you go back home.")
    else:
        choice1()

################ Student B Functions #####################
def choice2():
    choice = messagebox.showinfo("Bye Bye",
                                     "You will regret it!!!!!")



################ Main #####################
intro()

root.destroy()


