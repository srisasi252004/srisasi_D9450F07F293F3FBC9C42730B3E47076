class Student:

  def __init__(self, name, roll_number, cgpa):
     self.name = name
     self.roll_number = roll_number
     self.cgpa = cgpa


def sort_student(student_list):
  # sort the list of students in descending order of CGPA
  sorted_students = sorted(student_list,
                        key=lambda student: student.cgpa, 
                         reverse=True)
  #syntax _ lambda arg:exp
  return sorted_students


#Example usage:
students = [
     Student("Stephen", "A123", 7.8),
     Student("Karthik", "A124", 8.9),
     Student("Santhosh", "A125", 9.1),
     Student("Komban", "A126", 9.9),
 ]

sorted_students = sort_student(students)

 # Print the sorted list of students
for students in sorted_students:
  print("Name: {}, Roll Number: {}. CGPA  {}".format(students.name,
                                           students.roll_number,
                           students.cgpa))
