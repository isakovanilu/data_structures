"""Simple ATM Interface: Simulate an ATM interface 
where a user can check the balance, deposit, 
and withdraw money. This task introduces the 
concept of maintaining state and handling user choices."""


class DebitCard:
    def __init__(self, card_id, pin):
        self.card_id = card_id
        self.pin = pin
