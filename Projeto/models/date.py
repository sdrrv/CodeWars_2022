class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def getDay(self):
        return self.day

    def getMonth(self):
        return self.month

    def getYear(self):
        return self.year

    def setDay(self, day):
        self.day = day

    def setMonth(self, month):
        self.month = month

    def setYear(self, year):
        self.year = year

    def showDate(self):
        return "[" + self.year + "/" + self.month + "/" + self.day + "]"

    def equals(self, date):
        return self.day == date.getDay() and self.month == date.getMonth() and self.year == self.getYear()