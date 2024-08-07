import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview

class StudentPanel:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("800x600")
        self.view()
        self.root.mainloop()

    def fetch_data(self):
        db = sqlite3.connect("attendancesystem.db")
        cr = db.cursor()
        cr.execute('''SELECT s.rollno, s.name, s.course, a.attendance, a.marks
                      FROM student s
                      LEFT JOIN attendance a ON s.rollno = a.rollno''')
        data = cr.fetchall()
        db.close()
        return data

    def view(self):
        self.tree = Treeview(self.root, columns=("Roll Number", "Name", "Course", "Attendance", "Marks"), show="headings")
        self.tree.heading("Roll Number", text="Roll Number")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Course", text="Course")
        self.tree.heading("Attendance", text="Attendance")
        self.tree.heading("Marks", text="Marks")
        self.tree.pack(fill="both", expand=True)

        data = self.fetch_data()
        print(data)
        for row in data:
            self.tree.insert('', 'end', values=row)
