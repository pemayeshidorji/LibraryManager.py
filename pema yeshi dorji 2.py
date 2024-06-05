import random
import string
import os

# Utility function to generate random account number and password
def generate_account_number():
    return ''.join(random.choices(string.digits, k=10))

def generate_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

# Account class to define the structure of a bank account
class Account:
    def __init__(self, account_number, password, account_type, balance=0.0):
        self.account_number = account_number
        self.password = password
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}")
        else:
            print("Insufficient funds")

    def check_balance(self):
        print(f"Your current balance is {self.balance}")

# BusinessAccount and PersonalAccount subclasses inheriting from Account
class BusinessAccount(Account):
    def __init__(self, account_number, password, balance=0.0):
        super().__init__(account_number, password, "Business", balance)

class PersonalAccount(Account):
    def __init__(self, account_number, password, balance=0.0):
        super().__init__(account_number, password, "Personal", balance)

# Bank class to manage all accounts
class Bank:
    accounts_file = "accounts.txt"

    def __init__(self):
        self.accounts = {}
        self.load_accounts()

    def load_accounts(self):
        if os.path.exists(Bank.accounts_file):
            with open(Bank.accounts_file, 'r') as f:
                for line in f:
                    account_number, password, account_type, balance = line.strip().split(',')
                    balance = float(balance)
                    if account_type == "Business":
                        account = BusinessAccount(account_number, password, balance)
                    else:
                        account = PersonalAccount(account_number, password, balance)
                    self.accounts[account_number] = account

    def save_accounts(self):
        with open(Bank.accounts_file, 'w') as f:
            for account in self.accounts.values():
                f.write(f"{account.account_number},{account.password},{account.account_type},{account.balance}\n")

    def create_account(self, account_type):
        account_number = generate_account_number()
        password = generate_password()
        if account_type == "Business":
            account = BusinessAccount(account_number, password)
        else:
            account = PersonalAccount(account_number, password)
        self.accounts[account_number] = account
        self.save_accounts()
        print(f"Account created successfully. Account Number: {account_number}, Password: {password}")

    def login(self, account_number, password):
        account = self.accounts.get(account_number)
        if account and account.password == password:
            return account
        else:
            print("Invalid account number or password")
            return None

    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            self.save_accounts()
            print(f"Account {account_number} deleted successfully")
        else:
            print("Account does not exist")

    def transfer_money(self, from_account, to_account_number, amount):
        to_account = self.accounts.get(to_account_number)
        if to_account:
            if from_account.balance >= amount:
                from_account.withdraw(amount)
                to_account.deposit(amount)
                self.save_accounts()
                print(f"Transferred {amount} to account {to_account_number}")
            else:
                print("Insufficient funds")
        else:
            print("Receiving account does not exist")

# Main loop for the banking application
def main():
    bank = Bank()

    while True:
        print("\nWelcome to the Bank")
        print("1. Open an account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("1. Business Account")
            print("2. Personal Account")
            account_type_choice = input("Select account type: ")
            if account_type_choice == '1':
                bank.create_account("Business")
            elif account_type_choice == '2':
                bank.create_account("Personal")
            else:
                print("Invalid choice")

        elif choice == '2':
            account_number = input("Enter account number: ")
            password = input("Enter password: ")
            account = bank.login(account_number, password)
            if account:
                while True:
                    print("\n1. Check Balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Transfer Money")
                    print("5. Delete Account")
                    print("6. Logout")
                    user_choice = input("Enter your choice: ")

                    if user_choice == '1':
                        account.check_balance()
                    elif user_choice == '2':
                        amount = float(input("Enter amount to deposit: "))
                        account.deposit(amount)
                        bank.save_accounts()
                    elif user_choice == '3':
                        amount = float(input("Enter amount to withdraw: "))
                        account.withdraw(amount)
                        bank.save_accounts()
                    elif user_choice == '4':
                        to_account_number = input("Enter the account number to transfer to: ")
                        amount = float(input("Enter amount to transfer: "))
                        bank.transfer_money(account, to_account_number, amount)
                    elif user_choice == '5':
                        bank.delete_account(account.account_number)
                        break
                    elif user_choice == '6':
                        break
                    else:
                        print("Invalid choice")
        elif choice == '3':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
