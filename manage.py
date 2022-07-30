from tkinter import *
from tkinter import messagebox
from functools import partial
import pandas as pd
import matplotlib.pyplot as plt
import login
import calculate
import feedback
import invoice
import csv

#Storing data in .csv file
def store(cid, n, p, e, a, discount, tax,  totalamount, feedbackValue, filename):
    data = [cid, n, p, e, a, discount, tax, totalamount, feedbackValue, filename]
    with open('clothingdata.csv', 'a+', newline='') as newFile:
        newFileWriter = csv.writer(newFile)
        newFileWriter.writerow(data)
    messagebox.showinfo("store", "Details have been stored!")
    clothingData = pd.read_csv(r"C:\Users\Sruthi Jagan\PycharmProjects\MiniProject1\clothingdata.csv")

#Analysing feedback with bar chart
def analyseFeedback(feedbackValue):
    clothingData = pd.read_csv(r"C:\Users\Sruthi Jagan\PycharmProjects\MiniProject1\clothingdata.csv")
    df = pd.DataFrame(clothingData)
    df.groupby('Feedback').size().plot(kind='bar')
    plt.show()


tkWindow = Tk()
tkWindow.geometry('250x200')
tkWindow.title('Management Page')
tkWindow.configure(bg='#FFFFFF')

store = partial(store, login.cid, calculate.n, calculate.p, calculate.e, calculate.a, calculate.discount, calculate.tax,
                calculate.totalAmount, feedback.feedbackValue, invoice.fileName)

Label(tkWindow, text="\t", bg='#FFFFFF').grid(row=0, column=2)
Label(tkWindow, text="\t", bg='#FFFFFF').grid(row=1, column=0)
Button(tkWindow, text='Store', command=store, bg='#AC94CE', fg='#FFFFFF', border='0').grid(row=1, column=1)
Label(tkWindow, text="\t", bg='#FFFFFF').grid(row=1, column=2)

analyseFeedback = partial(analyseFeedback, feedback.feedbackValue)

Label(tkWindow, text="\t", bg='#FFFFFF').grid(row=3, column=2)
Label(tkWindow, text="\t", bg='#FFFFFF').grid(row=4, column=0)
Button(tkWindow, text='Analyse Feedback', command=analyseFeedback, bg='#AC94CE', fg='#FFFFFF', border='0').grid(row=4, column=1)
Label(tkWindow, text="\t", bg='#FFFFFF').grid(row=4, column=2)

tkWindow.mainloop()