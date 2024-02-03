"""Simple ATM Interface: Simulate an ATM interface 
where a user can check the balance, deposit, 
and withdraw money. This task introduces the 
concept of maintaining state and handling user choices."""


class DebitCard:
    def __init__(self, card_id, pin, first_name, last_name, balance=100):
        self.card_id = card_id
        self.pin = pin
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance
    
    def check_balance(self):
        print(f'Current Balance: {self.balance}')
        
    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        print(f'Deposited: {deposit_amount}$')
        
    def withdraw_amount(self, withdraw_amount):
        if self.balance < withdraw_amount:
            print('Insufficient amount')
        else:
            self.balance -= withdraw_amount
            print(f'Withdrawed: {withdraw_amount}$, remaining balance is {self.balance}')
        
