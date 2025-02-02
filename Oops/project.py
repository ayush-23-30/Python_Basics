class Student :
  def __init__(self, roll_No, name, class_name):
    self.roll_no = roll_No
    self.name = name
    self.class_name = class_name
    self.marks = {}
  def add_marks (self, subject, marks):
    if(subject in self.marks):
      print(f"{self.marks} already register")
    else : 
      self.marks[subject]  = marks; 

  def calc_avg_marks(self):
        if not self.marks:
            print("There are no available marks")
            return 0  # Returning 0 if no marks are available
        total_marks = sum(self.marks.values())
        average_marks = total_marks / len(self.marks)
        return average_marks

  def display_student_info(self):
        print("Student Information")
        print(f"Roll no: {self.roll_no}")
        print(f"Name: {self.name}")
        print(f"Class name: {self.class_name}")
        print(f"Marks: {self.marks}")
        print(f"Average: {self.calc_avg_marks()}")

  
std1 = Student(1,"ayush", "XI"); 
std2 = Student(2,"sahu", "X"); 
std3 = Student(3,"anuj", "XII"); 
std4 = Student(4,"vishal", "IX"); 

std1.add_marks("hindi", 89);
std1.add_marks("eng", 100);
std1.add_marks("maths", 70);

std2.add_marks("hindi", 90);
std2.add_marks("eng", 10);
std2.add_marks("maths", 170);

std3.add_marks("hindi", 32);
std3.add_marks("eng", 65);
std3.add_marks("maths", 66);

std4.add_marks("hindi", 90);
std4.add_marks("eng", 40);
std4.add_marks("maths", 10);

std1.display_student_info();
# std2.display_student_info();
# std3.display_student_info();
# std4.display_student_info();
