from tkinter import *

class SearchStudent:
    def __init__(self, student_data, content_frame, clear_content):
        self.student_data = student_data
        self.content_frame = content_frame
        self.clear_content = clear_content
        self.allstudents = []  # Initialize an empty list for students
        self.read_file()  # Load students when the class is instantiated

    def search_by_id(self):
        id_to_search = input("Enter ID Number to search: ")
        found = False
        for student in self.student_data.allstudents:
            if student[2] == id_to_search:  
                print("\n===== Student Found =====")
                print(f"Name: {student[0]}")
                print(f"Age: {student[1]}")
                print(f"ID Number: {student[2]}")
                print(f"Email: {student[3]}")
                print(f"Phone Number: {student[4]}")
                print("=========================\n")
                found = True
                break
        if not found:
            print("Student not found!")
    
    def read_file(self):
        try: 
            with open("student_data.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    student_data = line.strip().split(", ")
                    if len(student_data) == 5:  # Ensure there are 5 fields
                        # Create a dictionary for each student
                        student_dict = {
                            "name": student_data[0],
                            "age": student_data[1],
                            "idnum": student_data[2],
                            "email": student_data[3],
                            "phone": student_data[4]
                        }
                        self.allstudents.append(student_dict)
                    else:
                        print(f"Invalid student data line: {line}")
            print("All students loaded.")
        except FileNotFoundError:
            print("No existing student data found")

    def display_search_form(self):
        self.clear_content(self.content_frame)
        Label(self.content_frame, text="Search Student", font=("Segoe Print", 20), bg="#2c3e50", fg="white").pack(pady=10)

        Label(self.content_frame, text="Enter Student ID Number:", font=("Segoe Print", 14), bg="#2c3e50", fg="white").pack(pady=10)
        self.id_entry = Entry(self.content_frame, font=("Segoe Print", 14))
        self.id_entry.pack(pady=10)

        Button(self.content_frame, text="Search", font=("Segoe Print", 14), command=self.search_student).pack(pady=10)

        self.result_label = Label(self.content_frame, text="", font=("Segoe Print", 14), bg="#2c3e50", fg="white")
        self.result_label.pack(pady=10)

    def search_student(self):
        student_id = self.id_entry.get()
        student = self.get_student_by_id(student_id)  # Call the new method
        if student:
            self.result_label.config(text=f"Name: {student['name']}\nAge: {student['age']}\nEmail: {student['email']}\nPhone: {student['phone']}")
        else:
            self.result_label.config(text="Student NOT found")

    def get_student_by_id(self, student_id):
        # Search for the student by ID number in the loaded data
        for student in self.allstudents:
            if student["idnum"] == student_id:  # Match by ID number
                return student
        return None  # Return None if student not found


    
    