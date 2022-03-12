from controllers import controller
def terminal():
    while True:
        x = input(":")
        print(controller.adder(int(x), 2))