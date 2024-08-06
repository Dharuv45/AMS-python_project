from tkinter import *
from tkinter.ttk import Notebook
import sqlite3
from tkinter import messagebox
from admin import *
from teacher import *
class Main:
    def __init__(self):
        self.root = Tk()
        self.root.geometry(f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}")
        self.view()
        # self.set_admin_credentials("dharuv@gmail.com", "adge")
        self.root.mainloop()
        
    def adminlogin(self):
        db = sqlite3.connect("attendancesystem.db")
        cr = db.cursor()
        cr.execute(f"select * from Admin where Email='{self.Adminemail.get()}' and password='{self.Adminpass.get()}'")
        data = cr.fetchone()
        print(data)
        if data:
            messagebox.showinfo("Success", "Welcome")
            self.root.destroy()
            obj=Admin()
        else:
            messagebox.showerror("Error", "Wrong credentials")
         
    def teacherlog(self):
        db = sqlite3.connect("attendancesystem.db")
        cr = db.cursor()
        cr.execute(f"select * from teacher where Email='{self.teacheremail.get()}' and password='{self.teacherpass.get()}'")
        data = cr.fetchone()
        print(data)
        if data:
            messagebox.showinfo("Success", "Welcome")
            self.root.destroy()
            obj=Teacher()
        else:
            messagebox.showerror("Error", "Wrong credentials")
    def view(self):
        nb = Notebook(self.root)
        nb.pack(expand=True, fill=BOTH)
        
        F1 = Frame(nb, bg='#0077b6')
        F1.pack(expand=True, fill='both')
        f11 = Frame(F1, bg='#0077b6')
        f11.place(relx=0.5, rely=0.5, anchor='center')
        l1 = Label(f11, text="Email", font=("Arial", 16))
        l1.grid(row=0, column=0)
        self.studentemail = Entry(f11, font=("Arial", 16))
        self.studentemail.grid(row=0, column=1, padx=1, pady=10)
        l2 = Label(f11, text="Password", font=("Arial", 16))
        l2.grid(row=1, column=0, padx=10, pady=10)
        self.studentpass = Entry(f11, show='*', font=("Arial", 16))
        self.studentpass.grid(row=1, column=1, padx=10, pady=10)
        btn = Button(f11, text="Login", font=("Arial", 16))
        btn.grid(row=2, column=1, padx=10, pady=10)
        nb.add(F1, text="Student login")
        
        F2 = Frame(nb, bg='#f48c06')
        F2.pack(expand=True, fill='both')
        f22 = Frame(F2, bg='#f48c06')
        f22.place(relx=0.5, rely=0.5, anchor='center')
        l1 = Label(f22, text="Email", font=("Arial", 16))
        l1.grid(row=0, column=0, padx=10, pady=10)
        self.teacheremail = Entry(f22, font=("Arial", 16))
        self.teacheremail.grid(row=0, column=1, padx=1, pady=10)
        l2 = Label(f22, text="Password", font=("Arial", 16))
        l2.grid(row=1, column=0, padx=10, pady=10)
        self.teacherpass = Entry(f22, show='*', font=("Arial", 16))
        self.teacherpass.grid(row=1, column=1, padx=10, pady=10)
        btn = Button(f22, text="Login", font=("Arial", 16),command=self.teacherlog)
        btn.grid(row=2, column=1, padx=10, pady=10)
        nb.add(F2, text="Teacher login")
        
        F3 = Frame(nb, bg='#f8ad9d')
        F3.pack(expand=True, fill='both')
        f33 = Frame(F3, bg='#f8ad9d')
        f33.place(relx=0.5, rely=0.5, anchor='center')
        l1 = Label(f33, text="Email", font=("Arial", 16))
        l1.grid(row=0, column=0, padx=10, pady=10)
        self.Adminemail = Entry(f33, font=("Arial", 16))
        self.Adminemail.grid(row=0, column=1, padx=1, pady=10)
        l2 = Label(f33, text="Password", font=("Arial", 16))
        l2.grid(row=1, column=0, padx=10, pady=10)
        self.Adminpass = Entry(f33, show='*', font=("Arial", 16))
        self.Adminpass.grid(row=1, column=1, padx=10, pady=10)
        btn = Button(f33, text="Login", font=("Arial", 16), command=self.adminlogin)
        btn.grid(row=2, column=1, padx=10, pady=10)
        nb.add(F3, text="Admin login")



obj = Main()   
