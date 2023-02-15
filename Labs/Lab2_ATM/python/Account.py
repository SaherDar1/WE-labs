class Account:
    def __init__(self, accountNo="", pin=0, balance=100):
        self.accountNo = accountNo
        self.pin = pin
        self.balance = balance

    def writeInFile(self, num):
        file = open("input.txt", "a")
        s = self.accountNo+","+str(self.pin)+","+str(self.balance)+"\n"
        file.write(s)
        file.close()
        file = open("input.txt")
        lines = file.readlines()
        file.close()
        lines[0] = num + "\n"
        file = open("input.txt", "w")
        file.writelines(lines)
        file.close()
