from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter.ttk import Treeview,Notebook,Combobox

class Student:
    def __init__(self,name,email):
        self.name = name
        self.email = email 
        self.root4=Tk()
        self.root4.geometry(f'{self.root4.winfo_screenwidth()}x{self.root4.winfo_screenheight()}')
        self.view()
        self.root4.mainloop()

    def getattendance(self):
        db = sqlite3.connect("attendancesystem.db")
        cr = db.cursor()
        
        cr.execute(f'''select * from student where email='{self.email}' ''')
        self.data = cr.fetchone()
        self.rollno = self.data[0]
        cr.execute(f'''select date,attendance from attendance where rollno='{self.rollno}' ''')
        data1 = cr.fetchall()
        
        for i in data1:
            self.tree.insert('','end',values=i)

    def updateprofile(self):
        db=sqlite3.connect("attendancesystem.db")
        cr=db.cursor()
        cr.execute(f'''update teacher set name='{self.name.get()}',password='{self.studentspass.get()}' where email='{self.email}' ''') 
        db.commit()
        messagebox.showinfo("Success","Profile Updated Succcessfully")      


    def logout(self):
        self.root4.destroy()
        import mainpanel      

    def view(self):
        nb = Notebook(self.root4)
        nb.pack(expand=True, fill='both')
        
        F1 = Frame(nb, bg='#dee2ff')
        F1.pack(expand=True, fill='both')
        
        f11 = Frame(F1, bg='#dee2ff')
        f11.place(relx=0.5, rely=0.5, anchor='center')
        
        self.tree = Treeview(f11, columns=("column1", "column2"), show='headings')
        self.tree.heading("column1", text="Date")
        self.tree.heading("column2", text="Attendance")

        self.tree.pack()
        self.getattendance()
        nb.add(F1,text="Students Attendance") 


        F3 = Frame(bg='#dee2ff')
        F3.pack(expand=True, fill='both')
        self.f33=Frame(F3,bg='#dee2ff')
        self.f33.place(relx=0.5,rely=0.5,anchor='center')
        list_data=[StringVar(value=self.data[i]) for i in range(len(self.data))]

        l1 = Label(self.f33, text="Roll Number")
        l1.grid(row=0, column=0, padx=10, pady=10)
        self.rollno = Entry(self.f33,textvariable=list_data[0],state='disabled')
        self.rollno.grid(row=0, column=1, padx=10, pady=10)

        l2 = Label(self.f33, text="Name")
        l2.grid(row=1, column=0, padx=10, pady=10)
        self.name = Entry(self.f33,textvariable=list_data[1])
        self.name.grid(row=1, column=1, padx=10, pady=10)

        l3 = Label(self.f33, text="Email")
        l3.grid(row=2, column=0, padx=10, pady=10)
        self.email = Entry(self.f33,textvariable=list_data[2],state='disabled')
        self.email.grid(row=2, column=1, padx=10, pady=10)

        l4 = Label(self.f33, text="Password")
        l4.grid(row=3, column=0, padx=10, pady=10)
        self.studentspass = Entry(self.f33,show="*",textvariable=list_data[3])
        self.studentspass.grid(row=3, column=1, padx=10, pady=10)


        l6 = Label(self.f33, text="Assign Course")
        l6.grid(row=4, column=0, padx=10, pady=10)
        self.combo = Entry(self.f33,textvariable=list_data[5],state='disabled')
        self.combo.grid(row=4, column=1, padx=10, pady=10)
        addteacher = Button(self.f33, text="Update Profile",command=self.updateprofile)
        addteacher.grid(row=5, column=1, padx=10, pady=10)

        logbtn = Button(self.f33, text="Logout",command=self.logout)
        logbtn.grid(row=6, column=1, padx=10, pady=10)

        nb.add(F3,text="Update Profile")


  