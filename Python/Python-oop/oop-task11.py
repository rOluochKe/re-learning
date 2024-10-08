"""
Story behind the code:

There was a Bank that offered various types of accounts to its customers. One of the account types was called "Savings Account."

A Savings Account was a special type of account that allowed customers to save their money and earn interest on it.

#####

To represent this Savings Account in code, the bank created a class called "SavingsAccount."

-This class inherited from two other classes: "InterestBearingAccount" and "TransactionHistory." Let's dive into each class and see what they do.

###

The first class, "Account," served as the foundation for all types of bank accounts.

-It had essential attributes like the account number and the balance.

-It also had methods for depositing and withdrawing money from the account. These methods would update the account's balance accordingly.  Both accepting an amount and adding that to the balance property

##

The second class, "InterestBearingAccount," was a specialized type of account that earned interest on the balance.

-In addition to the attributes and methods inherited from the "Account" class, it had an extra attribute called interest_rate

-This attribute represented the interest rate at which the account earned interest.

-The class also had a method called "calculate_interest" that calculated the interest earned based on the balance and the interest rate.

##

The third class, "TransactionHistory," was responsible for keeping track of all the transactions made on an account.

-It had a list to store the transaction history, and methods to add transactions and display them.

##

Now, let's go back to the "SavingsAccount" class. It inherited from both "InterestBearingAccount" and "TransactionHistory," combining their functionalities into a single class.

-It had an additional initialization method that called the initialization methods of its parent classes to set up the necessary attributes.

#####

Outside the classes, a new Savings Account was created with an account number "SA123," an initial balance of $1000, and an interest rate of 0.05 (5%). The account was then used to deposit $500 and withdraw $200. The interest earned on the account and the current balance were calculated.

To keep track of the transactions, two transaction records were added to the account's transaction history using the "add_transaction" method. Finally, the transaction history was displayed, showing the deposit and withdrawal transactions.

At the end of the story, the account balance and the interest earned were printed to give the customer an overview of their savings account.

This provides a basic structure for managing a savings account, calculating interest, and maintaining a transaction history. It can be used as a starting point for building more sophisticated banking systems or as a learning resource for understanding inheritance and class relationships in Python.
"""


class Account:
    def __init__(self, act_num, balance):
        self.account = act_num
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdrawl(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Not Enough funds!")

    def get_balance(self):
        return self.balance


class InterestAccount(Account):
    def __init__(self, act_num, balance, interest_rate):
        Account.__init__(self, act_num, balance)
        self.interest_rate = interest_rate

    def calc_interest(self):
        return self.balance * self.interest_rate


class Transactions:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def history(self):
        for transaction in self.transactions:
            print(transaction)


class SavingsAccount(InterestAccount, Transactions):
    def __init__(self, account_number, balance, interest_rate):
        InterestAccount.__init__(self, account_number, balance, interest_rate)
        Transactions.__init__(self)


savings = SavingsAccount("SA001", 5000, 0.08)
savings.deposit(2500)
# 7500
savings.withdrawl(650)

interest = savings.calc_interest()
balance = savings.get_balance()

savings.add_transaction("Deposit: 2500")
savings.add_transaction("Withdrawl: 650")

savings.history()

print("Balance:", balance)
print("Interest:", interest)
