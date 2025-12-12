class BankAccount:

    # Class attribute
    bank_name = "National Bank"

    # Constructor
    def __init__(self, acc_no, holder, balance):
        self.acc_no = acc_no          # instance attribute
        self.holder = holder
        self.balance = balance

    # Instance method
    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    # Instance method
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    # Class method
    @classmethod
    def change_bank(cls, new_name):
        cls.bank_name = new_name

    # Static method
    @staticmethod
    def welcome():
        print("Welcome to the banking system!")

acc1 = BankAccount(101, "Peter", 500)
acc2 = BankAccount(102, "Ann", 1000)

acc1.deposit(200)
acc1.withdraw(100)
BankAccount.change_bank("Super Bank")
BankAccount.welcome()
