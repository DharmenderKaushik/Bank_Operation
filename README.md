
# Bank Operation

Bank Operation is a Python practice project that focuses on essential programming concepts such as Loops, Functions and  object-oriented programming (OOP). It provides a simulated banking experience with features like account creation, Deposit amount,Withdraw amount, MiniStatement.


## Installation

Install my-project with npm

```bash
  pip install time
```
Import-:
```
from time import sleep
```

    
## Features

- Account Creation
- Deposit amount
- Withdraw amount
- MiniStatement


## Usage
Here is a sample code of Bank Operation -:
```javascript
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
}
```


## Operations 

```
Welcome to State Bank Of India , Rewari,Haryana,India
Enter Your name : Dharmender kaushik
Enter Your Phone number : 93062.....
Enter Your address : Rewari
Hello Dharmender kaushik, congratulations your account is created successfully.

Please Select any Option : 
1.Deposit
2.Withdraw
3.Ministatement
4.Exit
```


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://github.com/DharmenderKaushik)

