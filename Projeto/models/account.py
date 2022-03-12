CONVERTION_EUR_DOLLAR = 1.09
from models.user import User
import pycountry_convert as pc
import random
class Account:
    def __init__(self,balance, account_id, location, user):
        self.user = user
        self.balance = balance
        self.account_id = account_id
        self.location = location
        self.operations = []
        self.continent = self.selectContinent(location)
        self.premium = True if balance >= 5000 else False

    def toString(self):
        string = "Premium" if self.premium else "Normal"
        return "Conta " + string + " com id " + str(self.getAccountId()) + " do utilizador " + str(self.getUser().getName()) + " com balanco " + str(self.getBalance()) + "€ localizada em " + str(self.get_location())
    
    def getName(self):
        return str(self.account_id)

    def getUser(self):
        return self.user

    def getStatus(self):
        return self.premium
    
    def getContinent(self):
        return self.continent
        
    def getBalance(self):
        return self.balance

    def getAccountId(self):
        return self.account_id
    
    def setBalance(self, newBalance):
        self.balance = newBalance
        self.premium = True if self.balance >= 5000 else False

    def get_location(self):
        return self.location

    def getOperations(self):
        return self.operations

    def convertToDollars(self):
        return "{:.2f}".format(self.get_balance()*CONVERTION_EUR_DOLLAR)

    def addOperation(self, operation):
        self.operations.append(operation)

    def searchOperation(self, date):
        for operation in self.operations:
            if operation.getDate().equals(date):
                return operation

    def selectContinent(self, country_name):
        newCountry = ""
        if (country_name[0].isupper() is False):
            newCountry+=country_name[0].upper()
            newCountry+=country_name[1:]
        else:
            newCountry = country_name
        country_alpha2 = pc.country_name_to_country_alpha2(newCountry)
        country_continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
        country_continent_name = pc.convert_continent_code_to_continent_name(country_continent_code)
        return country_continent_name








