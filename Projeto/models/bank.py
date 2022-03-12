from datetime import date
from models import *
class Bank:
    def __init__(self):
        self.date = date(2022,1,1)
        self.users = {}
    
    def getCurrentDate(self):
        return date
    def increaseDate(self, amount):
        self.date.setDay(date.getDay() + amount)
    
    def getUsers(self):
        return self.users
    def addUser(self, user):
        self.users[user.getEmail()] = user
    def getUser(self, email):
        return self.users[email]
    
    