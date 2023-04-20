# Write a Python class named Circle constructed by a radius and two methods which will compute the area and the
# perimeter of a circle.
class Circle:
    def __init__(self, radius: int):
        self.radius = radius

    def circle_area(self):
        return 3.14 * pow(self.radius, 2)

    def circle_perimeter(self):
        return 3.14 * self.radius * 2


circle_object = Circle(10)
print(circle_object.circle_area())
print(circle_object.circle_perimeter())


# 2. Write a Python program to create two empty classes, Student and Marks. Now create some instances and check
# whether they are instances of the said classes or not. Also, check whether the said classes are subclasses of the
# built-in object class or not.

class Student:
    pass


class Marks:
    pass


student = Student()
marks = Marks()

print(isinstance(marks, Student))
print(isinstance(marks, Marks))

print(isinstance(Student, object))
print(isinstance(Marks, object))


# A Bank
#
# Using the Account class as a base class, write two derived classes called SavingsAccount and CurrentAccount. A
# SavingsAccount object, in addition to the attributes of an Account object, should have an interest attribute and a
# method which adds interest to the account. A CurrentAccount object, in addition to the attributes of an Account
# object, should have an overdraft limit attribute.
#
# Now create a Bank class, an object of which contains an array of Account objects. Accounts in the array could be
# instances of the Account class, the SavingsAccount class, or the CurrentAccount class. Create some test accounts (
# some of each type).
#
# Write an update method in the Bank class. It iterates through each account, updating it in the following ways:
# Savings accounts get interest added (via the method you already wrote); CurrentAccounts get a letter sent if they
# are in overdraft. (use print to 'send' the letter).
#
# The Bank class requires methods for opening and closing accounts, and for paying a dividend into each account.


class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount: int):
        self.balance += amount

    def withdraw(self, amount: int):
        self.balance -= amount

class SavingsAccount(Account):

    def __init__(self, start_balance: int = 0, interest: float = 0):
        super().__init__(start_balance)
        self.interest = interest

    def add_interest(self, interest: float = 0):
        self.interest = interest


class CurrentAccount(Account):
    def __init__(self, start_balance:int = 0, overdraft: int = 0):
        super().__init__(start_balance)
        self.overdraft = overdraft


class Bank:
    def __init__(self, accounts: dict = {}):
        self.accounts = accounts

    def create_account(self, account_number: str, account_type: str):
        if (account_type == 'Saving'):
            self.accounts[account_number] = SavingsAccount()
        elif (account_type == 'Current'):
            self.accounts[account_number] = CurrentAccount()
        else:
            raise "Error: Wrong Account Type"

    def close_account(self, account_number: str):
        del self.accounts[account_number]
        return

    def update(self):
        for i in self.accounts:
            if isinstance(self.accounts[i], CurrentAccount) and self.accounts[i].balance < 0:
                print(f"Account {i} is in overdraft")
            elif isinstance(self.accounts[i], SavingsAccount):
                self.accounts[i].add_interest(5)

    def get_account(self, account_number: str):
        return self.accounts[account_number]

# bank = Bank.create_account('12345')
bank = Bank()
bank.create_account('1', 'Current')
bank.create_account('2', 'Current')
bank.create_account('3', 'Saving')
bank.create_account('4', 'Current')
bank.close_account('2')
bank.get_account('4').deposit(5)
bank.get_account('1').withdraw(5)

bank.update()

