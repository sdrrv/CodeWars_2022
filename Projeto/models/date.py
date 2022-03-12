import datetime

class Date:
    def __init__(self, year, month, day):
        self.date = datetime.datetime(year, month, day)

    def getDay(self):
        return self.date.day

    def getMonth(self):
        return self.date.month

    def getYear(self):
        return self.date.year

    def increaseDay(self, amount):
        self.date+= datetime.timedelta(days=amount)

    def increaseMonth(self, amount):
        self.date += datetime.timedelta(months = amount)

    def increaseYear(self, amount):
        self.year += datetime.timedelta(years = amount) 

    def showDate(self):
        return "[" + str(self.getYear()) + "/" + str(self.getMonth()) + "/" + str(self.getDay()) + "]"

    def equals(self, date):
        return self.getDay() == date.getDay() and self.getMonth() == date.getMonth() and self.getMonth() == self.getYear()