"""
Name: Jason Elliott
Date: 7/13/2024
Assignment: Create a working GUI interface for that includes instructions based on coursework, however tailor it to my wifes business for artwork. 

This is still a work in progress!!!!! 
"""
#Any imports would come first

from tkinter import *

#Window Number 1 of 2
window1=Tk()
window1.title("Guessing Game")
window1.geometry('800x500')

#Start of instructions and thank you to customer
ty_lbl = Label(window1, text="Thank you for coming!")
ty_lbl.grid()
instr_lbl = Label(window1, text="Please complete the questions below to obtain a live quote. If the amount is agreeable, submit to send request.")
instr_lbl.grid()

#functions
def followup():
    global comp_numb, guess2_lbl
    guess2_lbl.config(text=str(comp_numb))

def denial():
    global low_num, high_num, comp_numb
    high_num = comp_numb - 1
    comp_numb = random.randint(low_num, high_num)
    updateGuess()

def quote():
    global low_num, high_num, comp_numb
    low_num = comp_numb + 1
    comp_numb = random.randint(low_num, high_num)
    updateGuess()

btn1 = Button(window1, text="Would you like a follow up?", fg="red", command=followup)
btn2 = Button(window1, text="No, Thanks", fg="red", command=denial)
btn3 = Button(window1, text="Yes, Contact me for pricing", fg="green", command=quote)

btn1.grid(column=0, row=2)
btn2.grid(column=0, row=3)
btn3.grid(column=0, row=4)





window1.mainloop()
