# importing the good stuff.
from tkinter import *
from PIL import ImageTk, Image  
import pyperclip
import random

# * Initializing the display windows and environment variabels.
root = Tk()
root.geometry('400x300')
pass_str = StringVar()
pass_len = IntVar()
pass_len.set("")
img = Image.open('C:\\Users\\almogb\\Desktop\\Python Portfolio\\Password Generator\\Pass.jpg')
bg = ImageTk.PhotoImage(img)
label = Label(root, image=bg)
root.resizable(False,False)
label.place(x = 0,y = 0)

# / Creating function to generate the random password.
def GeneratePassword():
    pw = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
        'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
        'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', 
        '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&', 
        '*', '(', ')']

# ! Declaring empty string to the password.    
    password = ''

# . Looping to generate the password with the length entered from the user.
    for x in range(pass_len.get()):
        password = password + random.choice(pw)

# - Setting the password to the entry widget.
    pass_str.set(password)

# : Creating function to copy the given password to the clipboard.
def CopyPassword():
    random_password = pass_str.get()
    pyperclip.copy(random_password)

# Creating the Headline.
Label(root, text = "Password Generator App", font = "Georgia 22 bold").pack()

# . Creating the first input from the user.
Label(root, text = "Enter the password length you want", font = "Georgia 10 bold").pack(pady = 3)
Entry(root, textvariable = pass_len).pack(pady = 3)

# * Creating the other buttons.
Button(root, text = "Generate Password", font = "Georgia 10 bold", command = GeneratePassword).pack(pady = 7)
Entry(root, textvariable=pass_str).pack(pady = 3)
Button(root, text = "Copy to clipboard", font = "Georgia 10 bold", command = CopyPassword).pack()

# Printing the credits.
Label(root,text ="Made By - Almog Beni", font = 'Georgia 10 bold', width = '20').pack(side = 'bottom')

# . Running the main loop.
root.mainloop()