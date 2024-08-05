from tkinter import *
from tkinter.ttk import Notebook,Treeview
import sqlite3
from tkinter import messagebox

class Admin:
    def __init__(self):
        self.root1 = Tk()
        self.root1.geometry(f"{self.root1.winfo_screenwidth()}x{self.root1.winfo_screenheight()}")
        self.view()
        self.root1.mainloop()
    def addcourse(self):
        db = sqlite3.connect("attendancesystem.db")
        cr = db.cursor()
        cr.execute(f'''select * from courses where courseid={self.courseid.get()} or coursename='{self.coursename.get()}' ''')  
        data=cr.fetchone()
        if data:
            messagebox.showerror("Error","Course already exists")
        else:
            cr.execute(f'''insert into courses values({self.courseid.get()}, '{self.coursename.get()}')''')
            db.commit()
            db.close()
            messagebox.showinfo("Success","Course added successfully")
            self.getcoursees()
    def getcoursees(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        db = sqlite3.connect("attendancesystem.db")
        cr = db.cursor()
        cr.execute("select * from courses")
        data1=cr.fetchall()
        for i in data1:
            self.tree.insert('','end',values=i)

    def view(self):
        nb=Notebook()
        nb.pack(fill="both", expand=True)
        F1=Frame(bg="#bde0fe")
        F1.pack(fill="both", expand=True)
        f11=Frame(F1,bg="#bde0fe")
        f11.place(relx=0.5,rely=0.5,anchor="center")
        l1=Label(f11,text="Course Id")
        l1.grid(row=0,column=0,padx=10,pady=10)
        self.courseid=Entry(f11)
        self.courseid.grid(row=0,column=1,padx=10,pady=10)
        l2=Label(f11,text="Course name")
        l2.grid(row=1,column=0,padx=10,pady=10)
        self.coursename=Entry(f11)
        self.coursename.grid(row=1,column=1,padx=10,pady=10)
        btn=Button(f11,text="Add Course",command=self.addcourse)
        btn.grid(row=2,column=1,padx=10,pady=10)
        self.tree=Treeview(f11,columns=("column1","column2"),show="headings")
        self.tree.heading("column1",text="Course ID")
        self.tree.heading("column2",text="Course Name")
        self.tree.grid(row=3,column=1)
        self.getcoursees()
        nb.add(F1,text="Add Course") 






