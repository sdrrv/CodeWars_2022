from random import random

from models.date import Date
from models.user import User

class Operation:
    def __init__(self, date, ammount, src):
        self.date = date
        self.amount = ammount
        self.source = src

    def getAmount(self):
        return self.amount()

    def getDate(self):
        return self.date

class Transaction(Operation):
    def __init__(self, date, amount, src, dest):
        super().__init__(date, amount, src)
        self.destination = dest
        self.name = "Transacao entre " + str(self.source.getName()) + " e " + str(dest.getName()) + "--- " + str(self.amount) + \
                    " - " + self.date.showDate()

    def getName(self):
        return self.name

class ServicePayment(Operation):
    def __init__(self, date, ammount, src):
        super().__init__(date, ammount, src)
        self.name = "Pagamento de servico à Empresa " + random.randint(10000000, 99999999) + "--- " + str(self.amount) + \
                    " - " + self.date.showDate()
    def getName(self):
            return self.name

class Deposit(Operation):
    def __init__(self, date, amount, src):
        super().__init__(date, amount, src)
        self.name = "Deposito feito por " + self.source.getName() + " --- " + str(self.amount) + \
                    " - " + self.date.showDate()

    def getName(self):
            return self.name


class Withdraw(Operation):
    def __init__(self, date, amount, src):
        super().__init__(date, amount, src)
        self.name = "Levantamento feito por " + self.source.getName() + "--- " + str(self.amount) + \
                    "- na data " + self.date.showDate()

    def getName(self):
        return self.name                
