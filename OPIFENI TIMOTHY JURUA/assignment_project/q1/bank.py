class BankAccount:
    def __init__(self, balance=0.0):
        self._balance = float(balance)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if self._balance >= amount:
            self._balance -= amount
            return amount
        raise ValueError("Insufficient funds")

    def get_balance(self):
        return self._balance

# Demo when run directly
if __name__ == '__main__':
    a = BankAccount(100)
    b = BankAccount(50)
    a.deposit(25)
    try:
        a.withdraw(200)
    except Exception as e:
        print('A withdraw failed:', e)
    b.deposit(100)
    b.withdraw(30)
    print('A balance:', a.get_balance())
    print('B balance:', b.get_balance())
