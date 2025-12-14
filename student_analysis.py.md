\# Student Academic Performance Analysis System



student\_name = "Rasheed Fatia"

matric\_number = "23/60AC389"

age = 22

cgpa = 4.81

is\_active = True

courses\_registered = \["Python", "Data Science", "Statistics"]

grades = {"Python": "A", "Data Science": "A", "Statistics": "B"}



students = \[]



student1 = {

&nbsp;   "name": "Rasheed Fatia",

&nbsp;   "matric": "23/60AC389",

&nbsp;   "age": 22,

&nbsp;   "cgpa": 4.81,

&nbsp;   "is\_active": True,

&nbsp;   "courses": \["Python", "Data Science", "Statistics"],

&nbsp;   "outstanding": 0

}



student2 = {

&nbsp;   "name": "Yusuf Adeoye",

&nbsp;   "matric": "23/70JC093",

&nbsp;   "age": 21,

&nbsp;   "cgpa": 3.45,

&nbsp;   "is\_active": True,

&nbsp;   "courses": \["Python", "Statistics"],

&nbsp;   "outstanding": 0

}



student3 = {

&nbsp;   "name": "Moses Oyedele",

&nbsp;   "matric": "23/50BC102",

&nbsp;   "age": 24,

&nbsp;   "cgpa": 2.90,

&nbsp;   "is\_active": True,

&nbsp;   "courses": \["Python"],

&nbsp;   "outstanding": 1

}



student4 = {

&nbsp;   "name": "Timi Abidoye",

&nbsp;   "matric": "23/40DS111",

&nbsp;   "age": 23,

&nbsp;   "cgpa": 4.10,

&nbsp;   "is\_active": False,

&nbsp;   "courses": \["Data Science"],

&nbsp;   "outstanding": 0

}



student5 = {

&nbsp;   "name": "Nimah Nina",

&nbsp;   "matric": "23/20CS205",

&nbsp;   "age": 20,

&nbsp;   "cgpa": 3.80,

&nbsp;   "is\_active": True,

&nbsp;   "courses": \["Python", "Algorithms"],

&nbsp;   "outstanding": 0

}



students.extend(\[student1, student2, student3, student4, student5])



student\_names = \[s\["name"] for s in students]



unique\_courses = set()

for s in students:

&nbsp;   unique\_courses.update(s\["courses"])



department\_info = ("Religion Department", "Faculty of Technology", 2025)





def score\_to\_grade(score):

&nbsp;   if score >= 70:

&nbsp;       grade = "A"

&nbsp;   elif score >= 60:

&nbsp;       grade = "B"

&nbsp;   elif score >= 50:

&nbsp;       grade = "C"

&nbsp;   elif score >= 45:

&nbsp;       grade = "D"

&nbsp;   elif score >= 40:

&nbsp;       grade = "E"

&nbsp;   else:

&nbsp;       grade = "F"



&nbsp;   match grade:

&nbsp;       case "A":

&nbsp;           print("Excellent performance")

&nbsp;       case "B":

&nbsp;           print("Very good")

&nbsp;       case "C":

&nbsp;           print("Good")

&nbsp;       case "D":

&nbsp;           print("Fair")

&nbsp;       case "E":

&nbsp;           print("Poor")

&nbsp;       case "F":

&nbsp;           print("Fail")



&nbsp;   return grade



def get\_valid\_age\_cgpa():

&nbsp;   try:

&nbsp;       age\_input = int(input("Enter age: "))

&nbsp;       cgpa\_input = float(input("Enter CGPA: "))



&nbsp;       if age\_input < 16 or age\_input > 40:

&nbsp;           print("Invalid age range")

&nbsp;           return None, None



&nbsp;       if cgpa\_input < 0.0 or cgpa\_input > 5.0:

&nbsp;           print("Invalid CGPA range")

&nbsp;           return None, None



&nbsp;       return age\_input, cgpa\_input



&nbsp;   except ValueError:

&nbsp;       print("Invalid input type")

&nbsp;       return None, None



scores = \[55, 67, 89, 45, 72, 90, 61, 78, 84, 69]



top\_3 = scores\[:3]

last\_5 = scores\[-5:]

every\_other = scores\[::2]



set\_pass = {"Rasheed Fatia", "Yusuf Adeoye", "Nimah Nina"}

set\_merit = {"Rasheed Fatia", "Timi Abidoye"}



passed\_and\_merit = set\_pass \& set\_merit

all\_students = set\_pass | set\_merit

passed\_not\_merit = set\_pass - set\_merit


def check\_eligibility(student):

&nbsp;   if student\["cgpa"] >= 2.5 and student\["outstanding"] == 0 and student\["is\_active"]:

&nbsp;       return True, f'{student\["name"]} is eligible for graduation'

&nbsp;   else:

&nbsp;       return False, f'{student\["name"]} is not eligible for graduation'


def menu():

&nbsp;   while True:

&nbsp;       print("\\n1. View all students")

&nbsp;       print("2. Add new student")

&nbsp;       print("3. Check eligibility for graduation")

&nbsp;       print("4. Find top performer")

&nbsp;       print("5. Exit")



&nbsp;       choice = input("Enter choice: ")



&nbsp;       match choice:

&nbsp;           case "1":

&nbsp;               for s in students:

&nbsp;                   print(s\["name"])



&nbsp;           case "2":

&nbsp;               name = input("Enter name: ")

&nbsp;               matric = input("Enter matric number: ")

&nbsp;               age, cgpa = get\_valid\_age\_cgpa()

&nbsp;               if age is None:

&nbsp;                   continue

&nbsp;               active = input("Is active yes or no: ").lower() == "yes"

&nbsp;               courses = input("Enter courses comma separated: ").split(",")



&nbsp;               new\_student = {

&nbsp;                   "name": name,

&nbsp;                   "matric": matric,

&nbsp;                   "age": age,

&nbsp;                   "cgpa": cgpa,

&nbsp;                   "is\_active": active,

&nbsp;                   "courses": courses,

&nbsp;                   "outstanding": 0

&nbsp;               }



&nbsp;               students.append(new\_student)

&nbsp;               print("Student added successfully")



&nbsp;           case "3":

&nbsp;               name = input("Enter student name: ")

&nbsp;               for s in students:

&nbsp;                   if s\["name"].lower() == name.lower():

&nbsp;                       status, message = check\_eligibility(s)

&nbsp;                       print(message)



&nbsp;           case "4":

&nbsp;               top = max(students, key=lambda x: x\["cgpa"])

&nbsp;               print(top\["name"], top\["cgpa"])



&nbsp;           case "5":

&nbsp;               print("Goodbye")

&nbsp;               break


menu()





