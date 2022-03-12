import unittest
from models.bank import Bank

class CreationTests(unittest.TestCase):
    def test_createUser(self):
        bank = Bank()
        bank.createUser("Afonso", "afonso@gmail.com", "96786441")
        self.assertAlmostEquals(bank.getUser("afonso@gmail.com").getName(), "Afonso")
    
    def test_createAccount(self): 
        bank = Bank()
        bank.createUser("Afonso", "afonso@gmail.com", "96786441")
        bank.createAccount(0,"Portugal", "afonso@gmail.com")
        self.assertAlmostEquals(bank.getUser("afonso@gmail.com").getName(), "Afonso")
        
    def test_createTransaction(self):
        bank  = Bank()
        bank.createUser("Afonso", "afonso@gmail.com", "96786441")
        id1 = bank.createAccount(0,"Portugal", "afonso@gmail.com")
        
        bank.createUser("Dendas", "dendas@gmail.com", "96745241")
        id2 = bank.createAccount(0,"Brazil", "dendas@gmail.com")
        
        bank.registerTransaction(id1, id2, 20)
        
        self.assertEqual(20, bank.getAccountBalanceEuros(id2))
         
    
    
if __name__ == '__main__':
    unittest.main() 