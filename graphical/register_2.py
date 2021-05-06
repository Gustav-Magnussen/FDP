import tkinter as tk
import os
import sys
import sqlite3
import argon2

ph = argon2.PasswordHasher()

buttonValues = []

checkValues = []

#Connection to database
connect = sqlite3.connect('users.db')

cr = connect.cursor()

command = """CREATE TABLE IF NOT EXISTS
users(user_id INTEGER PRIMARY KEY, username TEXT, password TEXT)"""
cr.execute(command)


def change(button):
    """
    State of clickable buttons.
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

def checkUsername(username):
    """
    Checks if username is available.
    """
    
    cr.execute("SELECT username FROM USERS")
    
    usernames = cr.fetchall()
    for row in usernames:
        for names in row:
            if names == username:
                wrongInput.grid(column= 1, row=15)
                username = None
    return username

def changeCheck(button):
    """
    State of clickable check buttons.
    """
    colour = 'white'
    if buttonsCheck[button]['bg'] == 'white':
        buttonsCheck[button].configure(bg='grey')
        colour = 'grey'
    else:
        pass
    buttonsCheck[button].configure(state='disabled')
    
    nrButton = str(button)
    value = nrButton + colour
    checkValues.append(value)

def getUserName():
    """
    Gets username from user entry.
    """
    username = userEntry.get()
    return username
    

def click():
    userName = getUserName()
    buttonValues.sort()
    checkValues.sort()
    condition = 0
    if buttonValues == checkValues:
        values =  ''.join(buttonValues)
        username = checkUsername(userName)
        while True:   
            if username != None:
                if userName == username:
                    hash = ph.hash(values)
                    try:
                        ph.verify(hash, values)
                        condition = 1
                        break
                    except:
                        pass
                   
            else:
                wrongInput.grid(column= 1, row=15)
                break
        if condition == 1:
            cr.execute("INSERT INTO users (username, password) VALUES (?,?)",(userName, hash))
            connect.commit()
            window.destroy()
        else:
            wrongInput.grid(column= 1, row=15)
    else:
        wrongInput.grid(column= 1, row=15)
    
   
    

def reset():
    """
    Resets the user entry by restarting the program.
    """
    os.execl(sys.executable, sys.executable, *sys.argv)
    
window = tk.Tk()
window.geometry("300x400")

tk.Label(font=('Arial', 10), text='Register a new user', padx=10, pady=10).grid(columnspan=2, row=0, sticky='n')

frameUser = tk.Canvas(window, width=300, height=100)
frameUser.grid(columnspan=3)

framePassword1 = tk.Canvas(window, width=10, height=10)
framePassword1.grid(columnspan=4)


frameLabel = tk.Canvas(window, width=10, height=1)
frameLabel.grid(columnspan=2)

framePassword2 = tk.Canvas(window, width=10, height=10)
framePassword2.grid(columnspan=4)

tk.Label(frameUser, font=('Arial', 10), text='Username:', padx=10, pady=10).grid(column=0, row=2, sticky='e')

content = tk.StringVar()
userEntry = tk.Entry(frameUser, width=10)
userEntry.grid(column=1, row=2, columnspan=3, sticky='w')

aaBtn = tk.Button(framePassword1, width=2, height=1, bg='white', command = lambda: change(0))
aaBtn.grid(column=0, row=4, sticky='nse')
abBtn = tk.Button(framePassword1, width=2, height=1, bg='white', command = lambda: change(1))
abBtn.grid(column=1, row=4, sticky='nsew')
acBtn = tk.Button(framePassword1, width=2, height=1, bg='white', command = lambda: change(2))
acBtn.grid(column=2, row=4, sticky='nsew')
adBtn = tk.Button(framePassword1, width=2, height=1, bg='white', command = lambda: change(3))
adBtn.grid(column=3, row=4, sticky='nsew')

baBtn = tk.Button(framePassword1, width=2, height=1, bg='white', command = lambda: change(4))
baBtn.grid(column=0, row=5, sticky='nse')
bbBtn = tk.Button(framePassword1, width=2, height=1, bg='white', command = lambda: change(5))
bbBtn.grid(column=1, row=5, sticky='nsew')
bcBtn = tk.Button(framePassword1, width=2, height=1, bg='white', command = lambda: change(6))
bcBtn.grid(column=2, row=5, sticky='nsew')
bdBtn = tk.Button(framePassword1, width=2, height=1, bg='white', command = lambda: change(7))
bdBtn.grid(column=3, row=5, sticky='nsew')

caBtn = tk.Button(framePassword1, width=2, height=1, bg='white', command = lambda: change(8))
caBtn.grid(column=0, row=6, sticky='nse')
cbBtn = tk.Button(framePassword1, width=2, height=1, bg='white', command = lambda: change(9))
cbBtn.grid(column=1, row=6, sticky='nsew')
ccBtn = tk.Button(framePassword1, width=2, height=1, bg='white', command = lambda: change(10))
ccBtn.grid(column=2, row=6, sticky='nsew')
cdBtn = tk.Button(framePassword1, width=2, height=1, bg='white', command = lambda: change(11))
cdBtn.grid(column=3, row=6, sticky='nsew')

daBtn = tk.Button(framePassword1, width=2, height=1, bg='white', command = lambda: change(12))
daBtn.grid(column=0, row=7, sticky='ne')
dbBtn = tk.Button(framePassword1, width=2, height=1, bg='white', command = lambda: change(13))
dbBtn.grid(column=1, row=7, sticky='new')
dcBtn = tk.Button(framePassword1, width=2, height=1, bg='white', command = lambda: change(14))
dcBtn.grid(column=2, row=7, sticky='new')
ddBtn = tk.Button(framePassword1, width=2, height=1, bg='white', command = lambda: change(15))
ddBtn.grid(column=3, row=7, sticky='new')

tk.Label(frameLabel, font=('Arial', 10), text='Re-enter password:', padx=10, pady=10).grid(columnspan=2, row=3)

#Check buttons
eeBtn = tk.Button(framePassword2, width=2, height=1, bg='white', command = lambda: changeCheck(0))
eeBtn.grid(column=0, row=10, sticky='se')
efBtn = tk.Button(framePassword2, width=2, height=1, bg='white', command = lambda: changeCheck(1))
efBtn.grid(column=1, row=10, sticky='sew')
egBtn = tk.Button(framePassword2, width=2, height=1, bg='white', command = lambda: changeCheck(2))
egBtn.grid(column=2, row=10, sticky='sew')
ehBtn = tk.Button(framePassword2, width=2, height=1, bg='white', command = lambda: changeCheck(3))
ehBtn.grid(column=3, row=10, sticky='sew')

feBtn = tk.Button(framePassword2, width=2, height=1, bg='white', command = lambda: changeCheck(4))
feBtn.grid(column=0, row=11, sticky='nse')
ffBtn = tk.Button(framePassword2, width=2, height=1, bg='white', command = lambda: changeCheck(5))
ffBtn.grid(column=1, row=11, sticky='nsew')
fgBtn = tk.Button(framePassword2, width=2, height=1, bg='white', command = lambda: changeCheck(6))
fgBtn.grid(column=2, row=11, sticky='nsew')
fhBtn = tk.Button(framePassword2, width=2, height=1, bg='white', command = lambda: changeCheck(7))
fhBtn.grid(column=3, row=11, sticky='nsew')

geBtn = tk.Button(framePassword2, width=2, height=1, bg='white', command = lambda: changeCheck(8))
geBtn.grid(column=0, row=12, sticky='nse')
gfBtn = tk.Button(framePassword2, width=2, height=1, bg='white', command = lambda: changeCheck(9))
gfBtn.grid(column=1, row=12, sticky='nsew')
ggBtn = tk.Button(framePassword2, width=2, height=1, bg='white', command = lambda: changeCheck(10))
ggBtn.grid(column=2, row=12, sticky='nsew')
ghBtn = tk.Button(framePassword2, width=2, height=1, bg='white', command = lambda: changeCheck(11))
ghBtn.grid(column=3, row=12, sticky='nsew')

heBtn = tk.Button(framePassword2, width=2, height=1, bg='white', command = lambda: changeCheck(12))
heBtn.grid(column=0, row=13, sticky='nse')
hfBtn = tk.Button(framePassword2, width=2, height=1, bg='white', command = lambda: changeCheck(13))
hfBtn.grid(column=1, row=13, sticky='nsew')
hgBtn = tk.Button(framePassword2, width=2, height=1, bg='white', command = lambda: changeCheck(14))
hgBtn.grid(column=2, row=13, sticky='nsew')
hhBtn = tk.Button(framePassword2, width=2, height=1, bg='white', command = lambda: changeCheck(15))
hhBtn.grid(column=3, row=13, sticky='nsew')

buttons = [aaBtn, abBtn, acBtn, adBtn, baBtn, bbBtn, bcBtn, bdBtn, caBtn, cbBtn, ccBtn, cdBtn, daBtn, dbBtn, 
           dcBtn, ddBtn]

buttonsCheck = [eeBtn, efBtn, egBtn, ehBtn, feBtn, ffBtn, fgBtn, fhBtn, geBtn, gfBtn, ggBtn, ghBtn,
                heBtn, hfBtn, hgBtn, hhBtn]

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(4, weight=1)

submitBtn = tk.Button(text='Submit',width=5,height=1, padx=10, command=click)
submitBtn.grid(column=0, row=14, sticky='w')
resetBtn = tk.Button(text='Reset entries',width=6,height=1, padx=10, command=reset)
resetBtn.grid(column=1, row=14, sticky='e')

wrongInput = tk.Label(font=('Arial', 10), text='Entries does not match or input is invalid, please reset and enter valid input.', padx=10, pady=10)

window.mainloop()
