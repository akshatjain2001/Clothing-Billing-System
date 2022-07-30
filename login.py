from tkinter import *
from tkinter import messagebox
from functools import partial


#Checking if password entered is matching with system password
def login(customerID, password):
    global cid
    cid = customerID.get()
    pwd = password.get()
    if pwd == 'admin':
        messagebox.showinfo("login", "Login Successful!")
    else:
        messagebox.showinfo("login", "Login Failed!")


tkWindow = Tk()
tkWindow.geometry('300x200')
tkWindow.title('Login Page')
tkWindow.configure(bg='#FFFFFF')


Label(tkWindow, text="     ", bg='#FFFFFF').grid(row=1, column=2)
Label(tkWindow, text="     ", bg='#FFFFFF').grid(row=2, column=2)

#Customer ID entry
Label(tkWindow, text="    ", bg='#FFFFFF').grid(row=3, column=0)
customerIDLabel = Label(tkWindow, text='CustomerID', bg='#FFFFFF').grid(row=3, column=1)
customerID = StringVar()
customerIDEntry = Entry(tkWindow, textvariable=customerID, bg='#ECE4FC', border='0').grid(row=3, column=2)
Label(tkWindow, text="     ", bg='#FFFFFF').grid(row=5, column=2)

#Password Entry
Label(tkWindow, text="     ", bg='#FFFFFF').grid(row=6, column=0)
passwordLabel = Label(tkWindow, text='Password', bg='#FFFFFF').grid(row=6, column=1)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*', bg='#ECE4FC', border='0').grid(row=6, column=2)

Label(tkWindow, text="     ", bg='#FFFFFF').grid(row=7, column=2)

login = partial(login, customerID, password)

#Login Button
loginButton = Button(tkWindow, text='login', bg='#AC94CE', fg='#FFFFFF', border='0', command=login).grid(row=8, column=2)


tkWindow.mainloop()