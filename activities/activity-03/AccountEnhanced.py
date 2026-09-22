class Account:
    def __init__(self, accountNumber, name, age, initialBalance, accountType):
        self.__accountNumber = accountNumber
        self.__name = name
        self.__age = max(age, 18)
        self.__accountType = accountType if accountType in ("Savings", "Current") else "Savings"
        self.__balance = max(initialBalance, self.__minimum_balance())
        self.__status = "Active"
        self.__pin = None

    def __minimum_balance(self):
        return 500.0 if self.__accountType == "Savings" else 1000.0

    def deposit(self, amount):
        if self.__status != "Active" or amount <= 0:
            return False

        self.__balance += amount
        return True

    def withdraw(self, amount, pin):
        if self.__status != "Active":
            return False
        if not self.verifyPin(pin):
            return False
        if amount <= 0 or self.__balance - amount < self.__minimum_balance():
            return False

        self.__balance -= amount
        return True

    def closeAccount(self):
        if self.__status == "Inactive":
            return False

        self.__status = "Inactive"
        return True

    def reopenAccount(self):
        if self.__status == "Active":
            return False

        self.__status = "Active"
        return True

    def setPin(self, pin):
        if isinstance(pin, bool) or not isinstance(pin, int) or pin < 1000 or pin > 9999:
            return False

        self.__pin = pin
        return True

    def verifyPin(self, pin):
        return self.__pin is not None and self.__pin == pin

    def hasPin(self):
        return self.__pin is not None

    def getAccountNumber(self):
        return self.__accountNumber

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getBalance(self):
        return self.__balance

    def getAccountType(self):
        return self.__accountType

    def getStatus(self):
        return self.__status

    def setName(self, name):
        self.__name = name

    def setAge(self, age):
        self.__age = age
