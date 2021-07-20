# Importing Libraries

import random
from tkinter import *

# Initializing Window

root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('Rock, Paper, Scissors')
root.config(bg = 'lightblue')

Label(root, text = 'Rock, Paper, Scissors', font = 'arial 20 bold', bg = 'lightblue').pack()

# User Choice

user_take = StringVar()

Label(root, text = 'choose any one: rock, paper, scissors', font = 'arial 15 bold', bg = 'lightblue').place(x = 20, y = 70)
Entry(root, font = 'arial 15', textvariable = user_take, bg = 'antiquewhite2').place(x = 90, y = 130)

# Computer Choice

comp_pick = random.randint(1,3)

if comp_pick == 1:
    comp_pick = 'rock'
elif comp_pick == 2:
    comp_pick = 'paper'
else:
    comp_pick = 'scissors'

# Function to Start Game

Result = StringVar()

def play():

    user_pick = user_take.get()

    if user_pick == comp_pick:
        Result.set('tie,you both select same')

    elif user_pick == 'rock' and comp_pick == 'paper':
        Result.set('you loose, computer select paper')

    elif user_pick == 'rock' and comp_pick == 'scissors':
        Result.set('you win, computer select scissors')

    elif user_pick == 'paper' and comp_pick == 'scissors':
        Result.set('you loose, computer select scissors')

    elif user_pick == 'paper' and comp_pick == 'rock':
        Result.set('you win, computer select rock')

    elif user_pick == 'scissors' and comp_pick == 'rock':
        Result.set('you loose, computer select rock')

    elif user_pick == 'scissors' and comp_pick == 'paper':
        Result.set('you win, computer select paper')

    else:
        Result.set('invalid: choose any one -- rock, paper, scissors')

# Reset Function

def Reset():

    Result.set("")
    user_take.set("")

# Exit Function

def Exit():
    
    root.destroy()

# Buttons

Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='antiquewhite2', width = 50,).place(x=25, y = 250)

Button(root, font = 'arial 13 bold', text = 'PLAY', padx =5, bg = 'lightblue', command = play).place(x=150, y=190)

Button(root, font = 'arial 13 bold', text = 'RESET', padx =5, bg = 'lightblue', command = Reset).place(x=70, y=310)

Button(root, font = 'arial 13 bold', text = 'EXIT', padx =5, bg = 'lightblue', command = Exit).place(x=230, y=310)



root.mainloop()