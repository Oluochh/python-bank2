class Account:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
        self.balance=0
        self.loan=0
        self.loan_limit=500

    def deposit(self,amount):
        if amount<=0:
            return f"Amount must be greater than 0."  
        else:
            self.balance+=amount
            return f"Dear {self.name} you have deposited {amount},your new balance is KSH{self.balance}"
    def show_balance(self):
        return self.balance
    def withdraw(self,amount):
        if amount<=0:
            return f"amount must be greater than zero"
        elif amount>self.balance:
            return f"You can not withdraw KES {amount},available balance is {self.balance}"
        else:
            self.balance-=amount
            return f"You have withdrawn {amount},your balance is KES{self.balance}"
    def borrow(self,amount):
        if amount<=self.loan_limit:
            self.loan+=amount
            self.balance+=self.loan
            return f"Dear {self.name}, you have borrowed KES{amount}.Your loan of {self.loan} is due on november 1st,your balance is KES{self.balance}"
        else:
            return f"Your loan request of KES{amount} is unsuccessful because your loan limit is {self.loan_limit}"

                          
        
                        

                          
                        
                        
                
                 




                
                   



                    
   