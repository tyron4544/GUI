from tkinter import *

class PrintAllStudent:
    def __init__(self, student_data, content_frame, clear_content):
        self.student_data = student_data
        self.content_frame = content_frame  # Store the content_frame for GUI elements
        self.clear_content = clear_content  # Store the clear_content function

    def print_all_students(self):
        print("==========================ALL STUDENT INFORMATION==============================")
        for student in self.student_data.allstudents:
            print(f"\nName: {student[0]}")  
            print(f"Age: {student[1]}")   
            print(f"ID Number: {student[2]}")  
            print(f"Email: {student[3]}")  
            print(f"Phone Number: {student[4]}")  
        print("==========================NOTHING FOLLOWS==============================")

    def display_all_students(self):
        self.clear_content(self.content_frame)  # Clear previous content
        Label(self.content_frame, text="All Students Information", font=("Segoe Print", 20), bg="#2c3e50", fg="white").pack(pady=10)

        # Create a frame to center the text area
        center_frame = Frame(self.content_frame, bg="#2c3e50")
        center_frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Create a Text widget to display all student information
        text_area = Text(center_frame, font=("Segoe Print", 7), bg="#2c3e50", fg="white", wrap="word")
        text_area.pack(side="left", expand=True, fill="both")


        # Insert student information into the text area
        for student in self.student_data.allstudents:
            text_area.insert("end", f"Name: {student[0]}\n")
            text_area.insert("end", f"Age: {student[1]}\n")
            text_area.insert("end", f"ID Number: {student[2]}\n")
            text_area.insert("end", f"Email: {student[3]}\n")
            text_area.insert("end", f"Phone Number: {student[4]}\n")
            text_area.insert("end", "-" * 20 + "\n")  # Separator line


