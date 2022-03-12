class User:

   def __init__(self, name, email, mobile):
      self.name = name
      self.email = email
      self.mobile = mobile
      self.accounts = []
 
   def getName(self):
      return self.name

   def getEmail(self):
      return self.email

   def getMobile(self):
      return self.mobile

   def getAccounts(self):
      return self.accounts

   def createAccount(self, account):
      self.accounts.append(account)

   def getAccountById(self, accountId):
      for account in self.accounts:
         if accountId == account.getAccountId():
            return account

   def toString(self):
      return "Utilizador com nome: " + self.name + " número de telefone: " + self.mobile
   
