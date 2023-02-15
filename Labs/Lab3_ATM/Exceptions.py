class ContactException(Exception):
    def __init__(self, message):
        self.message = message

class ContactNumberNotValid(ContactException):
    pass

class ContactAlreadyExist(ContactException):
    pass




