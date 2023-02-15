import pymysql as py

from Account import Account
from Exceptions import AccountNotFound


class DB:
    def __init__(self, host="localhost", user="root", password="DvoraK567", database="lab4"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def __makeConnectionWithDB(self):
        con = py.connect(host=self.host, user=self.user,
                         password=self.password, database=self.database)
        cursor = con.cursor()
        return (con, cursor)

    def __closeConnection(self, con, cursor):
        if (cursor != None):
            cursor.close()
        if (con != None):
            con.close()

    def register_account(self, account):
        tup = self.__makeConnectionWithDB()
        con = tup[0]
        cursor = tup[1]
        query = "insert into user values(%s,%s,%s,%s,%s)"
        args = (account.accountno, account.password, account.balance,
                account.interest, account.transactions)
        cursor.execute(query, args)
        con.commit()
        query = "insert into account values(%s,%s)"
        args = (account.accountno, account.type)
        cursor.execute(query, args)
        con.commit()
        self.__closeConnection(con, cursor)
        return True

    def login(self, accountno, password):
        tup = self.__makeConnectionWithDB()
        con = tup[0]
        cursor = tup[1]
        query = "select  count(*) from user where accountno = %s and password = %s"
        args = (accountno, password)
        cursor.execute(query, args)
        self.__closeConnection(con, cursor)
        if cursor.fetchone()[0] == 0:
            return False
        return True

    def isAccountExists(self, accountno):
        tup = self.__makeConnectionWithDB()
        con = tup[0]
        cursor = tup[1]
        query = "select  count(*) from user where accountno = %s"
        args = (accountno)
        cursor.execute(query, args)
        self.__closeConnection(con, cursor)
        if cursor.fetchone()[0] == 0:
            return False
        return True

    def view_balance(self, accountno, password):
        tup = self.__makeConnectionWithDB()
        con = tup[0]
        cursor = tup[1]
        query = "select balance from user where accountno = %s and password = %s"
        args = (accountno, password)
        cursor.execute(query, args)
        balance = cursor.fetchone()[0]
        self.__closeConnection(con, cursor)
        return balance

    def adjust_balance(self, accountno, password, amount):
        tup = self.__makeConnectionWithDB()
        con = tup[0]
        cursor = tup[1]
        query = "update user set balance = %s where accountno = %s and password = %s"
        args = (amount, accountno, password)
        cursor.execute(query, args)
        con.commit()
        self.__closeConnection(con, cursor)

    def transfer_amount(self, accountno2, amount):
        tup = self.__makeConnectionWithDB()
        con = tup[0]
        cursor = tup[1]
        query = "update user set balance = %s where accountno = %s"
        args = (amount, accountno2)
        cursor.execute(query, args)
        con.commit()
        self.__closeConnection(con, cursor)

    def get_balance(self, accountno):
        tup = self.__makeConnectionWithDB()
        con = tup[0]
        cursor = tup[1]
        query = "select balance from user where accountno = %s"
        args = (accountno)
        cursor.execute(query, args)
        balance = cursor.fetchone()[0]
        self.__closeConnection(con, cursor)
        return balance
