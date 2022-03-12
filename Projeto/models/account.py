CONVERTION_EUR_DOLLAR = 1.09
from models.user import User
import random
class Account:
    def __init__(self,balance, account_id, location):
        self.balance = balance
        self.account_id = account_id
        self.location = location
        self.operations = []
        self.continent

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







class Premium_account(Account):
    pass








