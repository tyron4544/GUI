from tkinter import *; from add_student import AddStudent; from student import StudentInfo; from searchstudent import SearchStudent; from print_all_students import PrintAllStudent; from info import ViewMyInformation
win = Tk()
def clear_content(frame):
    for widget in frame.winfo_children(): widget.destroy()
def login():
    def search():
        idstu = idnum.get()
        with open("student_data.txt", "r") as file: data = file.readlines()
        found = False
        for line in data:
            student_info = line.strip().split(", ")
            if idstu == student_info[2]:
                win.destroy()
                main(student_info)
                found = True
                break
        if not found: lbl2.config(text="Student NOT found", fg="red")
    def clear():
        idnum.delete(0, END)
        lbl2.config(text="")
    win.title("Login")
    win.config(bg="#212f3d")
    win.geometry(f"600x380+{int(win.winfo_screenwidth()/2 - 600/2)}+{int(win.winfo_screenheight()/2 - 380/2)}")
    lbl1 = Label(win, text="Enter Student ID Number:", font=("Segoe Print", 22), bg="#212f3d", fg="white")
    lbl1.place(x=80, y=70)
    idnum = Entry(win, font=("Segoe Print", 19))
    idnum.place(x=85, y=130)
    btn = Button(win, text="Submit", width=8, font=("Segoe Print", 15), bg="#2c3e50", fg="white", command=search)
    btn.place(x=85, y=200)
    btn1 = Button(win, text="Clear", width=8, font=("Segoe Print", 15), bg="#2c3e50", fg="white", command=clear)
    btn1.place(x=220, y=200)
    lbl2 = Label(win, text="", font=("Segoe Print", 22), bg="#212f3d", fg="white")
    lbl2.place(x=85, y=275)
def main(student_info):
    student_data = StudentInfo()
    main_win = Tk()
    main_win.title("Main Menu")
    main_win.geometry(f"900x700+{int(main_win.winfo_screenwidth()/2 - 900/2)}+{int(main_win.winfo_screenheight()/2 - 700/2)}")
    main_win.config(bg="#2c3e50")
    def logout():
        main_win.destroy(); global win; win = Tk()
        login()
    content_frame = Frame(main_win, bg="#2c3e50")
    content_frame.pack(side="right", fill="both", expand=True)
    add_student_instance = AddStudent(student_data, content_frame)
    search_student_instance = SearchStudent(student_data, content_frame, clear_content)
    print_all_instance = PrintAllStudent(student_data, content_frame, clear_content)
    view_info_instance = ViewMyInformation(content_frame, student_info)
    menu_div = Frame(main_win, bg="#212f3d")
    menu_div.pack(side="left", fill="y")
    Label(menu_div, text="Main Menu", width=23, font=("Segoe Print", 14), bg="#212f3d", fg="white", pady=15).grid(row=0, column=0)
    Button(menu_div, text="Add Student", width=21, font=("Segoe Print", 14), bg="#212f3d", fg="white",
           command=add_student_instance.display_add_student_form).grid(row=1, column=0, pady=10)
    Button(menu_div, text="Search Student", width=21, font=("Segoe Print", 14), bg="#212f3d", fg="white",
           command=search_student_instance.display_search_form).grid(row=2, column=0, pady=10)
    Button(menu_div, text="Print All Students", width=21, font=("Segoe Print", 14), bg="#212f3d", fg="white",
           command=print_all_instance.display_all_students).grid(row=3, column=0, pady=10)
    Button(menu_div, text="View My Information", width=21, font=("Segoe Print", 14), bg="#212f3d", fg="white",
           command=view_info_instance.display_info).grid(row=4, column=0, pady=10)
    Button(menu_div, text="Logout", width=21, font=("Segoe Print", 14), bg="#212f3d", fg="white", command=logout).grid(row=5, column=0, pady=10)
    main_win.mainloop()
login()
win.mainloop()
