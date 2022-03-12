from models.date import Date
from models.user import User
class Operation():
    def __init__(self, date, ammount, src):
        self.date = date
        self.amount = ammount
        self.source = src

    def getAmount(self):
        return self.amount()

class Transaction(Operation):
    def __init__(self, dest):
        self.destination = dest
        self.name = "TRANSACAO entre " + self.source.getName() + " e " + dest.getName() + "no valor de " + self.amount

class ServicePayment(Operation):
    def __init__(self):
        self.name = "Pagamento de servico à Empresa " + self.source.getName() + "no valor de " + self.amount


class Deposit(Operation):
    def __init__(self):
        self.name = "Deposito feito por " + self.source.getName() + "no valor de " + self.amount

class
