students_list = []

def student_details(students_list):

    while True:
            
        name = input("Enter student's name : ")

        while True:

            try:

                roll_no = int(input("Enter roll no. : "))

                if roll_no <= 0:

                    print("Roll no. should be greater than zero.")
                    continue

                elif roll_no >= 100:

                    print("Roll no. should be less than 100.")
                    continue

                break

            except ValueError:

                print("Enter valid roll no.")
                continue


        while True:
            try:

                marks = int(input("Enter marks : "))

                if marks < 0:

                    print("Marks cannot be negative.")
                    continue

                elif marks > 100:

                    print("Marks cannot be greater than 100.")
                    continue

                break

            except ValueError:

                print("Enter valid marks")
                continue

        data = [name, roll_no, marks]

        students_list.append(data)
            
        another_student = input("Do you want to add another student ? (yes or no) : ").lower()
    
        while another_student not in ["yes", "no"]:

            print("Another student addition response must be in yes or no.")
            another_student = input("Do you want to add another student ? (yes or no) : ").lower()
            continue

        if another_student == "no":
            break

def search_student(students_list):

    his_detail = None

    try:

        found = False 
        search_roll = int(input("Enter the student roll no. to display his details : "))

        for detail in students_list:

            if search_roll == detail[1]:
                found = True
                his_detail = f"\nName : {detail[0]} | Roll No. : {detail[1]} | Marks : {detail[2]}\n"
                break

        if not found:
            
            print("\nNo such student found!\n")

    except ValueError:

        print("Enter valid roll no.")

    return his_detail

def calculate_average(students_list):

    try:
        
        total_marks = 0

        for detail in students_list:

            total_marks += detail[2]

        average_marks = round(total_marks / len(students_list), 2)

    except ZeroDivisionError:

        print("\nThere are no student details currently.\n")

        return None, None

    return total_marks, average_marks

def highest_marks(students_list):

    if not students_list:

        return None, None, None

    highest = 0
    highest_scorer_detail = None
    highest_scorer_name = None

    for detail in students_list:

        if detail[2] > highest:

            highest = detail[2]
            highest_scorer_detail = detail
            highest_scorer_name = detail[0]

    return highest, highest_scorer_detail, highest_scorer_name

def lowest_marks(students_list):

    if not students_list:

        return None, None, None

    lowest = 100
    lowest_scorer_detail = None
    lowest_scorer_name = None

    for detail in students_list:

        if detail[2] < lowest:

            lowest = detail[2]
            lowest_scorer_detail = detail
            lowest_scorer_name = detail[0]

    return lowest, lowest_scorer_detail, lowest_scorer_name

def calculate_grades(students_list):

    grade_list = []

    for detail in students_list:

        if detail[2] >= 90:

            grade = "A"

        elif detail[2] >= 75:

            grade = "B"

        elif detail[2] >= 60:

            grade = "C"

        elif detail[2] >= 40:

            grade = "D"

        else:

            grade = "F"

        grade_list.append(grade)

    return grade_list

def display_details(students_list, grade_list, total_marks, average_marks, highest_marks, highest_scorer_name, lowest_marks, lowest_scorer_name):

    report = ""

    for i in range(len(students_list)):

        data = f"\nName : {students_list[i][0]} | Roll No. : {students_list[i][1]} | Marks : {students_list[i][2]} | Grade : {grade_list[i]}\n"
        report += data

    content = f"\nTotal Marks : {total_marks}\nAverage Marks : {average_marks}\nHighest Marks : {highest_marks}\tName : {highest_scorer_name}\nLowest Marks : {lowest_marks}\tName : {lowest_scorer_name}\n"
    
    report += content

    return report, content

def save_details(report):

    with open("Student_Details.txt", "a") as file:

        file.write(report)

        print("File Saved Successfully.\n")

menu = "Type 1 for adding student detail.\nType 2 for displaying details.\nType 3 for searching student details.\nType 4 for getting stats.\nType 5 for saving the details.\nType 6 for exit.\n"

while True:

    print(menu) 

    try:
    
        choice = int(input("Enter your choice in numbers according to your work : "))
        print()

        if choice == 1:

            student_details(students_list)

        elif choice == 2:

            total_marks, average_marks = calculate_average(students_list)
            highest, highest_scorer_detail, highest_scorer_name = highest_marks(students_list)
            lowest, lowest_scorer_detail, lowest_scorer_name = lowest_marks(students_list)
            grade_list = calculate_grades(students_list)
            report, content = display_details(students_list, grade_list, total_marks, average_marks, highest, highest_scorer_name, lowest, lowest_scorer_name)
            print(report)

        elif choice == 3:

            his_detail = search_student(students_list)
            print(his_detail) if his_detail != None else print()

        elif choice == 4:

            total_marks, average_marks = calculate_average(students_list)
            highest, highest_scorer_detail, highest_scorer_name = highest_marks(students_list)
            lowest, lowest_scorer_detail, lowest_scorer_name = lowest_marks(students_list)
            grade_list = calculate_grades(students_list)
            report, content = display_details(students_list, grade_list, total_marks, average_marks, highest, highest_scorer_name, lowest, lowest_scorer_name)
            print(content)

        elif choice == 5:

            total_marks, average_marks = calculate_average(students_list)
            highest, highest_scorer_detail, highest_scorer_name = highest_marks(students_list)
            lowest, lowest_scorer_detail, lowest_scorer_name = lowest_marks(students_list)
            grade_list = calculate_grades(students_list)
            report, content = display_details(students_list, grade_list, total_marks, average_marks, highest, highest_scorer_name, lowest, lowest_scorer_name)
            save_details(report)

        elif choice == 6:

            print("Visit again.")
            break

        else:

            print("\nINVALID CHOICE.\n")

    except ValueError:

        print("\nChoice should be between 1 to 6 only.\n")