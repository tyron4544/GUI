from tkinter import *

class AddStudent:
    def __init__(self, student_data, content_frame):
        self.student_data = student_data
        self.content_frame = content_frame  

    def input_details_student(self, name, age, idnum, email, phone):
        self.addstudent(name, age, idnum, email, phone)
    
    def input_details_students(self):
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        idnum = input("Enter IDNumber: ")
        email = input("Enter Email: ")
        phone = input("Enter Phone Number: ")
        self.addstudent(name, age, idnum, email, phone)

    def addstudent(self, name, age, idnum, email, phone):
        self.student_data.set_name(name)
        self.student_data.set_age(age)
        self.student_data.set_id_num(idnum)
        self.student_data.set_email(email)
        self.student_data.set_phone_number(phone)
        student = [name, age, idnum, email, phone]
        self.student_data.allstudents.append(student)
        student_str = f"{name}, {age}, {idnum}, {email}, {phone}"
        self.write_to_file(student_str)
        print("Student Data added to the database")  

    def write_to_file(self, student):
        with open("student_data.txt", "a+") as file:
            for x in student:
                file.write(f"{x}")
            file.write("\n")
            file.close()
    print("Student Data added to the database")


    def display_add_student_form(self):

        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        Label(self.content_frame, text="Add New Student", font=("Segoe Print", 20), bg="#2c3e50", fg="white").pack(pady=10)

        center_frame = Frame(self.content_frame, bg="#2c3e50")
        center_frame.pack(expand=True)

        input_frame = Frame(center_frame, bg="#2c3e50")
        input_frame.pack(pady=20)

        labels = ["Name", "Age", "ID Number", "Email", "Phone Number"]
        entries = {}

        for label in labels:
            lbl = Label(input_frame, text=f"{label}:", font=("Segoe Print", 14), bg="#2c3e50", fg="white")
            lbl.pack(anchor="w", padx=20, pady=5)
            entry = Entry(input_frame, font=("Segoe Print", 12))
            entry.pack(anchor="w", padx=20, pady=5)
            entries[label] = entry

        def save_student():
            name = entries["Name"].get()
            age = entries["Age"].get()
            idnum = entries["ID Number"].get()
            email = entries["Email"].get()
            phone = entries["Phone Number"].get()
            self.input_details_student(name, age, idnum, email, phone)
            Label(input_frame, text="Student Added Successfully!", fg="green", bg="#2c3e50", font=("Segoe Print", 14)).pack(pady=10)

        Button(input_frame, text="Add Student", font=("Segoe Print", 14), bg="#2c3e50", fg="white", command=save_student).pack(pady=10)
