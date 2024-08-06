from tkinter import *
from tkinter.ttk import Notebook, Treeview, Combobox
import sqlite3
from tkinter import messagebox

class Teacher:
    def __init__(self):
        self.root4 = Tk()
        self.root4.geometry(f"{self.root4.winfo_screenwidth()}x{self.root4.winfo_screenheight()}")
        self.view()
        self.root4.mainloop()

    def view(self):
        nb = Notebook(self.root4)
        nb.pack(fill="both", expand=True)
        
        # First Tab: Add Students
        F2 = Frame(nb, bg="#bde0fe")
        
        f22 = Frame(F2, bg="#bde0fe")
        f22.place(relx=0.5, rely=0.5, anchor="center")
        
        l1 = Label(f22, text="Roll Number")
        l1.grid(row=0, column=0)
        self.rollno = Entry(f22)
        self.rollno.grid(row=0, column=1)
        
        l2 = Label(f22, text="Name")
        l2.grid(row=1, column=0)
        self.studentsname = Entry(f22)
        self.studentsname.grid(row=1, column=1)
        
        l3 = Label(f22, text="Email")
        l3.grid(row=2, column=0)
        self.studentsemail = Entry(f22)
        self.studentsemail.grid(row=2, column=1)
        
        l4 = Label(f22, text="Password")
        l4.grid(row=3, column=0)
        self.studentspass = Entry(f22, show="*")
        self.studentspass.grid(row=3, column=1)
        
        self.gender = StringVar(value="Male")
        
        l5 = Label(f22, text="Gender")
        l5.grid(row=4, column=0)
        
        self.teachergender = Radiobutton(f22, text="Male", value="Male", variable=self.gender)
        self.teachergender.grid(row=4, column=1)
        
        self.teachergender1 = Radiobutton(f22, text="Female", value="Female", variable=self.gender)
        self.teachergender1.grid(row=5, column=1)

        addstudents = Button(f22, text="Add Students")
        addstudents.grid(row=6, column=1, padx=10, pady=10)

        nb.add(F2, text="Add Students")
        
        # Second Tab: Add Details
        F1 = Frame(nb, bg="#bde0fe")
        
        f11 = Frame(F1, bg="#bde0fe")
        f11.place(relx=0.5, rely=0.5, anchor="center") 

        l1 = Label(f11, text="Roll Number")
        l1.grid(row=0, column=0)
        self.details_rollno = Entry(f11)
        self.details_rollno.grid(row=0, column=1)

        l2 = Label(f11, text="Attendance")
        l2.grid(row=1, column=0)
        self.attendance = Entry(f11)
        self.attendance.grid(row=1, column=1)

        l3 = Label(f11, text="Marks")
        l3.grid(row=2, column=0)
        self.marks = Entry(f11)
        self.marks.grid(row=2, column=1)

        adddetails = Button(f11, text="Add Details")
        adddetails.grid(row=3, column=1, padx=10, pady=10)

        nb.add(F1, text="Add Details")


