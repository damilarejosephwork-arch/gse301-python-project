"""
Student Academic Performance Analysis System
GSE301 Data Science: Python Fundamentals
"""

# ============================================
# PART 1: DATA COLLECTION AND STORAGE
# ============================================

# Task 1.1: Variable Declaration and Data Types
# Creating sample student data
student_name = "Rasheed Fatia"
matric_number = "23/60AC389"
age = 21
cgpa = 4.81
is_active = True
courses_registered = ["ELE567", "Data Science", "Statistics"]
grades = {"Python": "A", "Statistics": "A", "Data Science": "A"}

print("=== Task 1.1: Variable Declaration ===")
print(f"Student: {student_name}")
print(f"Matric: {matric_number}")
print(f"Age: {age}")
print(f"CGPA: {cgpa}")
print(f"Active: {is_active}")
print(f"Courses: {courses_registered}")
print(f"Grades: {grades}")
print()

# Task 1.2: Data Structures in Action
# List of student names
student_names = ["Rasheed Fatia", "Yusuf Adeoye", "Moses Oyedele", "Timi Abidoye", "Nimah Nina"]

# Dictionary for each student's full profile
student_profiles = {
    "Rasheed Fatia": {
        "matric": "23/60AC389",
        "age": 21,
        "cgpa": 4.81,
        "is_active": True,
        "courses": ["ELE567", "Data Science", "Statistics"],
        "grades": {"Python": "A", "Statistics": "A", "Data Science": "A"},
        "outstanding_courses": 0
    },
    "Yusuf Adeoye": {
        "matric": "23/70JC093",
        "age": 22,
        "cgpa": 3.45,
        "is_active": True,
        "courses": ["Python", "Algorithms"],
        "grades": {"Python": "B", "Statistics": "C"},
        "outstanding_courses": 0
    },
    "Moses Oyedele": {
        "matric": "23/80KD123",
        "age": 20,
        "cgpa": 2.30,
        "is_active": True,
        "courses": ["Python", "Networking"],
        "grades": {"Python": "D", "Statistics": "E"},
        "outstanding_courses": 1
    },
    "Timi Abidoye": {
        "matric": "23/90LE456",
        "age": 23,
        "cgpa": 3.90,
        "is_active": False,
        "courses": ["Algorithms", "Networking"],
        "grades": {"Python": "A", "Algorithms": "B"},
        "outstanding_courses": 0
    },
    "Nimah Nina": {
        "matric": "23/10MF789",
        "age": 19,
        "cgpa": 4.50,
        "is_active": True,
        "courses": ["Data Science", "Statistics"],
        "grades": {"Data Science": "A", "Statistics": "A"},
        "outstanding_courses": 2
    }
}

# Set to store unique courses offered
unique_courses = set()
for student in student_profiles.values():
    for course in student["courses"]:
        unique_courses.add(course)

# Tuple for fixed department information
department_info = ("Religion department", "Faculty of Technology", 2025)

print("=== Task 1.2: Data Structures ===")
print(f"Student Names: {student_names}")
print(f"Unique Courses: {unique_courses}")
print(f"Department Info: {department_info}")
print()

# ============================================
# PART 2: DATA PROCESSING AND LOGIC
# ============================================

# Task 2.1: Conditional Statements for Grading
def calculate_grade(score):
    """Convert score to grade using IF-ELIF-ELSE"""
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 45:
        return "D"
    elif score >= 40:
        return "E"
    else:
        return "F"

def get_feedback(grade):
    """Provide feedback using MATCH CASE"""
    match grade:
        case "A":
            return "Excellent performance!"
        case "B":
            return "Good work!"
        case "C":
            return "Satisfactory performance."
        case "D":
            return "You passed, but need improvement."
        case "E":
            return "Barely passed. Consider remedial classes."
        case "F":
            return "Failed. Retake required."
        case _:
            return "Invalid grade"

print("=== Task 2.1: Grading System ===")
test_scores = [85, 65, 55, 48, 42, 35]
for score in test_scores:
    grade = calculate_grade(score)
    feedback = get_feedback(grade)
    print(f"Score: {score} -> Grade: {grade} -> Feedback: {feedback}")
print()

# Task 2.2: Type Conversion and Validation
def get_valid_input():
    """Get and validate age and CGPA input"""
    while True:
        try:
            age_str = input("Enter age (as string): ")
            cgpa_str = input("Enter CGPA (as string): ")
            
            # Type conversion
            age_int = int(age_str)
            cgpa_float = float(cgpa_str)
            
            # Validation
            if 16 <= age_int <= 40 and 0.0 <= cgpa_float <= 5.0:
                return age_int, cgpa_float
            else:
                print("Error: Age must be between 16-40 and CGPA between 0.0-5.0")
        except ValueError:
            print("Error: Invalid input. Please enter numeric values.")
        except Exception as e:
            print(f"Unexpected error: {e}")

print("=== Task 2.2: Input Validation ===")
# Uncomment to test interactive input:
# age, cgpa = get_valid_input()
# print(f"Validated - Age: {age}, CGPA: {cgpa}")
print()

# ============================================
# PART 3: ANALYSIS AND REPORTING
# ============================================

# Task 3.1: List Operations and Slicing
assignment_scores = [85, 90, 78, 92, 88, 76, 95, 89, 81, 87]

top_3_scores = assignment_scores[:3]  # First 3 scores
last_5_scores = assignment_scores[-5:]  # Last 5 scores using negative indexing
every_other_score = assignment_scores[::2]  # Every other score

print("=== Task 3.1: List Slicing ===")
print(f"Original scores: {assignment_scores}")
print(f"Top 3 scores: {top_3_scores}")
print(f"Last 5 scores: {last_5_scores}")
print(f"Every other score: {every_other_score}")
print()

# Task 3.2: Set Operations
set_pass = {"Rasheed Fatia", "Yusuf Adeoye", "Timi Abidoye", "Nimah Nina"}
set_merit = {"Rasheed Fatia", "Nimah Nina", "Moses Oyedele"}

passed_and_merit = set_pass.intersection(set_merit)
all_students = set_pass.union(set_merit)
passed_no_merit = set_pass.difference(set_merit)

print("=== Task 3.2: Set Operations ===")
print(f"Students who passed Python: {set_pass}")
print(f"Students with CGPA > 4.0: {set_merit}")
print(f"Passed AND have merit: {passed_and_merit}")
print(f"All distinct students: {all_students}")
print(f"Passed but no merit: {passed_no_merit}")
print()

# ============================================
# PART 4: INTERACTIVE MENU SYSTEM
# ============================================

# Task 4.2: Eligibility Checker
def check_graduation_eligibility(student_name, student_data):
    """Check if student is eligible for graduation using logical operators"""
    cgpa_eligible = student_data["cgpa"] >= 2.5
    no_outstanding = student_data["outstanding_courses"] == 0
    is_active = student_data["is_active"]
    
    is_eligible = cgpa_eligible and no_outstanding and is_active
    
    message = f"\nMatric Number: {student_data['matric']}\n"
    message += f"CGPA: {student_data['cgpa']}\n"
    message += f"Outstanding Courses: {student_data['outstanding_courses']}\n"
    message += f"Active Status: {student_data['is_active']}\n"
    message += f"\nEligibility Result:\n"
    
    if is_eligible:
        message += f"{student_name} is eligible for graduation."
    else:
        message += f"{student_name} is NOT eligible for graduation."
        reasons = []
        if not cgpa_eligible:
            reasons.append("CGPA below 2.5")
        if not no_outstanding:
            reasons.append("Has outstanding courses")
        if not is_active:
            reasons.append("Student is not active")
        message += f" Reasons: {', '.join(reasons)}"
    
    return is_eligible, message

def find_top_performer(profiles):
    """Find student with highest CGPA"""
    top_student = None
    top_cgpa = 0.0
    
    for name, data in profiles.items():
        if data["cgpa"] > top_cgpa:
            top_cgpa = data["cgpa"]
            top_student = (name, data)
    
    return top_student

def add_new_student():
    """Add a new student to the system"""
    print("\n--- Add New Student ---")
    name = input("Enter name: ")
    matric = input("Enter matric number: ")
    
    while True:
        try:
            age = int(input("Enter age: "))
            cgpa = float(input("Enter CGPA: "))
            if 16 <= age <= 40 and 0.0 <= cgpa <= 5.0:
                break
            else:
                print("Invalid age or CGPA. Try again.")
        except ValueError:
            print("Please enter numeric values.")
    
    active_input = input("Is the student active (yes/no): ").lower()
    is_active = active_input in ["yes", "y"]
    
    courses_input = input("Enter courses (comma separated): ")
    courses = [course.strip() for course in courses_input.split(",")]
    
    # Add to system
    student_profiles[name] = {
        "matric": matric,
        "age": age,
        "cgpa": cgpa,
        "is_active": is_active,
        "courses": courses,
        "grades": {},  # Empty grades initially
        "outstanding_courses": 0  # Assuming no outstanding courses for new students
    }
    
    print(f"Student record for {name} added successfully!")
    return name

# Task 4.1: Console Menu System
def display_menu():
    """Display the main menu"""
    print("\n" + "=" * 50)
    print("Student Academic Performance System")
    print("=" * 50)
    print("Menu Options")
    print("1. View all students")
    print("2. Add new student")
    print("3. Check eligibility for graduation")
    print("4. Find top performer")
    print("5. Exit")
    print("-" * 50)

def run_menu_system():
    """Main menu loop"""
    print("Loading student records...")
    print(f"{len(student_profiles)} student profiles loaded successfully.")
    
    while True:
        display_menu()
        
        try:
            choice = input("Enter your choice: ").strip()
            
            match choice:
                case "1":
                    # View all students
                    print("\n--- List of Students ---")
                    for i, name in enumerate(student_names, 1):
                        print(f"{i}. {name}")
                
                case "2":
                    # Add new student
                    new_student = add_new_student()
                    if new_student not in student_names:
                        student_names.append(new_student)
                
                case "3":
                    # Check eligibility
                    student_name = input("Enter student name: ")
                    if student_name in student_profiles:
                        eligible, message = check_graduation_eligibility(
                            student_name, student_profiles[student_name]
                        )
                        print(message)
                    else:
                        print(f"Student '{student_name}' not found.")
                
                case "4":
                    # Find top performer
                    top_student = find_top_performer(student_profiles)
                    if top_student:
                        name, data = top_student
                        print("\n--- Top Performer ---")
                        print(f"Name: {name}")
                        print(f"Matric: {data['matric']}")
                        print(f"CGPA: {data['cgpa']}")
                        print(f"Courses: {data['courses']}")
                    else:
                        print("No students in the system.")
                
                case "5":
                    # Exit
                    print("\nExiting the system...")
                    print("Goodbye!")
                    break
                
                case _:
                    print("Invalid choice. Please enter 1-5.")
        
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Exiting...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

# ============================================
# PART 5: ADVANCED CHALLENGES (OPTIONAL)
# ============================================

# Task 5.1: Nested Data Processing
def process_nested_data():
    """Process nested student data"""
    # Sample nested scores (converting grades to numeric scores)
    student_scores = {
        "Rasheed Fatia": {"Python": 90, "Statistics": 85, "Data Science": 92},
        "Yusuf Adeoye": {"Python": 75, "Statistics": 68},
        "Moses Oyedele": {"Python": 58, "Statistics": 42}
    }
    
    print("\n=== Task 5.1: Nested Data Processing ===")
    
    # Calculate average for each student
    for student, scores in student_scores.items():
        avg_score = sum(scores.values()) / len(scores)
        print(f"{student}: Average score = {avg_score:.2f}")
    
    # Identify students scoring above 70 in all courses
    high_achievers = []
    for student, scores in student_scores.items():
        if all(score > 70 for score in scores.values()):
            high_achievers.append(student)
    
    print(f"Students scoring above 70 in all courses: {high_achievers}")

# Task 5.2: Pattern Matching with MATCH CASE
def identify_data_type(data):
    """Identify and summarize data type using MATCH CASE"""
    match data:
        case int():
            return f"Integer: {data}. This is a whole number."
        case float():
            return f"Float: {data}. This is a decimal number."
        case list():
            return f"List: {data}. Length: {len(data)}. Contains multiple items."
        case dict():
            return f"Dictionary: {data}. Keys: {list(data.keys())}."
        case str():
            return f"String: '{data}'. Length: {len(data)} characters."
        case _:
            return f"Unknown type: {type(data).__name__}"

# ============================================
# MAIN EXECUTION
# ============================================

if __name__ == "__main__":
    # Run the advanced challenges (optional)
    print("=" * 50)
    print("STUDENT ACADEMIC PERFORMANCE ANALYSIS SYSTEM")
    print("=" * 50)
    
    # Run optional tasks
    process_nested_data()
    
    print("\n=== Task 5.2: Data Type Identification ===")
    test_data = [42, 3.14, ["apple", "banana"], {"name": "John"}, "Hello World"]
    for item in test_data:
        result = identify_data_type(item)
        print(result)
    
    print("\n" + "=" * 50)
    print("Starting Interactive Menu System...")
    print("=" * 50)
    
    # Start the main menu system
    run_menu_system()