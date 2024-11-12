# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Reilly Thomer,11/9/2024, Script Edited
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
csv_data: str = ''  # Holds combined string data separated by a comma.
json_data: str = '' #Holds the json data
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.
student_data: dict = []  # dictionary of student data
students: list = []  # a list of student data

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
import json
try:
    file = open(FILE_NAME, "r")
    json_data = json.load(file)
    for item in json_data:
        # Transform the data from the file
        student_data = {"FirstName":item["FirstName"],"LastName":item["LastName"],"CourseName":item["CourseName"]}
        #student_data = [student_data[0], student_data[1], student_data[2].strip()]
        # Load it into our collection (list of lists)
        students.append(student_data)
    file.close()
except FileNotFoundError as e:
    print("-" * 50)
    print("Error:\n JSON file must exist before running this script!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
    if file.closed == False: #Makes sure the file is open before trying to close it.
        file.close()
    print("\n-- Program Ended --")
    print("-" * 50)
    exit()
except KeyError as e:
    print("-" * 50)
    print("Error:\n JSON file contains improper data. Check the data and fix any incorrect keys before running this script!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
    if file.closed == False: #Makes sure the file is open before trying to close it.
        file.close()
    print("\n-- Program Ended --")
    print("-" * 50)
    exit()
except Exception as e:
    print("-" * 50)
    print("Error:\n There was an error reading the JSON file.")
    print(e, e.__doc__, type(e), sep='\n')
    if file.closed == False: #Makes sure the file is open before trying to close it.
        file.close()
    print("\n-- Program Ended --")
    print("-" * 50)
    exit()

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            print("-" * 50)
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            csv_data = f'{student_first_name},{student_last_name},{course_name}'
            student_data = {"FirstName":student_first_name,"LastName":student_last_name,"CourseName":course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
            print("-" * 50)
            continue
        except ValueError as e:
            print("-" * 50)
            print(f"Error:\n {e}\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
            print("-" * 50)
        except Exception as e:
            print("-" * 50)
            print(f"Error:\n There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
            print("-" * 50)
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(student)
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students,file)
            file.close()
            print("-" * 50)
            print("The following data was saved to file!")
            for student in students:
                print(f"{student["FirstName"]},{student["LastName"]},{student["CourseName"]}")
            print("-" * 50)
            continue
        except Exception as e:
            print("-" * 50)
            print(f"Error:\n There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
            print("-" * 50)
            if file.closed == False:  # Makes sure the file is open before trying to close it.
                file.close()

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
