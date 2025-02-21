# print("new Project"); 

"""
add 
update 
delete 
veiw 
exit 
"""

# students = {
#   'paras' : 100, 
#   'gopal' : 200
# }

# access  print(students['gopal']);
#update =  student['key_name'] = new_valu
#delete del student ['key_name];

student_grades = { }

#add a new student 

def add_student (name, grade) :
  student_grades[name] = grade

  print(f"added {name} with a {grade}"); 


#update a student 
def update_student (name, grade):
  if name in student_grades :
    student_grades[name] = grade
    print(f"Updated name {name} and grades are {grade}")
  
  else : print(f" {name} is not found");

# add_student('xyz',00);
# print(student_grades);
# update_student('xyz', 902);
# print(student_grades);

def delete_student(name):
  if name in student_grades :
    del student_grades[name]
    print(f"{name} is deleted");
  else : print(f" {name} is not found");

def veiw_all_students ():
  if student_grades :
    for name , grades in student_grades.items():
      print(f"{name} : {grades}")
  else : print("No student Available"); 

# veiw_all_students()

def main():
  while(True):
    print('\n Student Grades Management System')
    print('1. Add a student')
    print('2. Update a student')
    print('3. Delete a student')
    print('4. View All student')
    print('5. Exit App'); 

    choice = int(input("Enter your Choice : ")); 

    if(choice == 1): 
      name = input("Enter Student Name = "); 
      grade = input("Enter Student Grade = "); 
      add_student(name, grade)
    elif (choice == 2):
      name = input("Enter Student Name = "); 
      grade = input("Enter Student Grade = "); 
      update_student(name, grade) 
    elif(choice == 3):
      name = input("Enter Student Name = "); 
      # grade = input("Enter Student Grade = "); 
      delete_student(name)
    elif (choice == 4):
      veiw_all_students(); 
    elif(choice == 5) :
      break;
    else : print("Enter a valid choice"); 

if __name__ == "__main__" :
  main();



