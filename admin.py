from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter.ttk import Treeview,Notebook,Combobox

class Admin:
    def __init__(self):
        self.root1=Tk()
        self.root1.geometry(f'{self.root1.winfo_screenwidth()}x{self.root1.winfo_screenheight()}')
        self.view()
        self.root1.mainloop()

    def addcourse(self):
        db=sqlite3.connect("attendancesystem.db")
        cr=db.cursor()
        cr.execute(f'''select * from courses where courseid='{self.courseid.get()}' and coursename='{self.coursename.get()}' ''')
        data=cr.fetchone()
        if data:
            messagebox.showerror("Error","Course name or id already exists")
        else:
            cr.execute(f'''insert into courses values({self.courseid.get()},'{self.coursename.get()}')''')
            db.commit()
            messagebox.showinfo("Success","Course Added")
            self.getcourses()

    def addteacher(self):
        db=sqlite3.connect("attendancesystem.db")
        cr=db.cursor()
        cr.execute(f'''select * from  teacher where eid='{self.teacherid.get()}' and email = '{self.teacheremail.get()}' or courses ='{self.combo_teacher.get()}' ''')
        data=cr.fetchone()
        if data:
            messagebox.showerror("Error","Employee already or course already exists")
        else:
            cr.execute(f'''insert into teacher values({self.teacherid.get()},'{self.teachername.get()}','{self.teacheremail.get()}','{self.teacherpass.get()}','{self.gender.get()}','{self.combo_teacher.get()}')''')
            db.commit()
            messagebox.showinfo("Success","Teacher Added")
            self.getteacher()
       

    def getteacher(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        db=sqlite3.connect("attendancesystem.db")
        cr=db.cursor()
        cr.execute('''select * from teacher''')
        data=cr.fetchall()
        for i in data:
            self.tree1.insert('','end',values=i)
            
            

    def getcourses(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        db=sqlite3.connect("attendancesystem.db")
        cr=db.cursor()
        cr.execute('''select * from courses''')
        data1=cr.fetchall()
        for i in data1:
            self.tree.insert('','end',values=i)
            self.courses.append(i[1])
            
            
            

    def view(self):
        self.courses=[]
        nb=Notebook()
        nb.pack(expand=True,fill='both')

#COURSES
        
        F1=Frame(bg='#87CEEB')
        F1.pack(expand=True,fill='both')
        f11=Frame(F1,bg='#87CEEB')
        f11.place(relx=0.5,rely=0.5,anchor='center')
        l1=Label(f11,text="Course ID")
        l1.grid(row=0,column=0,padx=10,pady=10)
        self.courseid=Entry(f11)
        self.courseid.grid(row=0,column=1,padx=10,pady=10)

        l2=Label(f11,text="Course Name")
        l2.grid(row=1,column=0,padx=10,pady=10)
        self.coursename=Entry(f11)
        self.coursename.grid(row=1,column=1,padx=10,pady=10)
        btn=Button(f11,text="Add Course",command=self.addcourse)
        btn.grid(row=2,column=1,padx=10,pady=10)

        self.tree=Treeview(f11,columns=("column1","column2"),show='headings')
        self.tree.heading("column1",text="Course Id")
        self.tree.heading("column2",text="Course Name")
        self.tree.grid(row=3,column=1)
        self.getcourses()

        nb.add(F1,text="Add Course")

#TEACHERS

        F2=Frame(bg='#bde0fe')
        F2.pack(expand=True,fill='both')
        f22=Frame(F2,bg='#bde0fe')
        f22.place(relx=0.5,rely=0.5,anchor='center')

        l1=Label(f22,text="Employee ID")
        l1.grid(row=0,column=0,padx=10,pady=10)
        self.teacherid=Entry(f22)
        self.teacherid.grid(row=0,column=1,padx=10,pady=10)

        l2=Label(f22,text="Name")
        l2.grid(row=1,column=0,padx=10,pady=10)
        self.teachername=Entry(f22)
        self.teachername.grid(row=1,column=1,padx=10,pady=10)

        l3=Label(f22,text="Email")
        l3.grid(row=2,column=0,padx=10,pady=10)
        self.teacheremail=Entry(f22)
        self.teacheremail.grid(row=2,column=1,padx=10,pady=10)

        l4=Label(f22,text="Password")
        l4.grid(row=3,column=0,padx=10,pady=10)
        self.teacherpass=Entry(f22)
        self.teacherpass.grid(row=3,column=1,padx=10,pady=10)

        self.gender=StringVar(value='Male')
        l5=Label(f22,text="Gender")
        l5.grid(row=4,column=0,padx=10,pady=10)
        self.teachergender=Radiobutton(f22,text="Male",value="Male",variable=self.gender)
        self.teachergender.grid(row=4,column=1,padx=10,pady=10)
        self.teachergender1=Radiobutton(f22,text="Female",value="Female",variable=self.gender)
        self.teachergender1.grid(row=5,column=1,padx=10,pady=10)

        l6=Label(f22,text="Assign Course")
        l6.grid(row=6,column=0,padx=10,pady=10)
        self.combo_teacher=Combobox(f22,values=self.courses)
        self.combo_teacher.grid(row=6,column=1,padx=10,pady=10)
        btn=Button(f22,text="Add Teacher",command=self.addteacher)
        btn.grid(row=7,column=1,padx=10,pady=10)

        self.tree1=Treeview(f22,columns=("column1","column2","column3","column4","column5","column6"),show='headings')
        self.tree1.heading("column1",text="Id")
        self.tree1.heading("column2",text="Name")
        self.tree1.heading("column3",text="Email")
        self.tree1.heading("column4",text="Password")
        self.tree1.heading("column5",text="Gender")
        self.tree1.heading("column6",text="Course Assigned")
        self.tree1.grid(row=8,column=1)
        self.getteacher()


        nb.add(F2,text="Add Teacher")
