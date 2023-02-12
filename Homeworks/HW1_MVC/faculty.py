from User import User

class faculty(User):
    def __init__(self):
        pass
        self.__id
        self.__designation
        self.__subject

    @property
    def id (self):
        return self.__id
    @id.setter
    def id (self,val):
        self.__id=int(val)

    @property
    def designation(self):
      return self.__designation
    @designation.setter
    def designation(self, val):
       self.__designation=val

    @property
    def subject (self):
        return self.__subject  

    @subject.setter
    def subject (self,val):
        self.__subject =val