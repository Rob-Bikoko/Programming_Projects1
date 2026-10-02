#encapsulation
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute

    # It restricts direct access to some of an object('s '
    #  'components to prevent accidental modification and protect the internal state)
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: ${amount}")
        else:
            print("Invalid withdrawal amount")

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

# Create a BankAccount instance
account = BankAccount("123456789")

# Deposit and withdraw money
account.deposit(100)
account.withdraw(50)

# Access the balance and account number
print(f"Account Number: {account.get_account_number()}")
print(f"Current Balance: ${account.get_balance()}")

# Attempt to access private attributes directly (will raise an error)
# print(account.__balance)  # Uncommenting this line will raise an AttributeError

"""
Private Attributes: The attributes __account_number and __balance are private and 
cannot be accessed directly from outside the class.
Public Methods: Methods like deposit(), withdraw(), get_balance(), 
and get_account_number() provide controlled access to the private attributes.
"""
