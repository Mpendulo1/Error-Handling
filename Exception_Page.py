from tkinter import *
from tkinter import messagebox

master = Tk()
master.geometry('600x600')
master.configure(bg='tomato')
master.title('Exception Handling')
label = Label(master, text='Please Enter Amount In Your Account', bg='OrangeRed2', fg='honeydew', font=('Arial', 20, 'bold'))
label.place(x=40, y=40)
entry1 = Entry(master, bg='honeydew', fg='gray20', width=40, font=('Arial', 20, 'bold'))
entry1.place(x=150, y=90, width=300, height=40)


def check_qualification():
    try:
        if int(entry1.get()) >= 3000:
            messagebox.showinfo("Message", "Congratulations. You qualify to go to Malaysia.")
    except ValueError:
        if entry1.get() != int:
            messagebox.showinfo("Message", "Please deposit more funds for this excursion.")
    else:
        if int(entry1.get()) < 3000:
            messagebox.showerror("Message", "Try Again")


button1 = Button(master, text='Check Qualification', bg='gray80', fg='gray12', font=('Georgia', 20, 'bold'), cursor='hand2', command=check_qualification)
button1.place(x=150, y=150, width=300, height=40)


def close():
    master.destroy()


button2 = Button(master, text='Exit', bg='gray80', fg='gray12', font=('Georgia', 20, 'bold'), cursor='hand2', command=close)
button2.place(x=250, y=500)
master.mainloop()
