from DB import ConnectDB_Class

class AllValidation(ConnectDB_Class):
    def __init__(self,localhost,user,password,database):
        ConnectDB_Class.__init__(self,localhost,user,password,database)
        pass

    def _nameUniqueness(self,username):
        args=(username)
        query="select username from user where username=%s"
        self.mydbCursor.execute(query,args)
        result = self.mydbCursor.fetchall()
        if(result ==()):
            return True
        else:
            return False
    def _checkCredentialsOfFaculty(self,password,designation,subject):
        faculy_password=password
        faculy_designation=designation
        faculy_subject=subject
        while(faculy_password==""):
            faculy_password=input("Empty, Enter Some Characters !!! Please Enter The Password : ")
        while(faculy_designation==""):
            faculy_designation=input("Empty, Enter Designation !!! Please Enter Again : ")
        while(faculy_subject==""):
            faculy_password=input("Enter The Subject name Again: ")
        mydic=[faculy_password,faculy_designation,faculy_subject]
        return mydic

    def _checkCredentialsOfStudents(self,password,semester,cgpa,major):
        user_password=password
        user_semester=semester
        user_cgpa=cgpa
        user_major=major
        while(password==""):
                user_password=input("Empty, Enter Some Characters !!! Please Enter The Password : ")
                password=user_password
        while(semester <= 0 or semester > 8):
            user_semester=int(input("Enter The Semester between 1 to 8 : "))
            semester=user_semester
        while(cgpa < 0.0 or cgpa>4.0):
                user_cgpa=float(input("Enter Your CGPA greater than 0 and less equal than 4: "))
                cgpa=user_cgpa
        status=True
        while(status):
            if(major =="BSSE" or major=="bsse"):
                status=False
            elif(major=="BCS" or major=="bcs"):
                status=False
            elif(major=="BSIT" or major=="bsit"):
                status=False
            elif(major=="BSDS" or major=="bsds"):
                status=False
            elif(major=="MSDS" or major=="msds"):
                status=False
            elif(major=="MSIT"or major=="msit"):
                status=False
            elif(major=="MSSE" or major=="msse"):
                status=False
            elif(major=="MSCS" or major=="mcs"):
                status=False
            else:
                user_major=input("Enter Again Major: ")
                major=user_major
            
        mydic=[user_password,user_semester,user_cgpa,user_major]
        return mydic
