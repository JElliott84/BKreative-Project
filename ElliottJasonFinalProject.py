"""
Name: Jason Elliott
Date: 7/13/2024
Assignment: Create a working GUI interface for that includes instructions based on coursework
"""
#Any imports would come first
from tkinter import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import messagebox
from tkinter import ttk

#Module 1 - Windows and settings
#Window Number 1 of 2
window1=Tk()
window1.title("B-Kreative Art")
window1.geometry('600x800')
window1.configure(bg="lightblue")

#Window Number 2 0f 2
window2=Tk()
window2.title("Grand Opening")
window2.geometry('500x400')
window2.configure(bg="lightblue")

#Module 2 - Funtions
#This is the function for the drop down numbers on colors
def color_selected(event):
    selected_color = color_var.get()

#This Function is where the radio buttons are selected for the user to pick a medium
def sel():
        selection = "You selected the option " + str(var.get())
        label.config(text=selection)

#This Function is for a button that will exit the app
def exit_app():
    window1.destroy()
    window2.destroy()
    
#This is for submitting an email
def submit_email():
    email = email_entry.get()
    if validate_email(email):
        messagebox.showinfo("Success", f"Email submitted: {email}")
    else:
        messagebox.showerror("Error", "Invalid email address")
#Here is Simple email validation
def validate_email(email):
    if "@" in email and "." in email:
        return True
    return False

#This function is for the Application to send me an email based on the input of the user
def quote():
    sender_email = "jasonelliott1984@outlook.com"
    receiver_email = "jasonelliott1984@outlook.com"
    password = "MyemailPassword"

    subject = "Quote"
    body = "This is to inform you that a quote was requested."

# Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
# Connect to the server and send the email
        server = smtplib.SMTP('64.233.184.108')
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

        
#Module 3 - Program
#Here we begin with label #1 and thank the customer
ty_lbl = Label(window1, text="Thank you for coming!", font='Helveltica 18 bold')
ty_lbl.grid()

#Label #2 is where we tell our customer to answer their questions. 
instr_lbl = Label(window1, text="Please complete the questions below to obtain a live quote. If the amount is agreeable, submit to send request.")
instr_lbl.grid()

#I used this to place space between each category
spacer_lbl = Label(window1, text="")
spacer_lbl.grid()

#The next labels are where we ask our customer what type of medium they are going to use
step_lbl = Label(window1, text="Step 1", font='Helveltica 14 bold')
step_lbl.grid()

medium_lbl = Label(window1, text="What type of medium would you like to use?")
medium_lbl.grid()

#All 3 Radio Buttons
var = IntVar()
R1 = Radiobutton(window1, text="Paper", variable=var, value=1, command=sel)
R1.grid()
R2 = Radiobutton(window1, text="Canvas", variable=var, value=2, command=sel)
R2.grid()
R3 = Radiobutton(window1, text="Cloth", variable=var, value=3, command=sel)
R3.grid()

spacer_lbl = Label(window1, text="")
spacer_lbl.grid()

#The next label is how many colors the customer is going to use to a max of 5
step_lbl = Label(window1, text="Step 2", font='Helveltica 14 bold')
step_lbl.grid()
color_lbl = Label(window1, text="How many colors are you going to use?")
color_lbl.grid()
color_var = StringVar()
colors = ["1", "2", "3", "4", "5", "More than 5"]
color_dropdown =ttk.Combobox(window1, textvariable=color_var, values=colors)
color_dropdown.bind("<<ComboboxSelected>>", color_selected)
color_dropdown.grid(pady=20)
color_var.set(colors[0])

step_lbl = Label(window1, text="Step 3", font='Helveltica 14 bold')
step_lbl.grid()

#Here is where I input the buttons into the GUI
Final_lbl = Label(window1, text="Would you like a Follow up?")
Final_lbl.grid()
btn1 = Button(window1, text="Yes", fg="green", command=quote)
btn2 = Button(window1, text="No, Thanks", fg="red", command=exit_app)


#this is geometry for the buttons
btn1.grid(column=0, row=20)
btn2.grid(column=0, row=21)


#This is the second windows function to give information on a future store opening!
ty_lbl = Label(window2, text="New Store is Coming to Plant City Area", font='Helveltica 18 bold')
ty_lbl.pack(pady=10)



# Create and place the email label and entry
email_label = Label(window1, text="Enter your email:")
email_label.grid(pady=5)

email_entry = Entry(window1, width=30)
email_entry.grid(pady=5)

# Create and place the submit button
submit_button = Button(window1, text="Yes Contact Me for Pricing", fg="green", command=submit_email)
submit_button.grid(column=0, row=25)

#Execute
window1.mainloop()
window2.mainloop()

