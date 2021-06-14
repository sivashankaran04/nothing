from tkinter import *
import tkinter.messagebox

window=Tk()
#declaring window title
window.title("EMPLOYEE DETAILS")
window.geometry("700x400")
window.configure(background="blue")


#CREATING NAME
firstname=Label(window,text="First Name").grid(row=1,column=1)
lastname=Label(window,text="Last Name").grid(row=2,column=1)
#EMAIL
email=Label(window,text="Email Id").grid(row=3,column=1)
#MOBILE NUMBER
mobile=Label(window,text="Contact number").grid(row=4,column=1)
#GENDER CREATED USING RADIOBUTTON
Gender =Label(window ,text = "Gender").grid(row = 5,column = 1)
var = IntVar()
Radiobutton(window, text="Male",padx = 30, variable=var, value=1).grid(row = 5,column = 2)
Radiobutton(window, text="Female",padx = 20, variable=var, value=2).grid(row = 5,column = 3)

#ADDRESS
Address = Label(window,text = "Address").grid(row = 6,column = 1)
#COUNTRY CREATED USING LIST
Country = Label(window ,text = "Country").grid(row = 7,column = 1)

list1 = ['INDIA','UK','USA','FRANCE','SPAIN']
c=StringVar()
droplist=OptionMenu(window,c, *list1)
droplist.config(width=15)
c.set('select your country')
droplist.grid(row = 7,column = 2)


firstname1=Entry(window).grid(row=1,column=2)
lastname1=Entry(window).grid(row=2,column=2)
email1=Entry(window).grid(row=3,column=2)
mobile1=Entry(window).grid(row=4,column=2)

Address1=Entry(window).grid(row=6,column=2)



#function declaration
def clicked():

    tkinter.messagebox.showinfo("entered successfully")

#button
Button(window, text="Submit", command=clicked,width=40,bg='grey',fg='blue').grid(row = 10,column = 2)
window.mainloop()


