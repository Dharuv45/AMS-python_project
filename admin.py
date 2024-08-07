from tkinter import *
from tkinter.ttk import Notebook,Treeview,Combobox
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

    def addteacher(self):
        db = sqlite3.connect("attendancesystem.db")
        cr = db.cursor()
        cr.execute('''select * from teacher where eid=? or email=?''', (self.teacherid.get(), self.teacheremail.get()))

        data=cr.fetchone()
        if data:
            messagebox.showerror("Error","Employee already exists or Course already exists")
        else:
            cr.execute(f'''insert into teacher values('{self.teacherid.get()}', '{self.teachername.get()}','{self.teacheremail.get()}','{self.teacherpass.get()}','{self.gender.get()}', '{self.combo.get()}')''')
            db.commit()
            db.close()
            messagebox.showinfo("Success"," added successfully")
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
            self.courses.append(i[1])

    def view(self):
        self.courses=[]
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



        F2=Frame(bg="#bde0fe")
        F2.pack(fill="both", expand=True)
        f22=Frame(F2,bg="#bde0fe")
        f22.place(relx=0.5,rely=0.5,anchor="center")
        l1=Label(f22,text="Employeeid Id")
        l1.grid(row=0,column=0)
        self.teacherid=Entry(f22)
        self.teacherid.grid(row=0,column=1)
        l2=Label(f22,text="Name")
        l2.grid(row=1,column=0)
        self.teachername=Entry(f22)
        self.teachername.grid(row=1,column=1)
        l3=Label(f22,text="Email")
        l3.grid(row=2,column=0)
        self.teacheremail=Entry(f22)
        self.teacheremail.grid(row=2,column=1)
        l4=Label(f22,text="Passeord")
        l4.grid(row=3,column=0)
        self.teacherpass=Entry(f22)
        self.teacherpass.grid(row=3,column=1)
        self.gender=StringVar(value="Male")
        l5=Label(f22,text="Gender")
        l5.grid(row=4,column=0)
        self.teachergender=Radiobutton(f22,text="Male",value="Male", variable=self.gender)
        self.teachergender.grid(row=4,column=1)
        self.teachergender1=Radiobutton(f22,text="Female",value="Female",variable=self.gender)
        self.teachergender1.grid(row=5,column=1)
        l6=Label(f22,text="Assign Course")
        l6.grid(row=6,column=0,padx=10,pady=10)
        self.combo=Combobox(f22,values=self.courses)
        self.combo.grid(row=6,column=1,padx=10,pady=10)
        addteacher=Button(f22,text="add teacher",command=self.addteacher)
        addteacher.grid(row=7,column=1,padx=10,pady=10)
        nb.add(F2,text="Add Teacher")

# jhbgudbg



                  






