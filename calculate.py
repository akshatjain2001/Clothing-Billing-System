from tkinter import *
from functools import partial

#Collect Data from Customer
def getValues(name, phonenumber, emailID, address, winter, winterValue, summer, summerValue, monsoon, monsoonValue, tops,
              topsValue, jeans, jeansValue, jacket, jacketValue, blazer, blazerValue, trouser, trouserValue, shoes, shoesValue):
    global n
    global p
    global e
    global a
    global winterItem
    global winterQuantity
    global summerItem
    global summerQuantity
    global monsoonItem
    global monsoonQuantity
    global topsItem
    global topsQuantity
    global jeansItem
    global jeansQuantity
    global jacketItem
    global jacketQuantity
    global blazerItem
    global blazerQuantity
    global trouserItem
    global trouserQuantity
    global shoesItem
    global shoesQuantity

    n = name.get()
    p = phonenumber.get()
    e = emailID.get()
    a = address.get()
    winterItem = winter.get()
    winterQuantity = winterValue.get()
    summerItem = summer.get()
    summerQuantity = summerValue.get()
    monsoonItem = monsoon.get()
    monsoonQuantity = monsoonValue.get()
    topsItem = tops.get()
    topsQuantity = topsValue.get()
    jeansItem = jeans.get()
    jeansQuantity = jeansValue.get()
    jacketItem = jacket.get()
    jacketQuantity = jacketValue.get()
    blazerItem = blazer.get()
    blazerQuantity = blazerValue.get()
    trouserItem = trouser.get()
    trouserQuantity = trouserValue.get()
    shoesItem = shoes.get()
    shoesQuantity = shoesValue.get()
    calculation(winterItem, winterQuantity, summerItem, summerQuantity, monsoonItem, monsoonQuantity, topsItem, topsQuantity,
                jeansItem, jeansQuantity, jacketItem, jacketQuantity, blazerItem, blazerQuantity, trouserItem, trouserQuantity,
                shoesItem, shoesQuantity)

#Calculation of Bill
def calculation(winterItem, winterQuantity, summerItem, summerQuantity, monsoonItem, monsoonQuantity, topsItem, topsQuantity,
                jeansItem, jeansQuantity, jacketItem, jacketQuantity, blazerItem, blazerQuantity, trouserItem, trouserQuantity,
                shoesItem, shoesQuantity):
    global itemList
    global itemcostList
    global quantityList
    global costList
    global totalAmount
    global discount
    global tax

    itemList = []
    itemcostList = []
    quantityList = []
    costList = []
    if winterItem == 1:
        itemList += ['Winter']
        itemcostList += ['2000']
        quantityList += [winterQuantity]
        costList += [2000*winterQuantity]
    if summerItem == 1:
        itemList += ['Summer']
        itemcostList += ['2000']
        quantityList += [summerQuantity]
        costList += [2000*summerQuantity]
    if monsoonItem == 1:
        itemList += ['Monsoon']
        itemcostList += ['2000']
        quantityList += [monsoonQuantity]
        costList += [2000*monsoonQuantity]
    if topsItem == 1:
        itemList += ['Tops']
        itemcostList += ['1000']
        quantityList += [topsQuantity]
        costList += [1000*topsQuantity]
    if jeansItem == 1:
        itemList += ['Jeans']
        itemcostList += ['2000']
        quantityList += [jeansQuantity]
        costList += [2000*jeansQuantity]
    if jacketItem == 1:
        itemList += ['Jacket']
        itemcostList += ['2000']
        quantityList += [jacketQuantity]
        costList += [2000*jacketQuantity]
    if blazerItem == 1:
        itemList += ['Blazer']
        itemcostList += ['3000']
        quantityList += [blazerQuantity]
        costList += [3000*blazerQuantity]
    if trouserItem == 1:
        itemList += ['Trouser']
        itemcostList += ['3000']
        quantityList += [trouserQuantity]
        costList += [3000*trouserQuantity]
    if shoesItem == 1:
        itemList += ['Shoes']
        itemcostList += ['3000']
        quantityList += [shoesQuantity]
        costList += [3000*shoesQuantity]

    totalAmount = float
    discount = float
    tax = float
    totalAmount = sum(costList)
    tax = totalAmount*0.02
    if totalAmount > 15000:
        discount = totalAmount * 0.1
        totalAmount -= discount
    elif totalAmount > 8000:
        discount = totalAmount * 0.05
        totalAmount -= discount
    else:
        discount = 0
        totalAmount -= discount
    totalAmount += tax

    Label(tkWindow, text="Discount= ", bg='#FFFFFF').grid(row=22, column=1)
    Label(tkWindow, text=" ₹{}".format(discount), bg='#FFFFFF').grid(row=22, column=2)
    Label(tkWindow, text="Tax= ", bg='#FFFFFF').grid(row=23, column=1)
    Label(tkWindow, text=" ₹{}".format(tax), bg='#FFFFFF').grid(row=23, column=2)
    Label(tkWindow, text="Total Amount= ", bg='#FFFFFF').grid(row=24, column=1)
    Label(tkWindow, text=" ₹{}".format(totalAmount), bg='#FFFFFF').grid(row=24, column=2)


tkWindow = Tk()
tkWindow.geometry('500x600')
tkWindow.title('Bill Generation Page')
tkWindow.configure(bg='#FFFFFF')

Label(tkWindow, text="\t", bg='#FFFFFF').grid(row=0, column=0)
Label(tkWindow, text="\t", bg='#FFFFFF').grid(row=1, column=0)
nameLabel = Label(tkWindow, text='Name', bg='#FFFFFF').grid(row=1, column=1)
name = StringVar()
nameEntry = Entry(tkWindow, textvariable=name, bg='#ECE4FC', border='0').grid(row=1, column=2)
Label(tkWindow, text="\t", bg='#FFFFFF').grid(row=1, column=3)

Label(tkWindow, text="\t", bg='#FFFFFF').grid(row=2, column=0)
phonenumberLabel = Label(tkWindow, text='Phone Number', bg='#FFFFFF').grid(row=2, column=1)
phonenumber = StringVar()
phonenumberEntry = Entry(tkWindow, textvariable=phonenumber, bg='#ECE4FC', border='0').grid(row=2, column=2)
Label(tkWindow, text="\t", bg='#FFFFFF').grid(row=2, column=3)

Label(tkWindow, text="\t", bg='#FFFFFF').grid(row=3, column=0)
emailIDLabel = Label(tkWindow, text='Email ID', bg='#FFFFFF').grid(row=3, column=1)
emailID = StringVar()
emailIDEntry = Entry(tkWindow, textvariable=emailID, bg='#ECE4FC', border='0').grid(row=3, column=2)
Label(tkWindow, text="\t", bg='#FFFFFF').grid(row=3, column=3)

Label(tkWindow, text="\t", bg='#FFFFFF').grid(row=4, column=0)
addressLabel = Label(tkWindow, text='Address', bg='#FFFFFF').grid(row=4, column=1)
address = StringVar()
addressEntry = Entry(tkWindow, textvariable=address, bg='#ECE4FC', border='0').grid(row=4, column=2)
Label(tkWindow, text="\t", bg='#FFFFFF').grid(row=4, column=4)


#Seasonal Apparel
Label(tkWindow, text='\t', bg='#FFFFFF').grid(row=5, column=0)

Label(tkWindow, text="\t", bg='#FFFFFF').grid(row=6, column=0)
winter = IntVar()
Checkbutton(tkWindow, text="Winter Set (₹2000)", bg='#FFFFFF', variable=winter).grid(row=6, column=1)
winterValue = IntVar()
winterEntry = Entry(tkWindow, textvariable=winterValue, bg='#ECE4FC', border='0').grid(row=6, column=2)
Label(tkWindow, text="\t", bg='#FFFFFF').grid(row=6, column=3)

Label(tkWindow, text="\t", bg='#FFFFFF').grid(row=7, column=0)
summer = IntVar()
Checkbutton(tkWindow, text="Summer Set (₹2000)", bg='#FFFFFF', variable=summer).grid(row=7, column=1)
summerValue = IntVar()
summerEntry = Entry(tkWindow, textvariable=summerValue, bg='#ECE4FC', border='0').grid(row=7, column=2)
Label(tkWindow, text="\t", bg='#FFFFFF').grid(row=7, column=3)

Label(tkWindow, text="\t", bg='#FFFFFF').grid(row=8, column=0)
monsoon = IntVar()
Checkbutton(tkWindow, text="Monsoon Set (₹2000)", bg='#FFFFFF', variable=monsoon).grid(row=8, column=1)
monsoonValue = IntVar()
monsoonEntry = Entry(tkWindow, textvariable=monsoonValue, bg='#ECE4FC', border='0').grid(row=8, column=2)
Label(tkWindow, text="\t", bg='#FFFFFF').grid(row=8, column=3)


#Casual Apparel
Label(tkWindow, text='\t', bg='#FFFFFF').grid(row=10, column=0)

Label(tkWindow, text="\t", bg='#FFFFFF').grid(row=11, column=0)
tops = IntVar()
Checkbutton(tkWindow, text="Tops (₹1000)", bg='#FFFFFF', variable=tops).grid(row=11, column=1)
topsValue = IntVar()
topsEntry = Entry(tkWindow, textvariable=topsValue, bg='#ECE4FC', border='0').grid(row=11, column=2)
Label(tkWindow, text="\t", bg='#FFFFFF').grid(row=11, column=3)

Label(tkWindow, text="\t", bg='#FFFFFF').grid(row=12, column=0)
jeans = IntVar()
Checkbutton(tkWindow, text="Jeans (₹2000)", bg='#FFFFFF', variable=jeans).grid(row=12, column=1)
jeansValue = IntVar()
jeansEntry = Entry(tkWindow, textvariable=jeansValue, bg='#ECE4FC', border='0').grid(row=12, column=2)
Label(tkWindow, text="\t", bg='#FFFFFF').grid(row=12, column=3)

Label(tkWindow, text="\t", bg='#FFFFFF').grid(row=13, column=0)
jacket = IntVar()
Checkbutton(tkWindow, text="Jacket (₹2000)", bg='#FFFFFF', variable=jacket).grid(row=13, column=1)
jacketValue = IntVar()
jacketEntry = Entry(tkWindow, textvariable=jacketValue, bg='#ECE4FC', border='0').grid(row=13, column=2)
Label(tkWindow, text="\t", bg='#FFFFFF').grid(row=13, column=3)


#Formal Apparel
Label(tkWindow, text='\t', bg='#FFFFFF').grid(row=14, column=0)

Label(tkWindow, text="\t", bg='#FFFFFF').grid(row=16, column=0)
blazer = IntVar()
Checkbutton(tkWindow, text="Blazer (₹3000)", bg='#FFFFFF', variable=blazer).grid(row=16, column=1)
blazerValue = IntVar()
blazerEntry = Entry(tkWindow, textvariable=blazerValue, bg='#ECE4FC', border='0').grid(row=16, column=2)
Label(tkWindow, text="\t", bg='#FFFFFF').grid(row=16, column=3)

Label(tkWindow, text="\t", bg='#FFFFFF').grid(row=17, column=0)
trouser = IntVar()
Checkbutton(tkWindow, text="Trouser (₹3000)", bg='#FFFFFF', variable=trouser).grid(row=17, column=1)
trouserValue = IntVar()
trouserEntry = Entry(tkWindow, textvariable=trouserValue, bg='#ECE4FC', border='0').grid(row=17, column=2)
Label(tkWindow, text="\t", bg='#FFFFFF').grid(row=17, column=3)

Label(tkWindow, text="\t", bg='#FFFFFF').grid(row=18, column=0)
shoes = IntVar()
Checkbutton(tkWindow, text="Shoes (₹3000)", bg='#FFFFFF', variable=shoes).grid(row=18, column=1)
shoesValue = IntVar()
shoesEntry = Entry(tkWindow, textvariable=shoesValue, bg='#ECE4FC', border='0').grid(row=18, column=2)
Label(tkWindow, text="\t", bg='#FFFFFF').grid(row=18, column=3)

#Calculate
getValues = partial(getValues, name, phonenumber, emailID, address, winter, winterValue, summer, summerValue, monsoon,
                    monsoonValue, tops, topsValue, jeans, jeansValue, jacket, jacketValue, blazer, blazerValue, trouser,
                    trouserValue, shoes, shoesValue)

Label(tkWindow, text="\t\t", bg='#FFFFFF').grid(row=19, column=1)
calculateButton = Button(tkWindow, text='Calculate', bg='#AC94CE', fg='#FFFFFF', border='0', command=getValues).grid(row=20, column=2)
Label(tkWindow, text="\t\t", bg='#FFFFFF').grid(row=21, column=1)

tkWindow.mainloop()