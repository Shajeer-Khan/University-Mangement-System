#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import ttk, messagebox

class UniversityManagementSystem:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("University Management System")

        # Create tabs
        self.tab_control = ttk.Notebook(self.window)
        self.tab_control.pack(expand=1, fill="both")

        self.student_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.student_tab, text="Student")

        self.faculty_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.faculty_tab, text="Faculty")

        self.course_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.course_tab, text="Course")

        # Student tab
        self.student_label = tk.Label(self.student_tab, text="Student Information")
        self.student_label.pack()

        self.student_name_label = tk.Label(self.student_tab, text="Name:")
        self.student_name_label.pack()
        self.student_name_entry = tk.Entry(self.student_tab)
        self.student_name_entry.pack()

        self.student_roll_number_label = tk.Label(self.student_tab, text="Roll Number:")
        self.student_roll_number_label.pack()
        self.student_roll_number_entry = tk.Entry(self.student_tab)
        self.student_roll_number_entry.pack()

        self.student_course_label = tk.Label(self.student_tab, text="Course:")
        self.student_course_label.pack()
        self.student_course_entry = tk.Entry(self.student_tab)
        self.student_course_entry.pack()

        self.student_add_button = tk.Button(self.student_tab, text="Add Student", command=self.add_student)
        self.student_add_button.pack()

        # Faculty tab
        self.faculty_label = tk.Label(self.faculty_tab, text="Faculty Information")
        self.faculty_label.pack()

        self.faculty_name_label = tk.Label(self.faculty_tab, text="Name:")
        self.faculty_name_label.pack()
        self.faculty_name_entry = tk.Entry(self.faculty_tab)
        self.faculty_name_entry.pack()

        self.faculty_designation_label = tk.Label(self.faculty_tab, text="Designation:")
        self.faculty_designation_label.pack()
        self.faculty_designation_entry = tk.Entry(self.faculty_tab)
        self.faculty_designation_entry.pack()

        self.faculty_course_label = tk.Label(self.faculty_tab, text="Course:")
        self.faculty_course_label.pack()
        self.faculty_course_entry = tk.Entry(self.faculty_tab)
        self.faculty_course_entry.pack()

        self.faculty_add_button = tk.Button(self.faculty_tab, text="Add Faculty", command=self.add_faculty)
        self.faculty_add_button.pack()

        # Course tab
        self.course_label = tk.Label(self.course_tab, text="Course Information")
        self.course_label.pack()

        self.course_name_label = tk.Label(self.course_tab, text="Name:")
        self.course_name_label.pack()
        self.course_name_entry = tk.Entry(self.course_tab)
        self.course_name_entry.pack()

        self.course_code_label = tk.Label(self.course_tab, text="Code:")
        self.course_code_label.pack()
        self.course_code_entry = tk.Entry(self.course_tab)
        self.course_code_entry.pack()

        self.course_add_button = tk.Button(self.course_tab, text="Add Course", command=self.add_course)
        self.course_add_button.pack()

    def add_student(self):
        student_name = self.student_name_entry.get()
        student_roll_number = self.student_roll_number_entry.get()
        student_course = self.student_course_entry.get()

        # Add student to database
        print(f"Student added: {student_name}, {student_roll_number}, {student_course}")

    def add_faculty(self):
        faculty_name = self.faculty_name_entry.get()
        faculty_designation = self.faculty_designation_entry.get()
        faculty_course = self.faculty_course_entry.get()

        # Add faculty to database
        print(f"Faculty added: {faculty_name}, {faculty_designation}, {faculty_course}")

    def add_course(self):
        course_name = self.course_name_entry.get()
        course_code = self.course_code_entry.get()

        # Add course to database
        print(f"Course added: {course_name}, {course_code}")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    university_management_system = UniversityManagementSystem()
    university_management_system.run()

