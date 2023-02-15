class contact():
    def __init__(self,id,n,mob,p):
        self.__name=n
        self.__id=id
        self.mobile = mob
        self.profession=p
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,n):
        if n!=None and n!="":
            self.__name=n
        else:
            self.__name = "default"
    @property
    def id(self):
        return self.__name
    @id.setter
    def name(self,id):
        if id!=None and id!="":
            self.__id=id
        else:
            self.__id = "default"
    @property
    def mobile(self):
        return self.__mobile
    @id.setter
    def mobile(self,mob):
        if mob!=None and mob!="":
            self.__mobile=mob
        else:
            self.__mobile = "default"
    @property
    def profession(self):
        return self.__profession
    @id.setter
    def profession(self,p):
        if p!=None and p!="":
            self.__profession=p
        else:
            self.__profession = "default"


    def printString(self):
        print("Name:",self.__name,"Id:",
              self.__id,"Mobile:",self.__mobile,"Profession",self.__profession)