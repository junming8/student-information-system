# Author: Ng Jun Ming


from functions import *

number_of_students = 0

students = {}
print("***** Welcome to SIT Mini Student Information System *****")
print(f'Number of student in the system: {number_of_students}')
questions()
Choice = input("Enter Your Choice: ")

while Choice != -1:
    if Choice == "1":
        admission_number1 = input("Please enter the admission number: ")
        admission_number = admission_number1.upper()
        student_name = input("Please enter the student name: ")
        module_name = input("Please enter the module name: ")
        score1 = input("Please enter the score: ")
        if admission_number in students:
            print("The student already exists!")
        else:
            admin_check_test = admin_check(admission_number)
            student_name_test = student_name_func(student_name)
            count_score = check_student_score(score1)
            module_name_check = checking_module(module_name)

            if not admin_check_test:
                print("Enter a valid admission number")
            if not student_name_test:
                print("Enter a valid student name")
            if not count_score:
                print("Enter a valid score")
            elif count_score and admin_check_test and student_name_test:
                students[admission_number] = [student_name, module_name, score1]
                print("Student added")
                number_of_students += 1

    elif Choice == "2":
        if len(students) == 0:
            print("No students in the system")
        else:
            print("== Update student==")
            admission_number1 = input("Please enter the admission number of the student you would like to update: ")
            admission_number = admission_number1.upper()
            if admission_number not in students:
                print("No such student found")
            else:
                print(" ")
                students.get(admission_number)
                print("Admission Number: ", admission_number)
                print("Student Name: ", students[admission_number][0])
                print("Module Name: ", students[admission_number][1])
                print("score: ", students[admission_number][2])
                print("Student Exist!")
                to_update = input(
                    "Enter 1 to Update Name \nEnter 2 to Update Module Name \nEnter 3 to Update Score \nEnter 0 to "
                    "return "
                    "to Main Menu \nWhat would you like to update?: ")
                if to_update == '0':
                    print(" ")
                elif to_update == "1":
                    new_name = input("Enter the new student name: ")
                    student_name_test2 = student_name_func(new_name)
                    if not student_name_test2:
                        print("Enter a valid name")
                    else:
                        students[admission_number][0] = new_name
                        print("Name Updated")
                elif to_update == "2":
                    new_module_name = input("Enter the new module name: ")
                    students[admission_number][1] = new_module_name
                    print("Module Name Updated")
                elif to_update == "3":
                    new_score = float(input("Enter the new score: "))
                    check_student_score_test = check_student_score(new_score)
                    legit_score2 = isinstance(new_score, str)
                    if new_score > 100:
                        print("enter a valid score that is under 100\n")
                    if legit_score2:
                        print("enter a valid number as the score")
                    else:
                        students[admission_number][2] = new_score
                        print("Score Updated")

    elif Choice == "3":
        if len(students) == 0:
            print("No students in the system")
        else:
            print("== Remove student ==")
            admission_number = str(input("Please enter the admission number you want to remove: "))
            if admission_number not in students:
                print("No such student found")
            else:
                print(" ")
                students.get(admission_number)
                print("Admission Number: ", admission_number)
                print("Student Name: ", students[admission_number][0])
                print("Module Name: ", students[admission_number][1])
                print("score: ", students[admission_number][2])
                confirm = input("Is this the student you want to remove? (Yes/No) ")
                if confirm == "Yes":
                    del (students[admission_number])
                    print("Student info removed!")
                    number_of_students -= 1
                else:
                    print("Student info was not removed")

    elif Choice == "4":
        if len(students) == 0:
            print("No students in the system")
        else:
            for admission_number in students:
                print(" ")
                students.get(admission_number)
                print("Admission Number:", admission_number)
                print("Student Name:", students[admission_number][0])
                print("Module Name:", students[admission_number][1])
                print("score:", students[admission_number][2])

    elif Choice == "5":
        if len(students) == 0:
            print("No students in the system")
        else:
            search_student()
            your_choice = input("Your choice: ")
            if your_choice == '1':
                admission_number = input("Please enter the admission number you wish to search by: ")
                if admission_number not in students:
                    print("No student with this admission number found!")
                else:
                    print(" ")
                    print("Admission Number:", admission_number)
                    print("Student Name:", students[admission_number][0])
                    print("Module Name:", students[admission_number][1])
                    print("score:", students[admission_number][2])
                    print(" ")
            if your_choice == '2':
                module_name_search = input("Please enter the module name you wish to search by: ")
                if module_name_search not in students:
                    print("No student with this module name found!")
                else:
                    for admission_number in students:
                        if module_name_search == students[admission_number][1]:
                            print(" ")
                            print("Admission Number:", admission_number)
                            print("Student Name:", students[admission_number][0])
                            print("Module Name:", students[admission_number][1])
                            print("score:", students[admission_number][2])
                            print(" ")
                        else:
                            print("")
            if your_choice == '3':
                print("Please enter the range of score you wish to search by: ")
                min_value = float(input("Minimum score: "))
                max_value = float(input("Maximum score: "))
                count_tracker = 0
                for i in students:
                    if float(students[admission_number][2]) < min_value or \
                            float(students[admission_number][2]) > max_value:
                        count_tracker += 1

                if count_tracker >= 1:
                    print("No students in that range")

                else:
                    for admission_number in students:
                        if float(students[admission_number][2]) >= min_value and float(
                                students[admission_number][2]) <= max_value:
                            print(" ")
                            print("Admission Number:", admission_number)
                            print("Student Name:", students[admission_number][0])
                            print("Module Name:", students[admission_number][1])
                            print("score:", students[admission_number][2])
                            print(" ")
                        else:
                            print("")

    elif Choice == "-1":
        print("application closed")
        break

    else:
        print("Enter a valid option")

    print("***** Welcome to SIT Mini Student Information System *****")
    print(f'Number of student in the system: {number_of_students}')
    questions()
    Choice = input("Enter Your Choice: ")
