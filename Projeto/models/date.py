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

    def showDate(self):
        return "[" + self.year + "/" + self.month + "/" + self.day + "]"