from tkinter import *
from tkinter import messagebox

#Collect Feedback
def clicked(value):
    global feedbackValue
    messagebox.showinfo("clicked", "Thank you for your feedback!")
    feedbackValue = value


tkWindow = Tk()
tkWindow.geometry('300x250')
tkWindow.title('Feedback Page Page')
tkWindow.configure(bg='#FFFFFF')

Label(tkWindow, text="\t", bg='#FFFFFF').grid(row=0, column=2)

radio = StringVar()
Label(tkWindow, text="\t", bg='#FFFFFF').grid(row=2, column=1)
Radiobutton(tkWindow, text="Excellent", variable=radio, value="Excellent", bg='#FFFFFF').grid(row=2, column=2)
Radiobutton(tkWindow, text="Very Good", variable=radio, value="Very Good", bg='#FFFFFF').grid(row=3, column=2)
Radiobutton(tkWindow, text="Good", variable=radio, value="Good", bg='#FFFFFF').grid(row=4, column=2)
Radiobutton(tkWindow, text="Needs Improvement", variable=radio, value="Needs Improvement", bg='#FFFFFF').grid(row=5, column=2)
Radiobutton(tkWindow, text="Poor", variable=radio, value="Poor", bg='#FFFFFF').grid(row=6, column=2)

Label(tkWindow, text="\t\t", bg='#FFFFFF').grid(row=7, column=2)

#Feedback record Button
recordButton = Button(tkWindow, text="Record", bg='#AC94CE', fg='#FFFFFF', border='0', command=lambda: clicked(radio.get())).grid(row=8, column=2)

tkWindow.mainloop()