#Author: Mikyle Khan
#File Name: student_qualifications.py
#Description: This program takes user input to determine if a student qualifies for the Dean's List or Honor Roll if at all

while True:
    #Get student's last name and check if the user wants to quit
    last_name = input("Enter the student's last name (type 'ZZZ' to stop): ")
    if last_name == 'ZZZ':
        break

    #Get student's first name and GPA
    first_name = input("Enter the student's first name: ")
    
    #Try to convert the GPA to a float, if it fails, ask again
    try:
        gpa = float(input("Enter the student's GPA: "))
    except ValueError:
        print("Oops! That wasn't a valid number. Please enter a numeric GPA.")
        continue

    #Check if the student qualifies for the Dean's List or Honor Roll
    if gpa >= 3.5:
        print(f"Congratulations, {first_name} {last_name}! You've made the Dean's List.")
    elif gpa >= 3.25:
        print(f"Well done, {first_name} {last_name}! You've made the Honor Roll.")
    else:
        print(f"{first_name} {last_name} did not qualify for the Dean's List or Honor Roll this time.")
