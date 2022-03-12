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
        self.name = "Transacao entre " + self.source.getName() + " e " + dest.getName() + "no valor de " + self.amount + \
                    ", na data " + self.date.showDate()

class ServicePayment(Operation):
    def __init__(self, date, ammount, src):
        super().__init__(date, ammount, src)
        self.name = "Pagamento de servico à Empresa " + random.randint(10000000, 99999999) + "no valor de " + self.amount + \
                    ", na data " + self.date.showDate()


class Deposit(Operation):
    def __init__(self, date, amount, src):
        super().__init__(date, amount, src)
        self.name = "Deposito feito por " + self.source.getName() + "no valor de " + self.amount + \
                    ", na data " + self.date.showDate()

class Withdraw(Operation):
    def __init__(self, date, amount, src):
        super().__init__(date, amount, src)
        self.name = "Levantamento feito por " + self.source.getName() + "no valor de " + self.amount + \
                    ", na data " + self.date.showDate()
