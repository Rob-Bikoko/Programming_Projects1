#Question 5a Encapsulated bank account
#Explain encapsulation and create BankAccount with a protected balance,
#deposit and withdrawal methods, and a balance display method
"""
   Concept explanation
   Encapsulation combines data and the methods that operate on that data inside a class. It also restricts uncontrolled access to the internal state. In Python, an attribute beginning with two underscores, such as __balance, is name-mangled. External code should therefore use the class methods, where validation and business rules can be enforced, instead of changing the balance directly.
   Step by step method
   Step 1. Store the opening balance in self.__balance.
   Step 2. In deposit(), reject amounts that are zero or negative; otherwise add the amount.
   Step 3. In withdraw(), reject non-positive amounts and amounts greater than the available balance.
   Step 4. Provide get_balance() or display_balance() as controlled read access.
   Step 5. Demonstrate that all normal changes occur through the methods.

"""
class BankAccount:
    def __init__(self, opening_balance=0):
        if opening_balance < 0:
            raise ValueError("Opening balance cannot be negative.")
        self.__balance = opening_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be greater than zero.")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be greater than zero.")
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount

    def get_balance(self):
        return self.__balance

    def display_balance(self):
        print(f"Current balance: ${self.__balance:.2f}")
