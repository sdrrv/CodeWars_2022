from views.terminalView import terminal
from views.website import create_app
from models.bank import Bank


#app = create_app()

if __name__ == '__main__':
    #app.run(debug=True)
    bank = Bank()    
    terminal(bank)

 