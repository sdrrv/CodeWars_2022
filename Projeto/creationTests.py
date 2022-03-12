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
    
    
if __name__ == '__main__':
    unittest.main() 