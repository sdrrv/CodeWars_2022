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
        return "[" + self.year + "/" + self.month + "/" + self.day + "]"

    def equals(self, date):
        return self.day == date.getDay() and self.month == date.getMonth() and self.year == self.getYear()