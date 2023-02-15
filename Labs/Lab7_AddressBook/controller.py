from Exceptions import *

import time

class ContactController():
    def __init__(self):
        self.__student = ContactController(None, None, None, None, None)
        self.__db = DB()

    @property
    def contact(self):
        return self.__contact

    @contact.setter
    def contact(self, contact):
        self.__contact = contact

    def ShowContact(self):
        try:
            print("-"*45)
            print("Welcome to Address Book")
            print("-"*45)
            name = input("Enter your username: ")
            id = input("Enter your id: ")
            mobileno = input("Enter your Mobile no: ")
            Profession = input("Enter your Profession: ")
            contacts = self.__db.get_user(name, id,mobileno,Profession)
            if  contacts!= None:
                ContactController = self.__db.get_contacts_by_id(contacts.Id)
                if contacts != None:
                    self.contacts = contacts
                    self.contacts.id = contacts.id
                    self.contacts.mobileno = contacts.mobileno
                    self.contacts.Profession = contacts.Profession
                    return True
                else:
                    print("Invalid credentials")
                    time.sleep(1)
                    return False

            else:
                print("Invalid credentials")
                return False
        except Exception as e:
            print(e)
            return False

    def CreateNewContact(self):
        try:
            print("-"*45)
            print("Welcome to the Address Book")
            print("-"*45)
            name = input("Enter your username: ")
            print("Checking if username is available...")

            time.sleep(1)

            if self.__db.if_username_available(name):
                id = input("Enter your id: ")
                self.__contacts.name = name
                self.__contacts.id= id
                self.__contacts.mobileno = input("Enter your mobileno: ")
                self.__contacts.city = input("Enter your city: ")
                self.__contacts.profession = input("Enter your profession: ")

                if self.contacts.name == "" or self.contacts.id == "" or self.contacts.mobileno == "" or self.contacts.city == "" or self.contacts.profession == "":
                    print("Invalid input, please try again")
                    self.register()
                else:
                    id = self.__db.CreateNewContact(
                        self.contacts.name, self.contacts.id)
                    if id != -1:
                        self.contacts.ID = id
                        self.__db.CreateNewContact(
                            self.contact.name, self.contact.id, self.contact.city, self.contact.profession)
                        print("Account Creation  successful")
                        time.sleep(1)
                        return True
                    else:
                        print("Account creation failed")
                        time.sleep(1)
                        return False
            else:
                print("\nUsername not available\n")
                self.register()
        except Exception as e:
            print(e)
            return False

    def view_Contact(self):
        print("-"*45)
        print(f"{self.contacts.name}'s Profile")
        print("-"*45)
        print("id: ".ljust(20), self.contacts.id)
        print("Name: ".ljust(20) + self.contacts.name)
        print("City: ".ljust(20) + self.contacts.city)
        print("Mobile No: ".ljust(20) + self.contacts.mobileno)
        print("-"*45)

     