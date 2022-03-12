from datetime import date
from models import user
from models.Operation import Operation, Transaction
from models.account import Account
from models.date import Date
from models.user import User
class Bank:
    def __init__(self):
        self.date = Date(2022,1,1)
        self.users = {}
        self.accounts = {}
        self.idCount = 0

    def getCurrentDate(self):
        return date

    def increaseDate(self, amount):
        self.date.setDay(date.getDay() + amount)
    
    def getUsers(self):
        return self.users

    def addUser(self, user):
        if user.getEmail() in self.users.keys():
            return -1
        self.users[user.getEmail()] = user

    def getUser(self, email):
        return self.users[email]
        
    def createUser(self, name, email, mobileNumber):
        self.addUser(User(name,email, mobileNumber))

    def createAccount(self, balance, location, userEmail):
        if userEmail not in self.users.keys():
            return -1 
        user = self.users[userEmail]
        newAccount = Account(balance, self.idCount, location, user)
        self.idCount += 1
        user.createAccount(newAccount)
    
    def isPremium(self, account):
        pass

    def calculateRealAmmount(self, IdSrc, IdDest, amount):
        if(self.accounts[IdSrc].getStatus() == True):
            return amount
        else:
            if (self.accounts[IdSrc].getContinent() == self.accounts[IdDest].getContinent()):
                return amount * 1.03
            else:
                return amount * 1.05
            

    def registerTransaction(self, IdSrc, IdDest, ammount):
        accountIds = self.accounts.keys()
        if IdSrc not in accountIds and IdDest not in accountIds:
            return -1
        amount = self.calculateRealAmmount(IdSrc, IdDest, ammount)
        op = Transaction(self.date, amount, self.accounts[IdSrc], self.accounts[IdDest])
        self.accounts[IdSrc].addOperation(op)
        self.accounts[IdDest].addOperation(op)
        self.accounts[IdSrc].setBalance(self.accounts[IdSrc] - amount)
        self.accounts[IdSrc].setBalance(self.accounts[IdDest] + ammount)

    def getAccountBalanceEuros(self, accountId):
        account = self.accounts[accountId]
        return account.getBalance()
    
    def getAccountBalanceDolah(self, accountId):
        account = self.accounts[accountId]
        return account.convertToDollars()

    def getAccountinfo(self, accountId):
        return self.accounts[accountId].toString
    
    def getUserinfo(self, userEmail):
        pass

    def getDate(self):
        return self.date.showDate()


        
         