from utils import AllValidation
from student import student

class StudentController(AllValidation):
    def __init__(self, localhost, user, password, database):
        AllValidation.__init__(self,localhost, user, password, database)
        pass

    def UsernameValidation(self,name):
        return self._nameUniqueness(name)
    
    def StudentValidationOfCredentials(self,password,semester,cgpa,major):
        return AllValidation._checkCredentialsOfStudents(self,password,semester,cgpa,major)

    def RegisterationOfStudent(self,credentialList): #usre_password,user_semester,user_cgpa,user_major,username
         return AllValidation._RegisterStudent(self,credentialList)

    def FacultyValidationOfCredentials(self,password,designation,subject):
        return AllValidation._checkCredentialsOfFaculty(self,password,designation,subject)
        
    def RegisterationOfFaculty(self,credentialList): #usre_password,designation,subject,username
         return AllValidation._RegisterFaculty(self,credentialList)

    def GetStudentNameByPassword(self,password):
        return AllValidation._GetUserName(self,password)

    def ShowStudentTable(self,table,name):
        return AllValidation._ShowStudentProfile(self,table,name)
    
    def ShowFacultyTable(self,table,name):
        return AllValidation._ShowFacultyProfile(self,table,name)

    def FacultyProfileDeletion(self,table,username):
        AllValidation._DeleteFacultyProfile(self,table,username)

    def StudentProfileDeletion(self,table,username):
        AllValidation._DeleteStudentProfile(self,table,username)
    
    def UserTableUpdation(self,attributename,username,password,value):
        AllValidation._UpdateUserTable(self,attributename,username,password,value)

    def facultyTableUpdation(self,attributename,username,value):
        AllValidation._UpdateFacultyTable(self,attributename,username,value)
        
    def StudentTableUpdation(self,attributename,username,value):
        AllValidation._UpdateStudentTable(self,attributename,username,value)


