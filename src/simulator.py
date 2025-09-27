import random

class Wallet:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def generate_address(self):
        return "0x" + "".join(random.choice("0123456789abcdef") for _ in range(40))

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        self.balance -= amount
        return self.balance

if __name__ == "__main__":
    wallet = Wallet("Demo Wallet")
    print("New Address:", wallet.generate_address())
    print("Deposit 100:", wallet.deposit(100))
    print("Withdraw 30:", wallet.withdraw(30))
