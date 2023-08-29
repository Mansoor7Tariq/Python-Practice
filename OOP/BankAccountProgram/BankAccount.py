import os


class BankAccount:
    balance = 0
    account_title = ''
    cnic = ''
    phone_number = ''

    def __init__(self, balance=0, account_title='', cnic='', phone_number=''):
        self.balance = balance
        self.account_title = account_title
        self.cnic = cnic
        self.phone_number = phone_number

    def open_account(self):
        self.account_title = input('Enter Account Title: ')
        self.cnic = input('Enter Cnic: ')
        self.phone_number = input('Enter Phone Number: ')
        self.balance = int(input(
            'If You Want To Add Any Money To Kick Start You Account With Add Here Or Just Enter (0): '))

    def deposit_money(self, amount):
        if self.authenticate_user():
            self.balance = self.balance + amount
            print('Amount Added: ', self.balance)
        else:
            print('Authentication Failed')

    def withdraw_money(self, amount):
        if self.authenticate_user():
            if (amount < self.balance):
                self.balance = self.balance - amount
                print('Amount Left: ', self.balance)
            else:
                print('Not Enough Money In Your Account')
        else:
            print('Authentication Failed')

    def authenticate_user(self):
        print('----- Authentication Process Please Enter Your Info ------')
        if (input('Enter Your Account Title: ') == self.account_title and
                input('Enter Your Cnic: ') == self.cnic):
            return True
        return False

    def get_current_balance(self):
        print('Your Current Balance Is: ', self.balance)

    def print_account_holder_details(self):
        print('Account Title : ', self.account_title)
        print('Cnic : ', self.cnic)
        print('Phone Number : ', self.phone_number)


def menu():
    user_account = BankAccount()

    choice = 0
    while choice != '-1':
        print("Choose an option:")
        print("1. Open a Account")
        print("2. Desposit Money")
        print("3. With Draw Money")
        print("4. See Current Balance")
        print("5. See You Info")
        print("-1. For Exit")

        choice = input("Enter your choice: ")
        os.system('clear')

        if choice == '-1':
            print("Bank Account in Python")
        elif choice == '1':
            user_account.open_account()
        elif choice == '2':
            user_account.deposit_money(
                int(input('Enter Amount You Want To Deposite: ')))
        elif choice == '3':
            user_account.withdraw_money(
                int(input('Enter Amount You Want To WithDraw: ')))
        elif choice == '4':
            user_account.get_current_balance()
        elif choice == '5':
            user_account.print_account_holder_details()
        else:
            print("Invalid choice")


menu()
