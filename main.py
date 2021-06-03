from tkinter import *
root = Tk()
root.title('Login Center')
root.geometry("600x600")
root.config(bg="OrangeRed2")

# Creating a widgets
l1 = Label(root, text='Login Details:', bg='OrangeRed2', fg='honeydew', font=('Arial', 20, 'bold'))
l1.place(x=120, y=10)

# Username
l2 = Label(root, text='Enter Username : ', bg='OrangeRed2', fg='honeydew', font=('Arial', 20, 'bold'))
l2.place(x=200, y=100)
e1 = Entry(root, bg='honeydew', fg='gray20', width=14, font=('Arial', 20, 'bold'))
e1.place(x=220, y=150)

# Password
l3 = Label(root, text='Enter Password : ', bg='OrangeRed2', fg='honeydew', font=('Arial', 20, 'bold'))

l3.place(x=200, y=250)
e2 = Entry(root, bg='honeydew', fg='gray20', width=14, font=('Arial', 20, 'bold'), show='*')

e2.place(x=220, y=300)


# Defining a Function fr logging in

def login():
   # importing message box
    from tkinter import messagebox
    username = ["Zipho", "Masi", "Lihle", "Thandokazi"]
    password = ["555", "333", "200", "221"]
    amount = [1000, 4000, 3000, 2900]

    found = False
    for x in range(len(username)):
        if e1.get()==username[x] and e2.get()==password[x] and amount[x]:
            found = True
        if found==True:
            messagebox.showinfo("PERMISSION", "ACCESS GRANTED")
            root.destroy()
            import Exception_Page
        else:
            messagebox.showinfo("ERROR INFO", "ACCESS DENIED")
            return
# Defining a function for clearing
def clear():
    e1.delete(0, END)
    e2.delete(0, END)


# Button
b1 = Button(root, text='Login', bg='gray80', fg='gray12', font=('Georgia', 20, 'bold'), cursor='hand2', command=login)
b1.place(x=250, y=400)


root.mainloop()
