# Author: Ng Jun Ming

def questions():
    print("Enter 1 to Add a new student")
    print("Enter 2 to Update an existing student info")
    print("Enter 3 to Remove an existing student info")
    print("Enter 4 to Display all student information in the system")
    print("Enter 5 to search for student(s)")
    print("Enter -1 to Exit the application")


def check_student_score(score1):
    length_score = str(score1)
    count_score = 0
    count_letters = 0
    for _ in length_score:
        check_score = length_score[count_score].isdigit()
        if not check_score:
            count_letters += 1
        else:
            count_score += 1
    if count_letters != 0 or count_score == 0:
        return False
    else:
        return True


def admin_check(admission_number1):
    check = 0
    No_number = 0
    No_letters = 0
    No_space = 0

    for _ in admission_number1:
        checker = admission_number1[check].isdigit()
        check_space = admission_number1[check]
        if check_space == " ":
            No_space += 1
            check += 1
        elif not checker:
            No_letters += 1
            check += 1

        elif checker:
            No_number += 1
            check += 1
    if No_space > 0:
        print("There should be no space in the admission number")
        return False
    if No_number != 6:
        print("There should be 6 numbers in the admission number")
        return False
    if No_letters != 1:
        print("There should only be 1 letter in the admission number ")
        return False
    else:
        return True


def student_name_func(student_name):
    count_student_name = 0
    count_numbers = 0
    for _ in student_name:
        check_student_name = student_name[count_student_name].isdigit()
        if not check_student_name:
            count_student_name += 1
        else:
            count_student_name += 1
            count_numbers += 1
    if count_numbers != 0 or count_student_name == 0:
        return False
    else:
        return True


def checking_module(module_name):
    if module_name == "":
        print("Please enter a valid module name")
        return False
    else:
        return True


def search_student():
    print("== Search Student ==")
    print("Search by:")
    print("Enter 1 to search by Admission Number")
    print("Enter 2 to search by Module Name")
    print("Enter 3 to search by Score Range")
    print("Enter 0 to search by Main Menu")
