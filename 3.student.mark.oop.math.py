import os
import curses
from curses.textpad import Textbox, rectangle
from curses import wrapper
import math
import numpy
from numpy import array

def getmark(stdscr, prompt, range):
      while True:
         try:
            value = float(InputBox(stdscr, prompt,0))
            if value > 0 and value <= range:
               return value
            else:
               stdscr.clear()
               print_center(stdscr ,"Invalid input. Please enter a positive, valid integer.\n")
               stdscr.refresh()
               stdscr.getch()
         except Exception:
            stdscr.clear()
            print_center(stdscr ,("Invalid input. Please enter an integer.\n")) 
            stdscr.refresh()
            stdscr.getch()

def check_and_get_positive(stdscr, prompt, range):
      while True:
         try:
            value = int(InputBox(stdscr, prompt,0))
            if value > 0 and value <= range:
               return value
            else:
               stdscr.clear()
               print_center(stdscr ,"Invalid input. Please enter a positive, valid integer.\n")
               stdscr.refresh()
               stdscr.getch()
         except Exception:
            stdscr.clear()
            print_center(stdscr ,("Invalid input. Please enter an integer.\n")) 
            stdscr.refresh()
            stdscr.getch()

def InputBox(stdscr, text, yoffset):
    curses.curs_set(1)
    h, w = stdscr.getmaxyx()
    x = w//2 - len(text)//2
    y = h//2+yoffset
    stdscr.clear()
    
    stdscr.addstr(y//2, x, text)

    # Get the dimensions of the terminal window
    height, width = stdscr.getmaxyx()

    # Calculate the center coordinates for the box
    box_height = 1
    box_width = 40
    box_y = (height - box_height) // 2+yoffset
    box_x = (width - box_width) // 2

    # Create the box window
    editwin = curses.newwin(box_height, box_width, box_y+yoffset, box_x)
    rectangle(stdscr, box_y - 1, box_x - 1, box_y + box_height + yoffset, box_x + box_width)
    stdscr.refresh()

    box = Textbox(editwin)
    box.edit()

    InputThing = box.gather()
    if InputBox != '' :
      return InputThing
    else :
      return 0

class Entity:
   def __init__(self, stdscr):
      self.__id = None
      self.__name = None
      self.stdscr = stdscr

   def set_id(self, id):
      self.__id = id
   
   def set_name(self, name):
      self.__name = name

   def get_id(self):
      return self.__id

   def get_name(self):
      return self.__name

   def list(self):
      h, table_width = self.stdscr.getmaxyx()
      id_column_width = 20
      name_column_width = table_width - id_column_width - 7

      id_str = str(self.get_id()).ljust(id_column_width)
      name_str = str(self.get_name()).ljust(name_column_width)

      table_row = f"| {id_str} | {name_str} |"

      self.stdscr.addstr(table_row)
      self.stdscr.addstr("-" * table_width)

   def input(self):
      entity_count = self.check_and_get_positive(self.stdscr,"Enter the number of Entity: ", 100)
      entities = []
      for i in range(entity_count):
         entity_id = InputBox(self.stdscr,f"Enter ID for Entity {i+1}: ",0)
         name = InputBox(self.stdscr,f"Enter name for Entity {i+1}: ",0)
         entity = Entity(self.stdscr)
         entity.set_id(entity_id)
         entity.set_name(name)
         entities.append(entity)    
      return entities
   
           # Add a new line after getting input

class Student(Entity):
   def __init__(self, stdscr):
      super().__init__(stdscr)
      self.__dob = None

   def set_dob(self, dob):
      self.__dob = dob

   def get_dob(self):
      return self.__dob
   
   def input(self):
      temp = []
      student_count = check_and_get_positive(self.stdscr,"Enter the number of students: ",100)
      if student_count != 0 :
         for i in range(student_count):
            student_id = InputBox(self.stdscr,f"Enter student ID for student {i+1}: ",0)
            name = InputBox(self.stdscr,f"Enter student name for student {i+1}: ",0)
            dob = InputBox(self.stdscr,f"Enter student date of birth for student {i+1}: ",0)
            student = Student(self.stdscr)
            student.set_id(student_id)
            student.set_name(name)
            student.set_dob(dob)
            temp.append(student)    
         return temp
      else:
          return

class Course(Entity):
   def __init__(self, stdscr):
      super().__init__(stdscr)
      self.__credits = None
      self.__marks = {}

   def get_credits(self):
      return self.__credits
   
   def list(self, stdscr):
      h, table_width = self.stdscr.getmaxyx()
      id_column_width = 20
      name_column_width = int((table_width - id_column_width - 7)/2)
      mark_column_width = table_width - id_column_width - name_column_width - 8
      id_str = self.get_id().ljust(id_column_width)
      name_str = self.get_name().ljust(name_column_width)
      credits_str = self.get_credits().ljust(mark_column_width)
      table_row = f"| {id_str} | {name_str} | {credits_str}"

      self.stdscr.addstr(table_row)
      self.stdscr.addstr("-" * table_width)
   
   def set_credits(self, credits):
      self.__credits = credits
   
   def get_marks(self):
      return self.__marks

   def set_marks(self, student_id, mark):
      self.__marks[student_id] = mark

   def input(self, students):
      courses=[]
      course_count = check_and_get_positive(self.stdscr,"Enter the number of courses: ", 10)
      if course_count != 0 :
         for i in range(course_count):
            course_id = InputBox(self.stdscr,f"Enter course ID for course {i+1}: ",0)
            name = InputBox(self.stdscr,f"Enter course name for course {i+1}: ",0)
            credits = check_and_get_positive(self.stdscr,"Enter number of credits", 10)
            course = Course(self.stdscr)
            course.set_id(course_id)
            course.set_name(name)
            course.set_credits(credits)
            courses.append(course)
         return courses
      else:
          return      

class SchoolSystem(Entity):
   def __init__(self, stdscr):
      self.stdscr = stdscr
      self.students = []
      self.courses = []
   
   def calculate_average_gpa(self, student):
      total_credits = 0
      weighted_sum = 0

      for course in self.courses:
                     if student.get_id() in course.get_marks():
                        mark = course.get_marks()[student.get_id()]
                        credits = course.get_credits()
                        total_credits += credits
                        weighted_sum += mark * credits
      if total_credits == 0:
                     return 0

      average_gpa = weighted_sum / total_credits* (4/10)
      return round(average_gpa, 1)

   def sort_students_by_gpa(self):
      self.students.sort(key=lambda student: self.calculate_average_gpa(student), reverse=True)

   def list_courses(self):
      h, table_width = self.stdscr.getmaxyx()
      id_column_width = 20
      name_column_width = int((table_width - id_column_width - 7)/2)
      mark_column_width = table_width - id_column_width - name_column_width - 8
      id_str = "ID".ljust(id_column_width)
      name_str = "NAME".ljust(name_column_width)
      credits_str = "CREDITS".ljust(mark_column_width)
      table_row = f"| {id_str} | {name_str} | {credits_str}"

      print_center_top(self.stdscr,"LIST OF COURSES")
      self.stdscr.addstr(table_row)
      self.stdscr.addstr("-" * table_width)

      for course in self.courses:
         course.list(self.stdscr)

   def list_students(self):
      h, table_width = self.stdscr.getmaxyx()
      id_column_width = 20
      name_column_width = table_width - id_column_width - 7
      id_str = "ID".ljust(id_column_width)
      name_str = "NAME".ljust(name_column_width)
      table_row = f"| {id_str} | {name_str} |"

      print_center_top(self.stdscr,"LIST OF STUDENTS")
      self.stdscr.addstr(table_row)
      self.stdscr.addstr("-" * table_width)
      for student in self.students:
         student.list()

   def show_student_marks(self, course):
      if course.get_marks() == {}:
         print_center(self.stdscr,("No mark added yet :("))
         return
      print_center_top(self.stdscr,f"STUDENT MARKS OF {course.get_name()} COURSE")

      h, table_width = self.stdscr.getmaxyx()
      id_column_width = 20
      name_column_width = int((table_width - id_column_width - 7) / 2)
      mark_column_width = table_width - id_column_width - name_column_width - 8
      id_str = "ID".ljust(id_column_width)
      name_str = "NAME".ljust(name_column_width)
      mark_str = "MARK".ljust(mark_column_width)
      table_row = f"| {id_str} | {name_str} | {mark_str}"
      self.stdscr.addstr(table_row)
      self.stdscr.addstr("-" * table_width)

      for student_id, mark in course.get_marks().items():
         student = self.student_by_id(student_id)
         id_str = str(student.get_id()).ljust(id_column_width)
         name_str = str(student.get_name()).ljust(name_column_width)
         mark_str = str(mark).ljust(mark_column_width)

         table_row = f"| {id_str} | {name_str} | {mark_str}"

         self.stdscr.addstr(table_row)
         self.stdscr.addstr("-" * table_width)
      self.stdscr.refresh()

   def student_by_id(self, student_id):
      for student in self.students:
         if student.get_id() == student_id:
            return student
      return None

   def list_gpa(self):
      h, table_width = self.stdscr.getmaxyx()
      id_column_width = 20
      name_column_width = int((table_width - id_column_width - 7) / 2)
      mark_column_width = table_width - id_column_width - name_column_width - 8
      id_str = "ID".ljust(id_column_width)
      name_str = "NAME".ljust(name_column_width)
      gpa_str = "MARK".ljust(mark_column_width)
      table_row = f"| {id_str} | {name_str} | {gpa_str}"

      self.stdscr.addstr(table_row)
      self.stdscr.addstr("-" * table_width)
      print_center_top(self.stdscr, "LIST OF STUDENTS'S GPA")
      self.stdscr.addstr(table_row)
      self.stdscr.addstr("-" * table_width)
      self.stdscr.refresh()
      for student in self.students:
         id_str = str(student.get_id()).ljust(id_column_width)
         name_str = str(student.get_name()).ljust(name_column_width)
         gpa = self.calculate_average_gpa(student)
         mark_str = str(gpa).ljust(mark_column_width)
         table_row = f"| {id_str} | {name_str} | {mark_str}"
         self.stdscr.addstr(table_row)
         self.stdscr.addstr("-" * table_width)
      self.stdscr.refresh()

menu = [
      "1. List Courses",
      "2. List Students",
      "3. Show Student Marks for a Course",
      "4. Add Student",
      "5. Add Course",
      "6. Add Marks for a Student in a Course",
      "7. List GPA",
      "8. Exit"
   ]

option = ['1','2','3','4','5','6','7','8']


def print_menu(stdscr, selected_row_idx, menu):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for idx, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()

def print_center(stdscr, text):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w//2 - len(text)//2
    y = h//2
    stdscr.addstr(y, x, text)
    stdscr.refresh()

def print_center_top(stdscr, text):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = 0
    y = h-h
    textlength = len(text)
    space = (w - textlength)//2
    for i in range(int(space)):
       stdscr.addstr("-")
    stdscr.addstr(text)
    for i in range(int(space)):
       stdscr.addstr("-")
    stdscr.refresh()


def menu_function(stdscr,user_choice):
      if user_choice == '1':
         os.system('cls')
         if school.courses == []:
            print_center(stdscr,("You haven't add any courses yet"))
         else:
            school.list_courses()
      elif user_choice == '2':
         os.system('cls')
         if school.students == []:
            print_center(stdscr,("You haven't add any student yet"))
         else:
            school.list_students()
      elif user_choice == '3':
         os.system('cls')
         if school.courses == []:
            print_center(stdscr,("You haven't add any courses yet"))
         else :
            select_menu = []
            current_row = 0
            i = 1
            for course in school.courses:
               select_menu = select_menu +  [ f"{i}." + course.get_name()]
               i = i + 1
            select_menu = select_menu + [f"{i}.Exit"]
            
            while 1:
               print_menu(stdscr, current_row, select_menu)
               key = stdscr.getch()
                  
               if key == curses.KEY_UP and current_row > 0:
                     current_row -= 1
               elif key == curses.KEY_DOWN and current_row < len(select_menu)-1:
                     current_row += 1
               elif key == curses.KEY_ENTER or key in [10, 13]:
                     print_center(stdscr, "You selected '{}'".format(select_menu[current_row]))
                     stdscr.getch()
                  # if user selected last row, exit the program
                     if current_row != len(select_menu)-1:
                        stdscr.clear()
                        course_choice = current_row
                        break
                     else:
                        course_choice = None
                        stdscr.clear()
                        break
            if(course_choice != len(select_menu)-1):
               school.show_student_marks(school.courses[course_choice])

      elif user_choice == '4':
         os.system('cls')
         new_students = Student_list.input()
         school.students.extend(new_students)
         print_center(stdscr,("Students added successfully!"))
      elif user_choice == '5':
         os.system('cls')
         new_courses = Course_list.input(school.students)
         school.courses.extend(new_courses)
         print_center(stdscr,("Courses added successfully!"))
      elif user_choice == '6':
         select_menu = []
         current_row = 0
         i = 1
         for course in school.courses:
            select_menu = select_menu +  [ f"{i}." + course.get_name()]
            i = i + 1
         select_menu = select_menu + [f"{i}.Exit"]
         
         while 1:
            print_menu(stdscr, current_row, select_menu)
            key = stdscr.getch()
               
            if key == curses.KEY_UP and current_row > 0:
                  current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(select_menu)-1:
                  current_row += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                  print_center(stdscr, "You selected '{}'".format(select_menu[current_row]))
                  stdscr.getch()
               # if user selected last row, exit the program
                  if current_row != len(select_menu)-1:
                     stdscr.clear()
                     course_choice = current_row
                     break
                  else:
                     course_choice = None
                     stdscr.clear()
                     break
         i = 1
         select_menu = []
         current_row = 0
         for student in school.students:
                  select_menu = select_menu +  [ f"{i}." + student.get_name()]
                  i = i + 1
         select_menu = select_menu + [f"{i}.Exit"]

         while (course_choice != None):
                  print_menu(stdscr, current_row, select_menu)
                  key = stdscr.getch()
                     
                  if key == curses.KEY_UP and current_row > 0:
                        current_row -= 1
                  elif key == curses.KEY_DOWN and current_row < len(select_menu)-1:
                        current_row += 1
                  elif key == curses.KEY_ENTER or key in [10, 13]:
                        print_center(stdscr, "You selected '{}'".format(select_menu[current_row]))
                        stdscr.getch()
                     # if user selected last row, exit the program
                        if current_row != len(select_menu)-1:
                           stdscr.clear()
                           student_choice = current_row
                           break
                        else:
                           stdscr.clear()
                           student_choice = None
                           break

         if (course_choice != None ) and (student_choice != None):
            try :
               mark = float(getmark(stdscr,(f"Enter marks from 0 to 10 for {school.students[student_choice].get_name()} "
                        f"({school.students[student_choice].get_id()}) in "
                        f"{school.courses[course_choice].get_name()}: "),10))
               school.courses[course_choice].set_marks(school.students[student_choice].get_id(), mark)
               print_center(stdscr,("Marks added successfully!"))
            except ValueError:
                print_center(stdscr,("Wrong Input, Please Input a float number!"))
         else:
            print_center(stdscr,("Wrong input"))


               
      elif user_choice == '7':
         school.list_gpa()

def main(stdscr):
    
    global school
    school = SchoolSystem(stdscr)
    global Student_list
    Student_list = Student(stdscr)
    global Course_list
    Course_list = Course(stdscr)
    exit = False
    # turn off cursor blinking
    curses.curs_set(0)

    # color scheme for selected row
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # specify the current selected row
    current_row = 0

    # print the menu
    print_menu(stdscr, current_row, menu)

    while not (exit):
        key = stdscr.getch()
         
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu)-1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            print_center(stdscr, "You selected '{}'".format(menu[current_row]))
            stdscr.getch()
    		# if user selected last row, exit the program
            if current_row == len(menu)-1:
               stdscr.clear()
               print_center(stdscr, "Exiting program. Goodbye!")
               stdscr.refresh()
               stdscr.getch()
               exit = True
               break
            else:
               menu_function(stdscr,option[current_row])
               stdscr.getch()

        print_menu(stdscr, current_row, menu)


wrapper(main)
