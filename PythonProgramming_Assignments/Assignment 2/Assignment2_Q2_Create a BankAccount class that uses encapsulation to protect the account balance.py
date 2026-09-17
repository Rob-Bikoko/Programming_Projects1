# BankAccount Program Using Encapsulation to Create a BankAccount class and
# protect the account balance from direct modification
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.__balance = initial_balance # Private attribute

    def deposit(self, amount):
        """Add money to the account."""
        if amount > 0:
            self.__balance += amount
            print(f"${amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
          """Withdraw money from the account."""
          if amount <= 0:
                print("Withdrawal amount must be positive.")
          elif amount > self.__balance:
               print("Insufficient funds.")
          else:
               self.__balance -= amount
               print(f"${amount} withdrawn successfully.")

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.__balance}")


# Create a bank account object
account = BankAccount("Alice", 1000)

# Display initial balance
account.display_balance()

# Deposit money
account.deposit(500)

# Display updated balance
account.display_balance()

# Withdraw money
account.withdraw(300)

# Display final balance
account.display_balance()

# Attempt to access private attribute directly
# This will raise an error:
# print(account.__balance)
