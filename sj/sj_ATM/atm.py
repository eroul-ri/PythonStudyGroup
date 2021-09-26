import sys

class account:
    def __init__(self, name=None, accountNum=None, balance=0):
        self.name = name
        self.accountNum = accountNum
        self.balance = balance

    def deposit(self, money):
        self.money = money
        self.balance += money

    def withdrawal(self, money):
        self.money = money
        self.balance -= money

    def transfer(self, opponentname, opponentaccountNum, money):
        self.opponentname = opponentname
        self.opponentaccountNum = opponentaccountNum
        self.money = money
        self.balance -= money


