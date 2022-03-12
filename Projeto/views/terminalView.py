from click import command
from controllers import controller

class Terminal:
    def __init__(self, bank):
        self.bank = bank


    def mainLoop(self):
        print("Select one option")
        print("1. Users")
        print("2. Accounts")
        print("3. Transactions")
        print("4. Others")
        print("5. Exit")

        while True:
            line = input("")
            commands = line.split(" ")
            if commands[0] == "1":
                manageUsers()
            if commands[0] == "2":
                manageAccounts()
            if commands[0] == "3":
                manageTransactions()
            if commands[0] == "4":
                manageOperations()
            if commands[0] == "5":
                return

    def showUserTransactions(self):
        print("a")

    def showUser(self):
        print("b")

    def registerUser(self):
        name = input("Enter your name:")
        email = input("Enter your email:")
        mobilenumber = input("Enter your mobile number:")
        self.bank.createUser(name, email, mobilenumber)

    def manageUsers(self):
        print("Select one operation")
        print("1. Regist User")
        print("2. Show User")
        print("3. Show User Transactions")
        print("4. Go Back")
        print("5. Exit")
        option = input()
        if (option == "1"):
            registerUser()
        if (option == "2"):
            showUser()
        if (option == "3"):
            showUserTransactions()
        if (option == "4"):
            self.mainLoop()
        if (option == "5"):
            exit(0)

    def manageAccounts(self):
        print("Select one operation")
        print("1. Register Account")
        print("2. Show Account")
        print("3. Show Account Transactions")
        print("4. Go back")
        print("5. Exit")
        option = input()
        if (option == "1"):
            registerAccount()
        if (option == "2"):
            showAccount()
        if (option == "3"):
            showAccountTransactions()
        if (option == "4"):
            mainLoop
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
            transferMoney()
        if (option == "2"):
            payServices()
        if (option == "3"):
            self.mainLoop()
        if (option == "4"):
            exit(0)

    def showDate(self):
        self.bank.getDate()

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
    
