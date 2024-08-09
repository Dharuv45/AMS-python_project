from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter.ttk import Treeview, Notebook,Combobox
from datetime import date

class Teacher:
    def __init__(self, name, email):
        self.root4 = Tk()
        self.root4.geometry(f'{self.root4.winfo_screenwidth()}x{self.root4.winfo_screenheight()}')
        l=Label(text=f'Hey {name}')
        l.place(anchor='nw',relx=0,rely=0)
        b=Button(text='logout')
        b.place(relx=1,rely=1,anchor='se')
        self.email=email
        self.view()
        self.root4.mainloop()

    def attendance(self):
        db = sqlite3.connect("attendancesystem.db")
        cr = db.cursor()
        today_str = date.today().isoformat()
        cr.execute(f'''select * from attendance where Date='{today_str}'  ''')
        data=cr.fetchall()
        print(data)
        if len(data)==0:
            for i in range(len(self.check_values)):
                cr.execute(f'''insert into attendance values({self.labels_roll[i]['text']},'{today_str}','{self.check_values[i].get()}')''')
                db.commit()
            messagebox.showinfo("Success","Attendance Marked successfully")
        else:
            messagebox.showerror("Error","Attendance Already Marked ")


    def getstudents(self):
        db = sqlite3.connect("attendancesystem.db")
        cr = db.cursor()
        
        cr.execute(f"SELECT * FROM teacher WHERE email='{self.email}'")
        self.data = cr.fetchone()
        self.course = self.data[5]
        cr.execute(f"SELECT * FROM student WHERE course='{self.course}'")
        data1 = cr.fetchall()

        for i in data1:
            self.tree.insert('', 'end', values=i)
        self.labels_roll=[]
        self.labels_name=[]
        self.check_values=[]
        l=Label(self.f22,text="Roll No")
        l.grid(row=0,column=0,padx=5,pady=5)
        l1=Label(self.f22,text="Name")
        l1.grid(row=0,column=1,padx=5,pady=5)
        l2=Label(self.f22,text="Attendance")
        l2.grid(row=0,column=2,padx=5,pady=5)

        for i in range(len(data1)):
            l=Label(self.f22,text=data1[i][0])
            l.grid(row=i+1,column=0)
            l1=Label(self.f22,text=data1[i][1])
            l1.grid(row=i+1,column=1)
            self.check_values.append(StringVar(value="Absent"))
            check=Checkbutton(self.f22,text='Present',onvalue="Present",offvalue="Absent",variable=self.check_values[i])
            check.grid(row=i+1,column=2)

            self.labels_roll.append(l)
            self.labels_name.append(l1)
            
        btn=Button(self.f22,text="Mark Attendance", command=self.attendance)
        btn.grid(row=len(data1)+1,column=1)    


    def updateprofile(self):
        db=sqlite3.connect("attendancesystem.db")
        cr=db.cursor()
        cr.execute(f'''update teacher set name='{self.teachername.get()}',password='{self.teacherpass.get()}' where email='{self.email}' ''') 
        db.commit()
        messagebox.showinfo("Success","Profile Updated Succcessfully")   

    def logout(self):
        self.root4.destroy()
        import mainpanel  

    def view(self):
        nb = Notebook(self.root4)
        nb.pack(expand=True, fill='both')
        
        F1 = Frame(nb, bg='#dee2ff')
        nb.add(F1, text='Students')
        F1.pack(expand=True, fill='both')
        
        f11 = Frame(F1, bg='#dee2ff')
        f11.place(relx=0.5, rely=0.5, anchor='center')
        
        self.tree = Treeview(f11, columns=("rollno", "name"), show='headings')
        self.tree.heading("rollno", text="Roll No")
        self.tree.heading("name", text="Name")
        self.tree.pack(expand=True, fill='both')

        nb.add(F1, text='View Students')
        F2 = Frame(bg='#dee2ff')
        F2.pack(expand=True, fill='both')
        self.f22=Frame(F2,bg='#dee2ff')
        self.f22.place(relx=0.5,rely=0.5,anchor='center')
        nb.add(F2,text="Mark Attendance")
        self.getstudents()

        F3 = Frame(bg='#dee2ff')
        F3.pack(expand=True, fill='both')
        self.f33=Frame(F3,bg='#dee2ff')
        self.f33.place(relx=0.5,rely=0.5,anchor='center')
        list_data=[StringVar(value=self.data[i]) for i in range(len(self.data))]

        l1 = Label(self.f33, text="Employee ID")
        l1.grid(row=0, column=0, padx=10, pady=10)
        self.teacherid = Entry(self.f33,textvariable=list_data[0],state='disabled')
        self.teacherid.grid(row=0, column=1, padx=10, pady=10)

        l2 = Label(self.f33, text="Name")
        l2.grid(row=1, column=0, padx=10, pady=10)
        self.teachername = Entry(self.f33,textvariable=list_data[1])
        self.teachername.grid(row=1, column=1, padx=10, pady=10)

        l3 = Label(self.f33, text="Email")
        l3.grid(row=2, column=0, padx=10, pady=10)
        self.teacheremail = Entry(self.f33,textvariable=list_data[2],state='disabled')
        self.teacheremail.grid(row=2, column=1, padx=10, pady=10)

        l4 = Label(self.f33, text="Password")
        l4.grid(row=3, column=0, padx=10, pady=10)
        self.teacherpass = Entry(self.f33,show="*",textvariable=list_data[3])
        self.teacherpass.grid(row=3, column=1, padx=10, pady=10)


        l6 = Label(self.f33, text="Assign Course")
        l6.grid(row=4, column=0, padx=10, pady=10)
        self.combo = Entry(self.f33,textvariable=list_data[5],state='disabled')
        self.combo.grid(row=4, column=1, padx=10, pady=10)
        addteacher = Button(self.f33, text="Update Profile",command=self.updateprofile)
        addteacher.grid(row=5, column=1, padx=10, pady=10)

        logbtn = Button(self.f33, text="Logout",command=self.logout)
        logbtn.grid(row=6, column=1, padx=10, pady=10)

        nb.add(F3,text="Update Profile")
