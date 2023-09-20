# Bank operation using OOP
from time import sleep


class Bank:
    bankname = "State Bank Of India"
    branch = "Rewari,Haryana,India"

    # create account
    def __init__(self, username, phone_number, address):
        self.username = username
        self.phone_number = phone_number
        self.address = address
        self.balance = 0.0  # set account balance to 0.0
        print(
            f'Hello {self.username}, congratulations your account is created successfully')

    # depoist
    def deposit(self, amount):
        self.balance = self.balance+amount
        print(f'{amount} deposited successfully')

    # withdraw
    def withdraw(self, amount):
        if amount < self.balance:
            self.balance = self.balance-amount
            print(f'{amount} withdraw successfully')
        else:
            print('Insufficent Fund...')

    # ministatement
    def ministatement(self):
        print(f'Your account balance is {self.balance}')


print(f'Welcome to {Bank.bankname} , {Bank.branch}')

# collect user data for account creation
username = input('Enter Your name : ')
phone_number = input('Enter Your Phone number : ')
address = input('Enter Your address : ')

# object creation based on user provided data
b = Bank(username, phone_number, address)

while True:
    print('\nPlease Select any Option : ')
    print('1.Deposit\n2.Withdraw\n3.Ministatement\n4.Exit')
    option = int(input())

    if option == 1:
        amount = float(input('Enter Deposited amount : '))
        b.deposit(amount)

    elif option == 2:
        amount = float(input('Enter Withdraw amount : '))
        b.withdraw(amount)

    elif option == 3:
        b.ministatement()

    elif option == 4:
        # print("kindly wait for a moment ........")
        loading = 'Wait...\n'
        for i in range(7):
            print(loading[i], end=' ', flush=True)
            sleep(0.5)
        print('\nThanks for using State Bank Of India ')
        break
    else:
        print('Invalid Option, please enter a valid option')
