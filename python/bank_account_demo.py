from bank_account import BankAccount

account1 = BankAccount("123", 100)
print(account1)

account2 = BankAccount("456", 100)
print(account2)

account2.deposit(100)
print(account2)