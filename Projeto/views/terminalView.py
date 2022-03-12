from click import command
from controllers import controller
def terminal():
    while True:
        line = input(":")
        if not line:
            exit(0)
        commands = line.split(" ")
        if commands[0] == "createUser":
            pass
        
        