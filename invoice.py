from tkinter import *
from tkinter import messagebox
from functools import partial
import login
import calculate
import feedback

#Generating Invoice and storing in the device
#Location of Invoice in Folder containing project files
def generateInvoice(cid, n, p, e, a, itemList, itemcostList, quantityList, costList, totalAmount, discount, tax, feedbackValue):
    global fileName

    f = open("{}.txt".format(cid), "w+")
    f.write("INVOICE\n")
    f.write("-"*117)
    f.write("\n")
    f.write("Customer ID = {}\n".format(cid))
    f.write("Name = {}\n".format(n))
    f.write("Phone Number = {}\n".format(p))
    f.write("Email ID = {}\n\n".format(e))
    f.write("")
    f.write("Item\t\t\tCost\t\t\tQuantity\t\tTotalCost\n")
    f.write("-" * 117)
    f.write("\n")
    for i in range(len(itemList)):
        f.write("{}\t\t\t{}\t\t\t{}\t\t\t{}\n".format(itemList[i], itemcostList[i], quantityList[i], costList[i]))
    f.write("\n")
    f.write("-"*117)
    f.write("\n")
    f.write("Discount = Rs.{}\n".format(discount))
    f.write("Tax = Rs.{}\n".format(tax))
    f.write("Total Amount = Rs.{}\n\n".format(totalAmount))
    f.write("Feedback = {}\n".format(feedbackValue))

    f.close()

    fileName = "{}.txt".format(cid)

    messagebox.showinfo("generateInvoice", "Invoice Generated")


tkWindow = Tk()
tkWindow.geometry('100x100')
tkWindow.title('Invoice Page')
tkWindow.configure(bg='#FFFFFF')

generateInvoice = partial(generateInvoice, login.cid, calculate.n, calculate.p, calculate.e, calculate.a, calculate.itemList,
                      calculate.itemcostList, calculate.quantityList, calculate.costList, calculate.totalAmount,
                      calculate.discount, calculate.tax, feedback.feedbackValue)

Label(tkWindow, text="\t\t", bg='#FFFFFF').grid(row=0, column=2)
invoiceButton = Button(tkWindow, text='Invoice', bg='#AC94CE', fg='#FFFFFF', border='0', command=generateInvoice).grid(row=1, column=2)

tkWindow.mainloop()