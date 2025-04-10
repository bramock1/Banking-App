def show_balance(balance):
    return f"Current balance: ${balance}"

def deposit(balance):
    deposit_amount = int(input("Enter amount to deposit: "))
    balance += deposit_amount
    print(f"Current balance: ${balance}")
    return balance
   
def withdraw(balance):
    withdraw_amount = int(input("Enter amount to withdraw: "))
    balance -= withdraw_amount
    print(f"Current balance: ${balance}")
    return balance

def logout(name):
    print(f"Goodbye {name}!")


    
