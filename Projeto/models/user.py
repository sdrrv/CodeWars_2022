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
   
