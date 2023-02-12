import pymysql
class ConnectDB_Class:
    def __init__(self,host,user,password,databaseName):
        self.__host=host
        self.__user=user
        self.__password=password
        self.__databaseName=databaseName
        self.connectionStatus=False
        self.mydb = None
        self.mydbCursor=None
        self.uniqueness=True
        checkStatus=False
        while(not(checkStatus)):
            try:
                self.mydb = pymysql.connect(host=self.__host, user=self.__user, password=self.__password, database=self.__databaseName)
                self.mydbCursor = self.mydb.cursor()
                checkStatus=True
                print("Connected Successfully")
            except Exception as e:
                print(str(e))
                checkStatus=False
                self.__host=input("Enter Host Name: ")
                self.__user=input("Enter User Name: ")
                self.__password=input("Enter Password: ")
                self.__databaseName=input("Enter Database Name: ")

    def _RegisterStudent(self,args):  #user_password,user_semester,user_cgpa,user_major,username
        Query="insert into user (username,password) values (%s ,%s)"
        Arguments=(args[3],args[0])
        self._ExecuteQueryWithParameters(Query,Arguments)
        query="Select id from user where username='"+ args[3]+"'"
        self.mydbCursor.execute(query)
        id = self.mydbCursor.fetchall()
        Args=(args[1],args[2],args[3],id[0][0])
        query="insert into student(semester, cgpa, major, user_id) values(%s, %s, %s , %s)"
        self._ExecuteQueryWithParameters(query,Args)
        return True
    def _RegisterFaculty(self,args):  #username,password,desination,subject,username
        Query="insert into user (username,password) values (%s ,%s)"
        Arguments=(args[3],args[0])
        self._ExecuteQueryWithParameters(Query,Arguments)
        query="Select user_id from user where username='"+ args[3]+"'"
        self.mydbCursor.execute(query)
        id = self.mydbCursor.fetchall()
        Args=(args[1],args[2],id[0][0])
        query="insert into faculty(designation, subject, user_id) values(%s, %s, %s)"
        self._ExecuteQueryWithParameters(query,Args)
        return True

    def _GetUserName(self,password):
        query="Select username from user where password='"+ password+"'"
        self.mydbCursor.execute(query)
        name = self.mydbCursor.fetchall()
        return name[0][0]
    def _ShowFacultyProfile(self, tabelName, userName):
        mydic=[]
        query="Select user_id, password from user where username='"+userName+"'"
        self.mydbCursor.execute(query)
        id = self.mydbCursor.fetchall()
        args=(id[0][0])
        query="Select designation, subject  from faculty where user_id=%s"
        self.mydbCursor.execute(query,args)
        result = self.mydbCursor.fetchall()
        mydic.append(result[0][0])
        mydic.append(result[0][1])
        return mydic

    def _ShowStudentProfile(self, tabelName, userName):
        mydic=[]
        query="Select id, password from user where username='"+userName+"'"
        self.mydbCursor.execute(query)
        user_id = self.mydbCursor.fetchall()
        args=(user_id[0][0])
        query="Select semester, cgpa, major from student where user_id=%s"
        self.mydbCursor.execute(query,args)
        result = self.mydbCursor.fetchall()
        mydic.append(result[0][0])
        mydic.append(result[0][1])
        mydic.append(result[0][2])
        return mydic

    def _DeleteFacultyProfile(self,tableName,username):
        query="Select user_id from user where username='"+username+"'"
        self.mydbCursor.execute(query)
        user_id = self.mydbCursor.fetchall()
        query="delete from faculty where user_id=%s"
        args=(user_id[0][0])
        self._ExecuteQueryWithParameters(query,args)
        query="delete from user where user_id=%s"
        args=(user_id[0][0])
        self._ExecuteQueryWithParameters(query,args)
    
    def _DeleteStudentProfile(self,tableName,username):
        query="Select user_id from user where username='"+username+"'"
        self.mydbCursor.execute(query)
        user_id = self.mydbCursor.fetchall()
        query="delete from student where user_id=%s"
        args=(user_id[0][0])
        self._ExecuteQueryWithParameters(query,args)
        query="delete from user where user_id=%s"
        args=(user_id[0][0])
        self._ExecuteQueryWithParameters(query,args)

    def _UpdateUserTable(self,attributename,username,password,val):
        if(attributename=="username"):
            query="update user set username=%s where username=%s and password=%s"
            args=(val,username,password)
            self._ExecuteQueryWithParameters(query,args)
        else:
            query="update user set password=%s where username=%s and password=%s"
            args=(val,username,password)
            self._ExecuteQueryWithParameters(query,args)
    def _UpdateFacultyTable(self,AttributeName,username,val):
        if(AttributeName=="subject"):
            query="update faculty set subject=%s where user_id=(select user_id from user where username=%s)"
            args=(val,username)
            self._ExecuteQueryWithParameters(query,args)
        else:
            query="update faculty set designation=%s where user_id=(select user_id from user where username=%s)"
            args=(val,username)
            self._ExecuteQueryWithParameters(query,args)
    def _UpdateStudentTable(self,AttributeName,username,val):
        if(AttributeName=="major"):
            query="update student set major=%s where user_id=(select user_id from user where username=%s)"
            args=(val,username)
            self._ExecuteQueryWithParameters(query,args)
        elif(AttributeName=="semester"):
            query="update student set semester=%s where user_id=(select user_id from user where username=%s)"
            args=(val,username)
            self._ExecuteQueryWithParameters(query,args)
        elif(AttributeName=="cgpa"):
            query="update student set cgpa=%s where user_id=(select user_id from user where username=%s)"
            args=(val,username)
            self._ExecuteQueryWithParameters(query,args)


    def _ExecuteQueryWithParameters(self,query,args):
        self.mydbCursor.execute(query,args)
        self.mydb.commit()

   