from User import User
class student(User):
    def __init__(self,semester,CGPA,Major):
        self.__id
        pass
        self.__semester=semester
        self.__CGPA=CGPA
        self.__Major=Major
    @property
    def id(self):
        return self.__id
    @property
    def semester(self):
        return self.__semester
    @property
    def CGPA(self):
        return self.__CGPA
    @property
    def Major(self):
        return self.__Major
    @id.setter
    def id(self,val):
        self.__id=int(val)
    @semester.setter
    def semester(self,val):
        self.__semester=int(val)
    @CGPA.setter
    def CGPA(self,val):
        self.__CGPA=float(val)
    @Major.setter
    def Major(self,val):
        self.__Major=val

