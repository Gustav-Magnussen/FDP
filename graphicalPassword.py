import tkinter as tk
import os
import sys

userNames = ['bob', 'john']

#Hardcoded sample passwords for user john and bob
bobPassword = ['0grey', '10grey', '12grey', '15grey', '3grey', '5grey', '6grey', '9grey']
johnPassword = ['0grey', '11grey', '12grey', '13grey', '14grey', '15grey', '1grey', '2grey', '3grey', '4grey', '7grey', '8grey']

#Start tkinter window
window = tk.Tk()

buttonValues = []

def reset():
    """
    Resets the user entry.
    """
    python = sys.executable
    os.execl(python, python, * sys.argv)

def change(button):
    """
    Gets state of buttons and stores in buttonvalues.
    """
    colour = 'white'
    if buttons[button]['bg'] == 'white':
        buttons[button].configure(bg='grey')
        colour = 'grey'
    else:
        pass
    buttons[button].configure(state='disabled')
    
    nrButton = str(button)
    value = nrButton + colour
    
    buttonValues.append(value)

def getUserName():
    """
    Gets username from user entry.
    """
    username = userEntry.get()
    return username
    

def loginSuccess():
    """'
    Opens and displayes the success login window.
    """
    window.destroy()
    successWindow = tk.Tk()
    tk.Label(successWindow, padx=10, pady=10, font=("Arial", 20), text='Login successfull').pack()

def graphicalCheck(name):
    """
    Takes username, checks against user graphical password.
    """
    buttonValues.sort()
    if name == 'bob':
        if buttonValues == bobPassword:
            output = 1
        else:
            output = 0
    elif name == 'john':
        if buttonValues == johnPassword:
            output = 1
        else:
            output = 0
    else:
        output = 0
        
    return output
    
def usernameClick():
    """
    Checks if username password combo is correct.
    """
    userName = getUserName()
    if userName in userNames:
        if graphicalCheck(userName) == 1:
            loginSuccess()
        else:
            wrongInput.grid(column= 1, row=9)   
    else:
        wrongInput.grid(column= 1, row=9)
        

#Frames
frameUser = tk.Canvas(window, width=300, height=100)
frameUser.grid(columnspan=3)

framePassword = tk.Canvas(window, width=10, height=10)
framePassword.grid(columnspan=4)



tk.Label(frameUser, font=('Arial', 12), text='Login Form').grid(column= 0, row=0, columnspan=2)
tk.Label(frameUser, font=('Arial', 10), text='Username:').grid(column=0, row=1, sticky='e')


#entry block
content = tk.StringVar()
userEntry = tk.Entry(frameUser, width=10)
userEntry.grid(column=1, row=1, columnspan=3, sticky='w')

#graphical password buttons

aaBtn = tk.Button(framePassword, width=2, height=1, bg='white', command = lambda: change(0))
aaBtn.grid(column=0, row=4, sticky='nse')
abBtn = tk.Button(framePassword, width=2, height=1, bg='white', command = lambda: change(1))
abBtn.grid(column=1, row=4, sticky='nsew')
acBtn = tk.Button(framePassword, width=2, height=1, bg='white', command = lambda: change(2))
acBtn.grid(column=2, row=4, sticky='nsew')
adBtn = tk.Button(framePassword, width=2, height=1, bg='white', command = lambda: change(3))
adBtn.grid(column=3, row=4, sticky='nsew')

baBtn = tk.Button(framePassword, width=2, height=1, bg='white', command = lambda: change(4))
baBtn.grid(column=0, row=5, sticky='nse')
bbBtn = tk.Button(framePassword, width=2, height=1, bg='white', command = lambda: change(5))
bbBtn.grid(column=1, row=5, sticky='nsew')
bcBtn = tk.Button(framePassword, width=2, height=1, bg='white', command = lambda: change(6))
bcBtn.grid(column=2, row=5, sticky='nsew')
bdBtn = tk.Button(framePassword, width=2, height=1, bg='white', command = lambda: change(7))
bdBtn.grid(column=3, row=5, sticky='nsew')

caBtn = tk.Button(framePassword, width=2, height=1, bg='white', command = lambda: change(8))
caBtn.grid(column=0, row=6, sticky='nse')
cbBtn = tk.Button(framePassword, width=2, height=1, bg='white', command = lambda: change(9))
cbBtn.grid(column=1, row=6, sticky='nsew')
ccBtn = tk.Button(framePassword, width=2, height=1, bg='white', command = lambda: change(10))
ccBtn.grid(column=2, row=6, sticky='nsew')
cdBtn = tk.Button(framePassword, width=2, height=1, bg='white', command = lambda: change(11))
cdBtn.grid(column=3, row=6, sticky='nsew')

daBtn = tk.Button(framePassword, width=2, height=1, bg='white', command = lambda: change(12))
daBtn.grid(column=0, row=7, sticky='nse')
dbBtn = tk.Button(framePassword, width=2, height=1, bg='white', command = lambda: change(13))
dbBtn.grid(column=1, row=7, sticky='nsew')
dcBtn = tk.Button(framePassword, width=2, height=1, bg='white', command = lambda: change(14))
dcBtn.grid(column=2, row=7, sticky='nsew')
ddBtn = tk.Button(framePassword, width=2, height=1, bg='white', command = lambda: change(15))
ddBtn.grid(column=3, row=7, sticky='nsew')

#List of graphical password buttons
buttons = [aaBtn, abBtn, acBtn, adBtn, baBtn, bbBtn, bcBtn, bdBtn, caBtn, cbBtn, ccBtn, cdBtn, daBtn, dbBtn, dcBtn, ddBtn]

#Button for submitting username query to database
submitBtn = tk.Button(text='Submit',width=5,height=1, padx=10, command=usernameClick)
submitBtn.grid(column=0, row=8, sticky='e')

#Button for reseting user entry
resetBtn = tk.Button(text='Reset entries',width=6,height=1, padx=10, command=reset)
resetBtn.grid(column=1, row=8, sticky='w')
wrongInput = tk.Label(font=("Arial", 12), text='Wrong Username/password')

window.mainloop()


