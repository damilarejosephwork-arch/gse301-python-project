"""

Student Academic Performance Analysis System

GSE301 Data Science: Python Fundamentals

"""



\# ============================================

\# PART 1: DATA COLLECTION AND STORAGE

\# ============================================



\# Task 1.1: Variable Declaration and Data Types

\# Creating sample student data

student\_name = "Rasheed Fatia"

matric\_number = "23/60AC389"

age = 21

cgpa = 4.81

is\_active = True

courses\_registered = \["ELE567", "Data Science", "Statistics"]

grades = {"Python": "A", "Statistics": "A", "Data Science": "A"}



print("=== Task 1.1: Variable Declaration ===")

print(f"Student: {student\_name}")

print(f"Matric: {matric\_number}")

print(f"Age: {age}")

print(f"CGPA: {cgpa}")

print(f"Active: {is\_active}")

print(f"Courses: {courses\_registered}")

print(f"Grades: {grades}")

print()



\# Task 1.2: Data Structures in Action

\# List of student names

student\_names = \["Rasheed Fatia", "Yusuf Adeoye", "Moses Oyedele", "Timi Abidoye", "Nimah Nina"]



\# Dictionary for each student's full profile

student\_profiles = {

&nbsp;   "Rasheed Fatia": {

&nbsp;       "matric": "23/60AC389",

&nbsp;       "age": 21,

&nbsp;       "cgpa": 4.81,

&nbsp;       "is\_active": True,

&nbsp;       "courses": \["ELE567", "Data Science", "Statistics"],

&nbsp;       "grades": {"Python": "A", "Statistics": "A", "Data Science": "A"},

&nbsp;       "outstanding\_courses": 0

&nbsp;   },

&nbsp;   "Yusuf Adeoye": {

&nbsp;       "matric": "23/70JC093",

&nbsp;       "age": 22,

&nbsp;       "cgpa": 3.45,

&nbsp;       "is\_active": True,

&nbsp;       "courses": \["Python", "Algorithms"],

&nbsp;       "grades": {"Python": "B", "Statistics": "C"},

&nbsp;       "outstanding\_courses": 0

&nbsp;   },

&nbsp;   "Moses Oyedele": {

&nbsp;       "matric": "23/80KD123",

&nbsp;       "age": 20,

&nbsp;       "cgpa": 2.30,

&nbsp;       "is\_active": True,

&nbsp;       "courses": \["Python", "Networking"],

&nbsp;       "grades": {"Python": "D", "Statistics": "E"},

&nbsp;       "outstanding\_courses": 1

&nbsp;   },

&nbsp;   "Timi Abidoye": {

&nbsp;       "matric": "23/90LE456",

&nbsp;       "age": 23,

&nbsp;       "cgpa": 3.90,

&nbsp;       "is\_active": False,

&nbsp;       "courses": \["Algorithms", "Networking"],

&nbsp;       "grades": {"Python": "A", "Algorithms": "B"},

&nbsp;       "outstanding\_courses": 0

&nbsp;   },

&nbsp;   "Nimah Nina": {

&nbsp;       "matric": "23/10MF789",

&nbsp;       "age": 19,

&nbsp;       "cgpa": 4.50,

&nbsp;       "is\_active": True,

&nbsp;       "courses": \["Data Science", "Statistics"],

&nbsp;       "grades": {"Data Science": "A", "Statistics": "A"},

&nbsp;       "outstanding\_courses": 2

&nbsp;   }

}



\# Set to store unique courses offered

unique\_courses = set()

for student in student\_profiles.values():

&nbsp;   for course in student\["courses"]:

&nbsp;       unique\_courses.add(course)



\# Tuple for fixed department information

department\_info = ("Religion department", "Faculty of Technology", 2025)



print("=== Task 1.2: Data Structures ===")

print(f"Student Names: {student\_names}")

print(f"Unique Courses: {unique\_courses}")

print(f"Department Info: {department\_info}")

print()



\# ============================================

\# PART 2: DATA PROCESSING AND LOGIC

\# ============================================



\# Task 2.1: Conditional Statements for Grading

def calculate\_grade(score):

&nbsp;   """Convert score to grade using IF-ELIF-ELSE"""

&nbsp;   if score >= 70:

&nbsp;       return "A"

&nbsp;   elif score >= 60:

&nbsp;       return "B"

&nbsp;   elif score >= 50:

&nbsp;       return "C"

&nbsp;   elif score >= 45:

&nbsp;       return "D"

&nbsp;   elif score >= 40:

&nbsp;       return "E"

&nbsp;   else:

&nbsp;       return "F"



def get\_feedback(grade):

&nbsp;   """Provide feedback using MATCH CASE"""

&nbsp;   match grade:

&nbsp;       case "A":

&nbsp;           return "Excellent performance!"

&nbsp;       case "B":

&nbsp;           return "Good work!"

&nbsp;       case "C":

&nbsp;           return "Satisfactory performance."

&nbsp;       case "D":

&nbsp;           return "You passed, but need improvement."

&nbsp;       case "E":

&nbsp;           return "Barely passed. Consider remedial classes."

&nbsp;       case "F":

&nbsp;           return "Failed. Retake required."

&nbsp;       case \_:

&nbsp;           return "Invalid grade"



print("=== Task 2.1: Grading System ===")

test\_scores = \[85, 65, 55, 48, 42, 35]

for score in test\_scores:

&nbsp;   grade = calculate\_grade(score)

&nbsp;   feedback = get\_feedback(grade)

&nbsp;   print(f"Score: {score} -> Grade: {grade} -> Feedback: {feedback}")

print()



\# Task 2.2: Type Conversion and Validation

def get\_valid\_input():

&nbsp;   """Get and validate age and CGPA input"""

&nbsp;   while True:

&nbsp;       try:

&nbsp;           age\_str = input("Enter age (as string): ")

&nbsp;           cgpa\_str = input("Enter CGPA (as string): ")

&nbsp;           

&nbsp;           # Type conversion

&nbsp;           age\_int = int(age\_str)

&nbsp;           cgpa\_float = float(cgpa\_str)

&nbsp;           

&nbsp;           # Validation

&nbsp;           if 16 <= age\_int <= 40 and 0.0 <= cgpa\_float <= 5.0:

&nbsp;               return age\_int, cgpa\_float

&nbsp;           else:

&nbsp;               print("Error: Age must be between 16-40 and CGPA between 0.0-5.0")

&nbsp;       except ValueError:

&nbsp;           print("Error: Invalid input. Please enter numeric values.")

&nbsp;       except Exception as e:

&nbsp;           print(f"Unexpected error: {e}")



print("=== Task 2.2: Input Validation ===")

\# Uncomment to test interactive input:

\# age, cgpa = get\_valid\_input()

\# print(f"Validated - Age: {age}, CGPA: {cgpa}")

print()



\# ============================================

\# PART 3: ANALYSIS AND REPORTING

\# ============================================



\# Task 3.1: List Operations and Slicing

assignment\_scores = \[85, 90, 78, 92, 88, 76, 95, 89, 81, 87]



top\_3\_scores = assignment\_scores\[:3]  # First 3 scores

last\_5\_scores = assignment\_scores\[-5:]  # Last 5 scores using negative indexing

every\_other\_score = assignment\_scores\[::2]  # Every other score



print("=== Task 3.1: List Slicing ===")

print(f"Original scores: {assignment\_scores}")

print(f"Top 3 scores: {top\_3\_scores}")

print(f"Last 5 scores: {last\_5\_scores}")

print(f"Every other score: {every\_other\_score}")

print()



\# Task 3.2: Set Operations

set\_pass = {"Rasheed Fatia", "Yusuf Adeoye", "Timi Abidoye", "Nimah Nina"}

set\_merit = {"Rasheed Fatia", "Nimah Nina", "Moses Oyedele"}



passed\_and\_merit = set\_pass.intersection(set\_merit)

all\_students = set\_pass.union(set\_merit)

passed\_no\_merit = set\_pass.difference(set\_merit)



print("=== Task 3.2: Set Operations ===")

print(f"Students who passed Python: {set\_pass}")

print(f"Students with CGPA > 4.0: {set\_merit}")

print(f"Passed AND have merit: {passed\_and\_merit}")

print(f"All distinct students: {all\_students}")

print(f"Passed but no merit: {passed\_no\_merit}")

print()



\# ============================================

\# PART 4: INTERACTIVE MENU SYSTEM

\# ============================================



\# Task 4.2: Eligibility Checker

def check\_graduation\_eligibility(student\_name, student\_data):

&nbsp;   """Check if student is eligible for graduation using logical operators"""

&nbsp;   cgpa\_eligible = student\_data\["cgpa"] >= 2.5

&nbsp;   no\_outstanding = student\_data\["outstanding\_courses"] == 0

&nbsp;   is\_active = student\_data\["is\_active"]

&nbsp;   

&nbsp;   is\_eligible = cgpa\_eligible and no\_outstanding and is\_active

&nbsp;   

&nbsp;   message = f"\\nMatric Number: {student\_data\['matric']}\\n"

&nbsp;   message += f"CGPA: {student\_data\['cgpa']}\\n"

&nbsp;   message += f"Outstanding Courses: {student\_data\['outstanding\_courses']}\\n"

&nbsp;   message += f"Active Status: {student\_data\['is\_active']}\\n"

&nbsp;   message += f"\\nEligibility Result:\\n"

&nbsp;   

&nbsp;   if is\_eligible:

&nbsp;       message += f"{student\_name} is eligible for graduation."

&nbsp;   else:

&nbsp;       message += f"{student\_name} is NOT eligible for graduation."

&nbsp;       reasons = \[]

&nbsp;       if not cgpa\_eligible:

&nbsp;           reasons.append("CGPA below 2.5")

&nbsp;       if not no\_outstanding:

&nbsp;           reasons.append("Has outstanding courses")

&nbsp;       if not is\_active:

&nbsp;           reasons.append("Student is not active")

&nbsp;       message += f" Reasons: {', '.join(reasons)}"

&nbsp;   

&nbsp;   return is\_eligible, message



def find\_top\_performer(profiles):

&nbsp;   """Find student with highest CGPA"""

&nbsp;   top\_student = None

&nbsp;   top\_cgpa = 0.0

&nbsp;   

&nbsp;   for name, data in profiles.items():

&nbsp;       if data\["cgpa"] > top\_cgpa:

&nbsp;           top\_cgpa = data\["cgpa"]

&nbsp;           top\_student = (name, data)

&nbsp;   

&nbsp;   return top\_student



def add\_new\_student():

&nbsp;   """Add a new student to the system"""

&nbsp;   print("\\n--- Add New Student ---")

&nbsp;   name = input("Enter name: ")

&nbsp;   matric = input("Enter matric number: ")

&nbsp;   

&nbsp;   while True:

&nbsp;       try:

&nbsp;           age = int(input("Enter age: "))

&nbsp;           cgpa = float(input("Enter CGPA: "))

&nbsp;           if 16 <= age <= 40 and 0.0 <= cgpa <= 5.0:

&nbsp;               break

&nbsp;           else:

&nbsp;               print("Invalid age or CGPA. Try again.")

&nbsp;       except ValueError:

&nbsp;           print("Please enter numeric values.")

&nbsp;   

&nbsp;   active\_input = input("Is the student active (yes/no): ").lower()

&nbsp;   is\_active = active\_input in \["yes", "y"]

&nbsp;   

&nbsp;   courses\_input = input("Enter courses (comma separated): ")

&nbsp;   courses = \[course.strip() for course in courses\_input.split(",")]

&nbsp;   

&nbsp;   # Add to system

&nbsp;   student\_profiles\[name] = {

&nbsp;       "matric": matric,

&nbsp;       "age": age,

&nbsp;       "cgpa": cgpa,

&nbsp;       "is\_active": is\_active,

&nbsp;       "courses": courses,

&nbsp;       "grades": {},  # Empty grades initially

&nbsp;       "outstanding\_courses": 0  # Assuming no outstanding courses for new students

&nbsp;   }

&nbsp;   

&nbsp;   print(f"Student record for {name} added successfully!")

&nbsp;   return name



\# Task 4.1: Console Menu System

def display\_menu():

&nbsp;   """Display the main menu"""

&nbsp;   print("\\n" + "=" \* 50)

&nbsp;   print("Student Academic Performance System")

&nbsp;   print("=" \* 50)

&nbsp;   print("Menu Options")

&nbsp;   print("1. View all students")

&nbsp;   print("2. Add new student")

&nbsp;   print("3. Check eligibility for graduation")

&nbsp;   print("4. Find top performer")

&nbsp;   print("5. Exit")

&nbsp;   print("-" \* 50)



def run\_menu\_system():

&nbsp;   """Main menu loop"""

&nbsp;   print("Loading student records...")

&nbsp;   print(f"{len(student\_profiles)} student profiles loaded successfully.")

&nbsp;   

&nbsp;   while True:

&nbsp;       display\_menu()

&nbsp;       

&nbsp;       try:

&nbsp;           choice = input("Enter your choice: ").strip()

&nbsp;           

&nbsp;           match choice:

&nbsp;               case "1":

&nbsp;                   # View all students

&nbsp;                   print("\\n--- List of Students ---")

&nbsp;                   for i, name in enumerate(student\_names, 1):

&nbsp;                       print(f"{i}. {name}")

&nbsp;               

&nbsp;               case "2":

&nbsp;                   # Add new student

&nbsp;                   new\_student = add\_new\_student()

&nbsp;                   if new\_student not in student\_names:

&nbsp;                       student\_names.append(new\_student)

&nbsp;               

&nbsp;               case "3":

&nbsp;                   # Check eligibility

&nbsp;                   student\_name = input("Enter student name: ")

&nbsp;                   if student\_name in student\_profiles:

&nbsp;                       eligible, message = check\_graduation\_eligibility(

&nbsp;                           student\_name, student\_profiles\[student\_name]

&nbsp;                       )

&nbsp;                       print(message)

&nbsp;                   else:

&nbsp;                       print(f"Student '{student\_name}' not found.")

&nbsp;               

&nbsp;               case "4":

&nbsp;                   # Find top performer

&nbsp;                   top\_student = find\_top\_performer(student\_profiles)

&nbsp;                   if top\_student:

&nbsp;                       name, data = top\_student

&nbsp;                       print("\\n--- Top Performer ---")

&nbsp;                       print(f"Name: {name}")

&nbsp;                       print(f"Matric: {data\['matric']}")

&nbsp;                       print(f"CGPA: {data\['cgpa']}")

&nbsp;                       print(f"Courses: {data\['courses']}")

&nbsp;                   else:

&nbsp;                       print("No students in the system.")

&nbsp;               

&nbsp;               case "5":

&nbsp;                   # Exit

&nbsp;                   print("\\nExiting the system...")

&nbsp;                   print("Goodbye!")

&nbsp;                   break

&nbsp;               

&nbsp;               case \_:

&nbsp;                   print("Invalid choice. Please enter 1-5.")

&nbsp;       

&nbsp;       except KeyboardInterrupt:

&nbsp;           print("\\n\\nProgram interrupted. Exiting...")

&nbsp;           break

&nbsp;       except Exception as e:

&nbsp;           print(f"An error occurred: {e}")



\# ============================================

\# PART 5: ADVANCED CHALLENGES (OPTIONAL)

\# ============================================



\# Task 5.1: Nested Data Processing

def process\_nested\_data():

&nbsp;   """Process nested student data"""

&nbsp;   # Sample nested scores (converting grades to numeric scores)

&nbsp;   student\_scores = {

&nbsp;       "Rasheed Fatia": {"Python": 90, "Statistics": 85, "Data Science": 92},

&nbsp;       "Yusuf Adeoye": {"Python": 75, "Statistics": 68},

&nbsp;       "Moses Oyedele": {"Python": 58, "Statistics": 42}

&nbsp;   }

&nbsp;   

&nbsp;   print("\\n=== Task 5.1: Nested Data Processing ===")

&nbsp;   

&nbsp;   # Calculate average for each student

&nbsp;   for student, scores in student\_scores.items():

&nbsp;       avg\_score = sum(scores.values()) / len(scores)

&nbsp;       print(f"{student}: Average score = {avg\_score:.2f}")

&nbsp;   

&nbsp;   # Identify students scoring above 70 in all courses

&nbsp;   high\_achievers = \[]

&nbsp;   for student, scores in student\_scores.items():

&nbsp;       if all(score > 70 for score in scores.values()):

&nbsp;           high\_achievers.append(student)

&nbsp;   

&nbsp;   print(f"Students scoring above 70 in all courses: {high\_achievers}")



\# Task 5.2: Pattern Matching with MATCH CASE

def identify\_data\_type(data):

&nbsp;   """Identify and summarize data type using MATCH CASE"""

&nbsp;   match data:

&nbsp;       case int():

&nbsp;           return f"Integer: {data}. This is a whole number."

&nbsp;       case float():

&nbsp;           return f"Float: {data}. This is a decimal number."

&nbsp;       case list():

&nbsp;           return f"List: {data}. Length: {len(data)}. Contains multiple items."

&nbsp;       case dict():

&nbsp;           return f"Dictionary: {data}. Keys: {list(data.keys())}."

&nbsp;       case str():

&nbsp;           return f"String: '{data}'. Length: {len(data)} characters."

&nbsp;       case \_:

&nbsp;           return f"Unknown type: {type(data).\_\_name\_\_}"



\# ============================================

\# MAIN EXECUTION

\# ============================================



if \_\_name\_\_ == "\_\_main\_\_":

&nbsp;   # Run the advanced challenges (optional)

&nbsp;   print("=" \* 50)

&nbsp;   print("STUDENT ACADEMIC PERFORMANCE ANALYSIS SYSTEM")

&nbsp;   print("=" \* 50)

&nbsp;   

&nbsp;   # Run optional tasks

&nbsp;   process\_nested\_data()

&nbsp;   

&nbsp;   print("\\n=== Task 5.2: Data Type Identification ===")

&nbsp;   test\_data = \[42, 3.14, \["apple", "banana"], {"name": "John"}, "Hello World"]

&nbsp;   for item in test\_data:

&nbsp;       result = identify\_data\_type(item)

&nbsp;       print(result)

&nbsp;   

&nbsp;   print("\\n" + "=" \* 50)

&nbsp;   print("Starting Interactive Menu System...")

&nbsp;   print("=" \* 50)

&nbsp;   

&nbsp;   # Start the main menu system

&nbsp;   run\_menu\_system()

