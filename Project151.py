
from tkinter import *
import random

root= Tk()
root.title("Monthly Profits")
root.geometry("800x800")
root["bg"] = "lightblue"

label1 = Label(root)
label2 = Label(root)
label3 = Label(root)
label4 = Label(root)

month = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

profits = (20000, 45000, 78000, 97000, 12000, 456000, 65000, 54000, 10000, 30000, 70000, 90000)

label1["text"] = "Months : January, February, March, April, May, June, July, August, September, October, November, December"
label2["text"] = "Profit : 20000, 45000, 78000, 97000, 12000, 456000, 65000, 54000, 10000, 30000, 70000, 90000"


max_profit = max(profits)
max_profit_index = profits.index(max_profit)

max_profit_month = month[max_profit_index]
label3["text"] = "The maximum profit of " + str(max_profit)+ " was recorded in the month of " + str(max_profit_month)



min_profit = min(profits)
min_profit_index = profits.index(min_profit)

min_profit_month = month[min_profit_index]
label4["text"] = "The maximum profit of " + str(min_profit)+ " was recorded in the month of " + str(min_profit_month)


btn1 = Button(root, text="Show Max Profitable Month")
btn1.place(relx = 0.5, rely = 0.3, anchor= CENTER)

btn2 = Button(root, text="Show Min Profitable Month")
btn2.place(relx = 0.5, rely = 0.5, anchor= CENTER)

label1.place(relx=0.5, rely=0.1, anchor=CENTER)
label2.place(relx=0.5, rely=0.2, anchor=CENTER)
label3.place(relx=0.5, rely=0.4, anchor=CENTER)
label4.place(relx=0.5, rely=0.6, anchor=CENTER)


root.mainloop()
