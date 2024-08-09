from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter.ttk import Notebook
from admin import *
from teacher import *
from studentpanel import *
class Main:
    def __init__(self):
        self.root=Tk()
        self.root.geometry(f'{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}')
        self.view()
        self.root.mainloop()

    def adminlogin(self):
        db=sqlite3.connect("attendancesystem.db")
        cr=db.cursor()
        cr.execute(f'''select * from Admin where Email='{self.adminemail.get()}' and Password='{self.adminpass.get()}' ''')
        data=cr.fetchone()
        print(data)
        if data:
            messagebox.showinfo("Success",'welcome')
            self.root.destroy()
            obj=Admin()
        else:
            messagebox.showerror("Error","wronginfo")


    def teacherlog(self):
        db=sqlite3.connect("attendancesystem.db")
        cr=db.cursor()
        cr.execute(f'''select * from teacher where email='{self.teacheremail.get()}' and password='{self.teacherpass.get()}' ''')
        data=cr.fetchone()
        print(data)
        if data:
            messagebox.showinfo("Success",'welcome')
            self.root.destroy()
            obj=Teacher(data[1],data[2])
        else:
            messagebox.showerror("Error","wronginfo"    )

    def getcourses(self):
     
        db=sqlite3.connect("attendancesystem.db")
        cr=db.cursor()
        cr.execute('''select * from courses''')
        data1=cr.fetchall()
        for i in data1:
            self.courses.append(i[1])


    def addstudent(self):
        db=sqlite3.connect("attendancesystem.db")
        cr=db.cursor()
        cr.execute(f'''select * from student where 
                   rollno={self.studentid.get()} or
                   email='{self.studentemail.get()}' ''')
        data=cr.fetchone()
        if data:
            messagebox.showerror("Error","Student already exists or course already assigned")
        else:
            cr.execute(f'''insert into student values
                       ({self.studentid.get()},'{self.studentname.get()}'
                       ,'{self.studentemail.get()}',
                       '{self.studentpass.get()}'
                       ,'{self.gender.get()}'
                       ,'{self.combo.get()}')''' )
            db.commit()
            messagebox.showinfo("Success","Account Created")
            self.root7.destroy()

    def studentlog(self):
        db=sqlite3.connect("attendancesystem.db")
        cr=db.cursor()
        cr.execute(f'''select * from student where email='{self.studentemail.get()}' and Password='{self.studentpass.get()}' ''')
        data=cr.fetchone()
        print(data)
        if data:
            messagebox.showinfo("Success",'welcome')
            self.root.destroy()
            obj=Student(data[1],data[2])
        else:
            messagebox.showerror("Error","wronginfo")
    

   
    def studentregister(self):
        self.courses=[]
        self.gender=StringVar(value="Male")
        self.getcourses()
        self.root7=Tk()
        self.root7.geometry(f'{self.root7.winfo_screenwidth()}x{self.root7.winfo_screenheight()}')
        self.root7.config(bg="#ffcad4")
        F2=Frame(self.root7,bg='#bde0fe')
        F2.pack(expand=True,fill='both')
        f22=Frame(F2,bg='#bde0fe')
        f22.place(relx=0.5,rely=0.5,anchor='center')
        l1=Label(f22,text="Roll No")
        l1.grid(row=0,column=0,padx=10,pady=10)
        self.studentid=Entry(f22)
        self.studentid.grid(row=0,column=1,padx=10,pady=10)
        l2=Label(f22,text="Name")
        l2.grid(row=1,column=0,padx=10,pady=10)
        self.studentname=Entry(f22)
        self.studentname.grid(row=1,column=1,padx=10,pady=10)
        l3=Label(f22,text="Email")
        l3.grid(row=2,column=0,padx=10,pady=10)
        self.studentemail=Entry(f22)
        self.studentemail.grid(row=2,column=1,padx=10,pady=10)
        l4=Label(f22,text="Password")
        l4.grid(row=3,column=0,padx=10,pady=10)
        self.studentpass=Entry(f22,show='*')
        self.studentpass.grid(row=3,column=1,padx=10,pady=10)
        self.gender=StringVar(value='Male')
        l5=Label(f22,text="Gender")
        l5.grid(row=4,column=0,padx=10,pady=10)
        self.studentgender=Radiobutton(f22,text="Male",value="Male",variable=self.gender)
        self.studentgender.grid(row=4,column=1,padx=10,pady=10)
        self.studentgender1=Radiobutton(f22,text="Female",value="Female",variable=self.gender)
        self.studentgender1.grid(row=5,column=1,padx=10,pady=10)
        l6=Label(f22,text='Select Course')
        l6.grid(row=6,column=0,padx=10,pady=10)
        self.combo=Combobox(f22,values=self.courses)
        self.combo.grid(row=6,column=1,padx=10,pady=10)
        addstudent=Button(f22,text="Add student",command=self.addstudent)
        addstudent.grid(row=7,column=1,padx=10,pady=10)


        
    def view(self):
        nb=Notebook()
        nb.pack(expand=True,fill="both")
        

        F1=Frame(bg='#0077b6')
        F1.pack(expand=True,fill='both')
        f11=Frame(F1,bg='#0077b6')
        f11.place(relx=0.5,rely=0.5,anchor='center')
      
        l1=Label(f11,text="Email",font=("Arial",16),bg='#0077b6')
        l1.grid(row=0,column=0,padx=10,pady=10)
        self.studentemail=Entry(f11,font=("Arial",16))
        self.studentemail.grid(row=0,column=1,padx=10,pady=10)
        l2=Label(f11,text="Password",font=("Arial",16),bg='#0077b6')
        l2.grid(row=1,column=0,padx=10,pady=10)
        self.studentpass=Entry(f11,show='*',font=("Arial",16))
        self.studentpass.grid(row=1,column=1,padx=10,pady=10)
        btn=Button(f11,text="Login",font=("Arial",16),command=self.studentlog)
        btn.grid(row=2,column=1,padx=10,pady=10)
        btn1=Button(f11,text="Register",font=("Arial",16),command=self.studentregister)
        btn1.grid(row=3,column=1,padx=10,pady=10)

        nb.add(F1,text="Student Login")
        F2=Frame(bg='#f48c06')
        F2.pack(expand=True,fill='both')
        f22=Frame(F2,bg='#f48c06')
        f22.place(relx=0.5,rely=0.5,anchor='center')
      
        l1=Label(f22,text="Email",font=("Arial",16),bg='#f48c06')
        l1.grid(row=0,column=0,padx=10,pady=10)
        self.teacheremail=Entry(f22,font=("Arial",16))
        self.teacheremail.grid(row=0,column=1,padx=10,pady=10)
        l2=Label(f22,text="Password",font=("Arial",16),bg='#f48c06')
        l2.grid(row=1,column=0,padx=10,pady=10)
        self.teacherpass=Entry(f22,show='*',font=("Arial",16))
        self.teacherpass.grid(row=1,column=1,padx=10,pady=10)
        btn=Button(f22,text="Login",font=("Arial",16),command=self.teacherlog)
        btn.grid(row=2,column=1,padx=10,pady=10)

        nb.add(F2,text="Teacher Login")

        F3=Frame(bg='#f8ad9d')
        F3.pack(expand=True,fill='both')
        f33=Frame(F3,bg='#f8ad9d')
        f33.place(relx=0.5,rely=0.5,anchor='center')
      
        l1=Label(f33,text="Email",font=("Arial",16),bg='#f8ad9d')
        l1.grid(row=0,column=0,padx=10,pady=10)
        self.adminemail=Entry(f33,font=("Arial",16))
        self.adminemail.grid(row=0,column=1,padx=10,pady=10)
        l2=Label(f33,text="Password",font=("Arial",16),bg='#f8ad9d')
        l2.grid(row=1,column=0,padx=10,pady=10)
        self.adminpass=Entry(f33,show='*',font=("Arial",16))
        self.adminpass.grid(row=1,column=1,padx=10,pady=10)
        btn1=Button(f33,text="Login",font=("Arial",16),command=self.adminlogin)
        btn1.grid(row=2,column=1,padx=10,pady=10)

        nb.add(F3,text="Admin Login")
obj=Main()


