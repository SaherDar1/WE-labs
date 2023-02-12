from student import student
from controler import StudentController
status = True
while (status):
    print("*****Welcome To the Management System*****")
    print("1) Registered\n")
    print("2) Login\n")
    print("3) Press -1 to Exist\n")
    userChoice = int(input("Enter Your Choice: "))
    if (userChoice == -1):
        status = False
    elif (userChoice == 1):
        print("1) Student Profile \n")
        print("2) Faculty Profile \n")
        userChoice = int(input("Enter Your Choice: "))

        if (userChoice == 1):
            student = StudentController(
                "localhost", "root", "1122", "fcit")
            student_name = input("Enter the Student Name: ")
            while (student.UsernameValidation(student_name) == False):
                student_name = input("User Already Exist try Another Name: ")
            usre_password = input("Enter The Password: ")
            user_semester = int(input("Enter The Semester: "))
            user_cgpa = float(input("Enter Your CGPA: "))
            user_major = input("Enter Your Major: ")
            student_credential_list = (student.StudentValidationOfCredentials(
                usre_password, user_semester, user_cgpa, user_major))  # except username
            # append student name for coontroller class
            student_credential_list.append(student_name)
            stu = student.RegisterationOfStudent(student_credential_list)
            if (stu == True):
                print(" Registeration SuccessFull !!! ")

        elif (userChoice == 2):
            faculty_name = input("Enter the Faculty Name: ")
            faculty = StudentController(
                "localhost", "root", "1234", "fcit")
            while (faculty.UsernameValidation(faculty_name) == False):
                faculty_name = input("User Already Exist try Another Name: ")
            usre_password = input("Enter The Password")
            desg = input("Enter Your Designation: ")
            subject = input("Enter Your Subject: ")
            faculty_credential_list = faculty.FacultyValidationOfCredentials(
                usre_password, desg, subject)
            faculty_credential_list.append(faculty_name)
            st = faculty.RegisterationOfFaculty(faculty_credential_list)
            if (st == True):
                print("Faculty Registered SuccessFully !!! ")

    elif (userChoice == 2):
        print("1) Student \n")
        print("2) Faculty \n")
        userChoice = int(input("Enter Your Chouce: "))
        if (userChoice == 1):  # student
            student_object=StudentController("localhost", "root", "1234", "fcit")
            name=input("Enter your Name: ")
            if(student_object.UsernameValidation(name) == True):
                print("Account Not Exist !!!")
            else:
                faclt_pass=input("Enter your Password ")
                if(name == student_object.GetStudentNameByPassword(faclt_pass)):
                    print("1) Update Student\n")
                    print("2) Show Student Profile \n")
                    print("3) Delete Student\n")
                    userChoice = int(input("Enter Your Chouce: "))
                    if(userChoice==1):
                        attr=input("Enter the attribute to update ")
                        if(attr=="username"):
                            new_name=input("Enter The New Username: ")
                            while (student_object.UsernameValidation(new_name) == False):
                                new_name = input("User Already Exist try Another Name: ")
                            student_object.UserTableUpdation(attr,name,faclt_pass,new_name)
                        elif(attr=="password"):
                            new_pass=input("Enter The New password: ")
                            student_object.UserTableUpdation(attr,name,faclt_pass,new_pass)
                        elif(attr == "major"):
                            new_major=input("Enter The New Major: ")
                            student_object.StudentTableUpdation(attr,name,new_major)
                        elif(attr=="semester"):
                            new_semester=input("Enter The New Semester: ")
                            student_object.StudentTableUpdation(attr,name,new_semester)
                        elif(attr == "cgpa"):
                            new_cgpa=input("Enter The New CGPA: ")
                            student_object.StudentTableUpdation(attr,name,new_cgpa)
                    elif(userChoice==2):
                        lst=student_object.ShowStudentTable("student",name)
                        print("Name: " + name+"\n")
                        print("password: " + faclt_pass+"\n")
                        print("semester: " , lst[0],"\n")
                        print("CGPA: " , lst[1],"\n")
                        print("Major: " , lst[2],"\n")

                    elif(userChoice==3):
                        student_object.StudentProfileDeletion("student",name)
                else:
                    print("Wrong Password")
        elif (userChoice == 2):  # faculty
            faculty_object=StudentController("localhost", "root", "1234", "fcit")
            name=input("Enter your Name: ")
            if(faculty_object.UsernameValidation(name) == True):
                print("Account Not Exist !!!")
            else:
                faclt_pass=input("Enter your Password ")
                if(name == faculty_object.GetStudentNameByPassword(faclt_pass)):
                    print("1) Update Faculty\n")
                    print("2) Show Faculty Profile\n")
                    print("3) Delete Faculty\n")
                    userChoice = int(input("Enter Your Chouce: "))
                    if(userChoice==1):
                        attr=input("Enter the attribute to update ")
                        if(attr=="username"):
                            new_name=input("Enter The New Username: ")
                            while (faculty_object.UsernameValidation(new_name) == False):
                                new_name = input("User Already Exist try Another Name: ")
                            faculty_object.UserTableUpdation(attr,name,faclt_pass,new_name)
                        elif(attr=="password"):
                            new_pass=input("Enter The New password: ")
                            faculty_object.UserTableUpdation(attr,name,faclt_pass,new_pass)
                        elif(attr=="desination"):
                            new_desig=input("Enter The New Designation: ")
                            faculty_object.facultyTableUpdation(attr,name,new_desig)
                        elif(attr=="subject"):
                            new_sub=input("Enter The New Subject: ")
                            faculty_object.facultyTableUpdation(attr,name,new_sub)
                    elif(userChoice==2):
                        lst=faculty_object.ShowFacultyTable("faculty",name)
                        print("Name: " + name+"\n")
                        print("password: " + faclt_pass+"\n")
                        print("designation: " + lst[0]+"\n")
                        print("Subject: " + lst[1]+"\n")

                    elif(userChoice==3):
                         faculty_object.FacultyProfileDeletion("faculty",name)
                    else:
                        print("Wrong Password")

    status = False

