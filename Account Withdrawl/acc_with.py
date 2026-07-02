class InsufficientFundsError(Exception):
    pass

def withdraw(balance, amount):
   if amount > balance:
       raise InsufficientFundsError("Not enough funds")
    

balance = 5000
amount = 3000

try:
    balance = withdraw(balance, amount)
    print("Withdrawal Successful")
    print("Remaining Balance: ", balance)
    
except InsufficientFundsError as e:
    print(e)