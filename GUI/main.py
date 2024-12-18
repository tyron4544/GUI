from student import StudentInfo
from main_menu import MainMenu
from searchstudent import SearchStudent
from add_student import AddStudent
from print_all_students import PrintAllStudent

stu = StudentInfo()

addstud = AddStudent(stu, content_frame=None)  
printall = PrintAllStudent(stu, content_frame=None, clear_content=None)  
search = SearchStudent(stu, content_frame=None, clear_content=None)  

main_menu = MainMenu(addstud, printall, search,content_frame=None)

main_menu.display_menu()




