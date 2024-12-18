from tkinter import *
class ViewMyInformation:
    def __init__(self, content_frame, student_info):
        self.content_frame = content_frame  # Store the content_frame for GUI elements
        self.student_info = student_info  # Store the student information

    def display_info(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        Label(self.content_frame, text="My Information", font=("Segoe Print", 20), bg="#2c3e50", fg="white").pack(pady=10)

        labels = ["Name", "Age", "ID Number", "Email", "Phone Number"]
        for i, label in enumerate(labels):
            lbl = Label(self.content_frame, text=f"{label}: {self.student_info[i]}", font=("Segoe Print", 14), bg="#2c3e50", fg="white")
            lbl.pack(anchor="w", padx=20, pady=5)

