class User:
    def __init__(self, accountno, password, interest, balance=100, transactions=0):
        self.accountno = accountno
        self.password = password
        self.balance = balance
        self.interest = interest
        self.transactions = transactions
