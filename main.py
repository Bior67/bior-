
class BankAccount:
    def __init__(self, account_number, account_type, balance=0.0):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrew: {amount}")
        else:
            print("Invalid withdrawal amount or insufficient funds!")

    def transfer(self, amount, target_account):
        if 0 < amount <= self.balance:
            self.balance -= amount
            target_account.balance += amount
            self.transactions.append(f"Transferred: {amount} to account {target_account.account_number}")
            target_account.transactions.append(f"Received: {amount} from account {self.account_number}")
        else:
            print("Invalid transfer amount or insufficient funds!")

    def get_balance(self):
        return self.balance

    def get_transactions(self):
        return self.transactions

class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.accounts = []

    def create_account(self, account_type, initial_deposit=0.0):
        account_number = f"{self.customer_id}-{len(self.accounts) + 1}"
        new_account = BankAccount(account_number, account_type, initial_deposit)
        self.accounts.append(new_account)

    def get_accounts(self):
        return self.accounts

class Transactions:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_transaction_history(self):
        return self.transactions

# Create customers and accounts
customer1 = Customer("John Doe", "C001")
customer1.create_account("Savings", 1000)
customer1.create_account("Checking", 500)

customer2 = Customer("Jane Smith", "C002")
customer2.create_account("Savings", 1500)

# Perform operations
customer1.get_accounts()[0].deposit(500)
customer1.get_accounts()[1].withdraw(200)
customer1.get_accounts()[0].transfer(300, customer2.get_accounts()[0])

# Check balances and transactions
print(f"Customer 1, Account 1 Balance: {customer1.get_accounts()[0].get_balance()}")
print(f"Customer 1, Account 2 Balance: {customer1.get_accounts()[1].get_balance()}")
print(f"Customer 2, Account 1 Balance: {customer2.get_accounts()[0].get_balance()}")

print("Customer 1, Account 1 Transactions:", customer1.get_accounts()[0].get_transactions())
print("Customer 1, Account 2 Transactions:", customer1.get_accounts()[1].get_transactions())
print("Customer 2, Account 1 Transactions:", customer2.get_accounts()[0].get_transactions())

# Generate account statements
def generate_statement(account):
    statement = f"Account Statement for {account.account_number} ({account.account_type}):\n"
    statement += "Transactions:\n"
    for transaction in account.get_transactions():
        statement += f"- {transaction}\n"
    statement += f"Current Balance: {account.get_balance()}"
    return statement

print(generate_statement(customer1.get_accounts()[0]))
print(generate_statement(customer1.get_accounts()[1]))
print(generate_statement(customer2.get_accounts()[0]))
