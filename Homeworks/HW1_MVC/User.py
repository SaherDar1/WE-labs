class User:
    def __init__(self):
        self.__id
        self.__username
        self.__password
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, val):
        self.__id=int(val)
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self,val):
        self.__username=val
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self,val):
        self.__password=val