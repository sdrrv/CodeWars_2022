from click import command
from controllers import controller
def terminal():
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

def showUserTransactions():
    print("a")

def showUser():
    print("b")

def registerUser():
    name = input("Enter your name:")
    email = input("Enter your email:")
    mobilenumber = input("Enter your mobile number:")
    createUser(name, email, mobilenumber)

def manageUsers():
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
        terminal()
    if (option == "5"):
        exit(0)

def manageAccounts():
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
        terminal()
    if (option == "5"):
        exit(0)

def manageTransactions():
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
        terminal()
    if (option == "4"):
        exit(0)

def manageOperations():
    print("Select one operation")
    print("1. Show Date")
    print("2. Go back")
    print("3. Exit")
    option = input()
    if (option == "1"):
        showDate()
    if (option == "2"):
        terminal()
    if (option == "3"):
        exit(0)
    
