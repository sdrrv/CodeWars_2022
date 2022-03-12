from click import command
from controllers import controller

class Terminal:
    def __init__(self, bank):
        self.bank = bank


    def mainLoop(self):
        print("Select one option")
        print("1. Users")
        print("2. Accounts")
        print("3. Operations")
        print("4. Others")
        print("5. Exit")

        while True:
            line = input("")
            commands = line.split(" ")
            if commands[0] == "1":
                self.manageUsers()
            if commands[0] == "2":
                self.manageAccounts()
            if commands[0] == "3":
                self.manageTransactions()
            if commands[0] == "4":
                self.manageOperations()
            if commands[0] == "5":
                return

    def showUser(self):
        email = input("Enter your email:")
        print(self.bank.getUserinfo(email))
        self.manageUsers()

    def registerUser(self):
        name = input("Enter your name:")
        email = input("Enter your email:")
        mobilenumber = input("Enter your mobile number:")
        self.bank.createUser(name, email, mobilenumber)
        self.manageUsers()

    def manageUsers(self):
        print("Select one operation")
        print("1. Regist User")
        print("2. Show User")
        print("3. Go Back")
        print("4. Exit")
        option = input()
        if (option == "1"):
            self.registerUser()
        if (option == "2"):
            self.showUser()
        if (option == "3"):
            self.mainLoop()
        if (option == "4"):
            exit(0)

    def registerAccount(self):
        

    def manageAccounts(self):
        print("Select one operation")
        print("1. Register Account")
        print("2. Show Account")
        print("3. Show Account Operations")
        print("4. Go back")
        print("5. Exit")
        option = input()
        if (option == "1"):
            self.registerAccount()
        if (option == "2"):
            self.showAccount()
        if (option == "3"):
            self.showAccountTransactions()
        if (option == "4"):
            self.mainLoop()
        if (option == "5"):
            exit(0)

    def manageTransactions(self):
        print("Select one operation")
        print("1. Transfer money")
        print("2. Pay services")
        print("3. Go back")
        print("4. Exit")
        option = input()
        if (option == "1"):
            self.transferMoney()
        if (option == "2"):
            self.payServices()
        if (option == "3"):
            self.mainLoop()
        if (option == "4"):
            exit(0)

    def showDate(self):
        self.bank.showDate()

    def manageOperations(self):
        print("Select one operation")
        print("1. Show Date")
        print("2. Go back")
        print("3. Exit")
        option = input()
        if (option == "1"):
            self.showDate()
        if (option == "2"):
            self.mainLoop()
        if (option == "3"):
            exit(0)
    
