# -*- coding: utf-8 -*-
"""
Created on Thu May  6 16:22:40 2021

@author: gustav martin
"""
import tkinter as tk
import os
import sys
from fingerprint import *

def click():
    """
    Checks user input username against system username.
    """
    user = os.getlogin()
    username = getUserName()
    if user == username:
        userSuccess()
    else:
        wrongInput.grid(column= 1, row=4)
        wrongInput2.grid(column= 1, row=5)

def getUserName():
    """
    Gets username from user entry.
    """
    username = userEntry.get()
    return username

def userSuccess():
    """'
    Opens and displayes the success login window.
    """
    window.destroy()
    
    successWindow = tk.Tk()
    successWindow.geometry("300x100")
    tk.Label(successWindow, font=("Arial", 10), text='Username is correct.').grid(columnspan=3, row=1, sticky='e')
    tk.Label(successWindow, font=("Arial", 10), text='Click start and put your finger on the fingerprint scanner.').grid(columnspan=3, row=2, sticky='e')
    submitBtn = tk.Button(text='Start Scan',width=10,height=1, command=finger)
    submitBtn.grid(column=0, row=3, sticky='n')
    
    
    successWindow.grid_columnconfigure(0, weight=1)
    successWindow.grid_columnconfigure(4, weight=1)
    


def loginSuccess():
    """'
    Opens and displayes the success login window.
    """
    success = tk.Tk()
    success.geometry("300x100")
    tk.Label(success, padx=10, pady=10, font=("Arial", 20), text='Login successfull').pack()
    
def loginFailed():
    """'
    Opens and displayes the fail login window.
    """
    failed = tk.Tk()
    failed.geometry("300x100")
    tk.Label(failed, padx=10, pady=10, font=("Arial", 20), text='Login failed, please restart program.').pack()
    
def reset():
    """
    Resets the user entry by restarting the program.
    """
    os.execl(sys.executable, sys.executable, *sys.argv)
    
def finger():
    """
    Fingerprint recognition using luspock's solution: https://github.com/luspock/FingerPrint.
    """
    try:
        myFP.open()
        if myFP.verify():
            loginSuccess()
        else:
            loginFailed()
    finally:
        myFP.close()

myFP = FingerPrint()

window = tk.Tk()
window.geometry("300x200")

frameUser = tk.Canvas(window, width=300, height=100)
frameUser.grid(columnspan=3)


tk.Label(frameUser,font=('Arial', 10), text=' \n ', padx=10, pady=10).grid(column=0, row=1, sticky='e')
tk.Label(frameUser, font=('Arial', 10), text='Username:', padx=10, pady=10).grid(column=0, row=2, sticky='e')


#User entry
content = tk.StringVar()
userEntry = tk.Entry(frameUser, width=10)
userEntry.grid(column=1, row=2, columnspan=3, sticky='w')

submitBtn = tk.Button(frameUser, text='Submit',width=10,height=1, command=click)
submitBtn.grid(column=0, row=3, sticky='n')
resetBtn = tk.Button(frameUser, text='Reset entries',width=10,height=1, command=reset)
resetBtn.grid(column=1, row=3, sticky='w')

wrongInput = tk.Label(font=("Arial", 10), text='The entered username is not correct.')
wrongInput2 = tk.Label(font=("Arial", 10), text='Please reset and enter the correct username.')

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(4, weight=1)

window.mainloop()
