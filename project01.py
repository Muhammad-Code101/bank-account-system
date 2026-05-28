# This is a half finished feature
import random

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.account_number = random.randint(10000000, 99999999)

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount of {amount} has been deposited in your account")
        print(f"Current balance: {self.balance}")

        with open("Transaction.txt", "a") as f:
            f.write(f"Deposited {amount}\n")

    def add_interest(self, rate):
        interest = self.balance * (rate  / 100)
        self.balance += interest
        print(f"Interest Added: {interest}\nCurrent Balance: {self.balance}")

    def take_loan(self, amount):
        if amount > self.balance * 2:
            print("Loan amount too high! Maximum loan is twice your balance.")
        else:
            self.balance += amount
            print(f"Loan of {amount} approved!")
            print(f"Current balance: {self.balance}")

            with open("Transaction.txt", "a") as f:
                f.write(f"Loan taken: {amount}\n")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Amount of {amount} has been deducted from your balance")
            print(f"Current balance: {self.balance}")

            with open("Transaction.txt", "a") as f:
                f.write(f"Deducted {amount}\n")

    def transfer(self, amount):
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print(f"Amount of {amount} has been successfully transferred")
            print(f"Current balance: {self.balance}")

            with open("Transaction.txt", "a") as f:
                f.write(f"Transferred {amount}\n")

    def show(self):
        print(f"Account holder: {self.name}\nAccount Number: {self.account_number}\nBalance: {self.balance}")
        print("---------------------------------------")

account = BankAccount("Muhammad Raza", 20000000)
account.show()
account.add_interest(5)
account.deposit(10000)
account.withdraw(100)
account.transfer(200)
account.take_loan(5000)