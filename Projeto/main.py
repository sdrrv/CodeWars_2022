from views.terminalView import Terminal
from views.website import create_app
from models.bank import Bank


#app = create_app()

if __name__ == '__main__':
    #app.run(debug=True)
    
    bank = Bank()    
    term = Terminal(bank)
    term.mainLoop()

 