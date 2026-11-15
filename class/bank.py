class BankAccount:
    
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insuficient balance")
            
    def show_balance(self):
        print(f"{self.owner}'s balance is {self.balance}")
        
        
def run():
        
    account1 = BankAccount("Terna", 2000)

    account1.deposit(5000)
    account1.withdraw(4000)

    account1.show_balance()