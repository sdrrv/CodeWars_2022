CONVERTION_EUR_DOLLAR = 1.09
from models.user import User
import pycountry_convert as pc
import random
class Account:
    def __init__(self,balance, account_id, location):
        self.balance = balance
        self.account_id = account_id
        self.location = location
        self.operations = []
        self.continent = self.selectContinent(location)

    def get_balance(self):
        return self.balance

    def get_accountId(self):
        return self.account_id

    def get_location(self):
        return self.location

    def get_operations(self):
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








