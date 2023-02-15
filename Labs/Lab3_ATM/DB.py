import pymysql
from Customer import Customer


class DBHandler:
    def __init__(self):
        self.__connection = None
        self.__cursor = None

    def connect(self):
        try:
            self.__connection = pymysql.connect(host='localhost', user='root', password='1234', database='atm')
            self.__cursor = self.__connection.cursor()
        except Exception as e:
            print(str(e))

    def disconnect(self):
        if self.__connection is not None:
            self.__connection.close()

    def select(self, sql):
        try:
            # check if the connection is established or not
            if self.__connection is None:
                self.connect()

            # execute the sql
            self.__cursor.execute(sql)

            # fetch the data (all entries)
            data = self.__cursor.fetchall()

            # return data as list of customers
            customers_list = []

            for row in data:
                customer = Customer(row[1], row[2], float(row[3]))
                customers_list.append(customer)
            return customers_list
        except Exception as e:
            print(str(e))
            return None
        finally:
            self.disconnect()

    def insert(self, sql, args):
        try:
            # check if the connection is established or not
            if self.__connection is None:
                self.connect()

            # execute the sql
            self.__cursor.execute(sql, args)

            # commit the changes
            self.__connection.commit()
        except Exception as e:
            print(str(e))
        finally:
            self.disconnect()

    def update(self, sql, args):
        try:
            # check if the connection is established or not
            if self.__connection is None:
                self.connect()

            # execute the sql
            self.__cursor.execute(sql, args)

            # commit the changes
            self.__connection.commit()
        except Exception as e:
            print(str(e))
        finally:
            self.disconnect()
            

# db = DBHandler()
# db.connect()
# db.update("update customers set balance = 200 where account_no = %s", ('ATMAcc1'))