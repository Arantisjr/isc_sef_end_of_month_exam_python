class Person:
      def __init__(self,name,age):
            self.name = name
            self.name = age

class Student(Person):
      def __init__(self, name, age,student_id,grades):
            self.name = name
            self.name = age
            self.student_id = student_id
            self.grades = grades
           

      def calculate_average(grades):
            average_grade = (grades/5)*100
            print(f"student average:{average_grade}")
      def display_details(name, age,student_id,grades):
            print(f"student_name:{name},student_age:{age},grades:{grades},sudent_id:{student_id}")
     
            

student1 = Student.display_details("arantis")