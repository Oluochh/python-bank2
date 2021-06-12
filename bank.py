from datetime import datetime, time
from typing import Type

class Account:
    def __init__(self,name,phone,transactions):
        self.name=name
        self.phone=phone
        self.balance=0
        self.loan=0
        self.loan_limit=500
        self.transactions=[]
   

    def deposit(self,amount):
        try:
            10+amount
        except TypeError:
             return f"The amount must be in figures"
        if amount<=0:
            return f"Amount must be greater than 0."  
        else:
            self.balance+=amount
            transaction={"amount":"amount","balance":"self.balance","time":datetime.now(),"narration":"Deposit"}
            self.transactions.append(transaction)
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
    def get_statement(self):
        for transaction in self.transactions:
            narration=transaction["narration"]
            amount=transaction["amount"]
            balance=transaction["balance"]
            time=transaction["time"]
            print(f'{time.strftime("%D")}date of transaction{narration}, {amount}transacted,and now your balance is {balance}')

    def repay_loan(self,amount):
        if(amount)>0:
              return f"Dear {self.name} you have been loaned an amount of {amount} your new balance is {self.balance}"

        elif  amount<self.loan:
              self.loan-=amount
              return f"Dear customer,you have paid your debt of {amount} your outstanding debt is {self.loan} "
        else:
              difference=amount-self.loan
              self.balance+=difference
              self.loan=0
              return f"Dear customer, you have succesfully paid your loan of {self.loan}, your new balance is{self.balance}"

    def Transfer(self,amount,account):
            try:
             10+amount
            except TypeError:
                return f"the amount must be in figures"
            fee = amount * 0.05

            if amount>0:
                    return f"the amount is less than zero"
            if amount + fee > self.balance:
                return f"your balance is {self.balance},you need{amount+fee} "
            else:
                self.balance=amount+fee 
                account.deposit(amount)
                return f"You have transferred succesfully" 

class MobileMoneyAccount(Account):
    def __init__(self,name,phone,service_provider):
        super().__init__(name,phone)
        self.service_provider=service_provider
        self.limit=300000
    def buy_airtime(self,amount):
        try:
            1+amount
        except TypeError:
            return f"The amount must be in figures"
        if amount<5:
            return f"Dear {self.name} you have to purchase KES 5 or more"
        else:
            self.balance-=amount
            return f"Dear {self.name} you have successfully purchased {amount} airtime.Your new balance is{self.balance}"

    
        
        
         

        

