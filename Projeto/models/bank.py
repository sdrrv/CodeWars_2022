from datetime import date
from Projeto.models import user
from models.date import Date
from models.user import User
class Bank:
    def __init__(self):
        self.date = Date(2022,1,1)
        self.users = {}
    
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
    
     