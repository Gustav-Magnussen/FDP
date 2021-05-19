# -*- coding: utf-8 -*-
"""
Created on Sun May  9 00:53:53 2021

@author: gustav martin
"""
import sqlite3


connect = sqlite3.connect('users.db')

cr = connect.cursor()

command = """CREATE TABLE IF NOT EXISTS
users(user_id INTEGER PRIMARY KEY, username TEXT, password TEXT)"""
cr.execute(command)

#Adds test user data
cr.execute("INSERT INTO users (username, password) VALUES (?,?)",('bob','$argon2id$v=19$m=102400,t=2,p=8$JSo0Mx39wcxBVJHsBywhrQ$deop6ytHU+vu2rBAJdEoRA' ))
cr.execute("INSERT INTO users (username, password) VALUES (?,?)",('john','$argon2id$v=19$m=102400,t=2,p=8$qGZ6+0cPtsdJOhUpKGho9g$j7pFGeeQssHe/0m7y+ks4g' ))
connect.commit()
